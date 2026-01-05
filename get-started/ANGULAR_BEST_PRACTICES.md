# Angular Best Practices - API calls with HttpClient

## Overview

This project uses Angular's `HttpClient` to communicate with FastAPI backend.

## Structure

### 1. Environment configuration

- `src/environments/environment.ts` - Development environment
- `src/environments/environment.prod.ts` - Production environment

This makes it easy to switch API URLs between different environments.

### 2. Service (TodoService)

The service is a singleton that handles all API calls. It uses:

- **HttpClient** for HTTP requests
- **RxJS Observables** for asynchronous handling
- **Centralized error handling** via `handleError()`
- **Retry logic** for GET requests
- **TypeScript interfaces** for type safety

### 3. Using the service in a component

```typescript
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TodoService } from './services/todo.service';
import { Todo } from './models/todo';

@Component({
  selector: 'app-todo-list',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="todo-container">
      <h2>My Todos</h2>

      <!-- Loading state -->
      <div *ngIf="loading">Loading...</div>

      <!-- Error state -->
      <div *ngIf="error" class="error">{{ error }}</div>

      <!-- Todo list -->
      <ul *ngIf="!loading && !error">
        <li *ngFor="let todo of todos">
          {{ todo.title }}
          <button (click)="deleteTodo(todo.id!)">Delete</button>
        </li>
      </ul>

      <!-- Add new todo -->
      <button (click)="addTodo()">Add Todo</button>
    </div>
  `,
})
export class TodoListComponent implements OnInit {
  todos: Todo[] = [];
  loading = false;
  error: string | null = null;

  constructor(private todoService: TodoService) {}

  ngOnInit(): void {
    this.loadTodos();
  }

  // Fetch all todos
  loadTodos(): void {
    this.loading = true;
    this.error = null;

    this.todoService.getTodos().subscribe({
      next: (data) => {
        this.todos = data;
        this.loading = false;
      },
      error: (err) => {
        this.error = err.message;
        this.loading = false;
        console.error('Error fetching todos:', err);
      },
    });
  }

  // Create new todo
  addTodo(): void {
    const newTodo: Todo = {
      title: 'New task',
      description: 'Description',
    };

    this.todoService.createTodo(newTodo).subscribe({
      next: (todo) => {
        this.todos.push(todo);
        console.log('Todo created:', todo);
      },
      error: (err) => {
        this.error = err.message;
        console.error('Error creating todo:', err);
      },
    });
  }

  // Update todo
  updateTodo(id: string, updatedData: Partial<Todo>): void {
    const todo = this.todos.find((t) => t.id === id);
    if (!todo) return;

    const updated = { ...todo, ...updatedData };

    this.todoService.updateTodo(id, updated).subscribe({
      next: (result) => {
        const index = this.todos.findIndex((t) => t.id === id);
        if (index !== -1) {
          this.todos[index] = result;
        }
        console.log('Todo updated:', result);
      },
      error: (err) => {
        this.error = err.message;
        console.error('Error updating:', err);
      },
    });
  }

  // Delete todo
  deleteTodo(id: string): void {
    this.todoService.deleteTodo(id).subscribe({
      next: () => {
        this.todos = this.todos.filter((t) => t.id !== id);
        console.log('Todo deleted');
      },
      error: (err) => {
        this.error = err.message;
        console.error('Error deleting:', err);
      },
    });
  }
}
```

## Important concepts

### Observables vs Promises

Angular uses **RxJS Observables** instead of Promises:

- `subscribe()` to subscribe to data
- Automatic unsubscription when component is destroyed (with async pipe or OnDestroy)
- Support for operators like `map`, `filter`, `retry`, etc.

### Subscribe pattern

```typescript
this.todoService.getTodos().subscribe({
  next: (data) => {
    /* Handle success */
  },
  error: (err) => {
    /* Handle error */
  },
  complete: () => {
    /* Optional: Call is complete */
  },
});
```

### Async Pipe (Alternative method)

You can also use async pipe in template to avoid manual subscription:

```typescript
export class TodoListComponent {
  todos$ = this.todoService.getTodos();

  constructor(private todoService: TodoService) {}
}
```

```html
<ul>
  <li *ngFor="let todo of todos$ | async">{{ todo.title }}</li>
</ul>
```

### Unsubscribe best practices

To avoid memory leaks:

```typescript
import { Component, OnDestroy } from '@angular/core';
import { Subject, takeUntil } from 'rxjs';

export class MyComponent implements OnDestroy {
  private destroy$ = new Subject<void>();

  ngOnInit() {
    this.todoService
      .getTodos()
      .pipe(takeUntil(this.destroy$))
      .subscribe((data) => {
        // Handle data
      });
  }

  ngOnDestroy() {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

## CORS handling

If you get CORS errors, add this to your FastAPI backend:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Tips for Internship

1. **Use TypeScript interfaces** - Provides type safety and autocomplete
2. **Centralize API calls** - Everything in services, not in components
3. **Error handling** - Show user-friendly error messages
4. **Loading states** - Show when data is loading
5. **Environment files** - Different URLs for dev/prod
6. **Unsubscribe** - Avoid memory leaks with takeUntil or async pipe

## Troubleshooting

- **Cannot find module 'rxjs'**: Run `npm install`
- **CORS error**: Check FastAPI CORS settings
- **Connection refused**: Check that backend is running on the right port
- **404 errors**: Verify API endpoint paths
