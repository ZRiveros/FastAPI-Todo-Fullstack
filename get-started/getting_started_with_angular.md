# Getting Started with Angular

## 🟦 Step 1 — Install Node Version Manager (NVM)

This lets you install Node properly.

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

Reload the terminal:

```bash
source ~/.bashrc
```

Verify NVM is installed:

```bash
nvm --version
```

## 🟦 Step 2 — Install Node (LTS)

```bash
nvm install --lts
```

Then test:

```bash
node -v
npm -v
```

## 🟦 Step 3 — Install Angular CLI

```bash
npm install -g @angular/cli
```

Test version:

```bash
ng version
```

## ✅ 2. Create your Angular project (the right way!)

Do this outside your backend project because you'll call from this to the frontend.

```bash
cd ~
mkdir fastapi_todo_front
cd fastapi_todo_front
ng new fastapi-todo-front
```

## 🟦 Start Angular:

```bash
cd fastapi-todo-front
ng serve --open
```

This will start the development server and automatically open your browser to `http://localhost:4200`.

---

## Next Steps

After setting up Angular, follow the guides in this repository:

- **ANGULAR_TYPESCRIPT_GUIDE.md** - Complete guide to understanding Angular and TypeScript
- **ANGULAR_BEST_PRACTICES.md** - Best practices for API calls with HttpClient
