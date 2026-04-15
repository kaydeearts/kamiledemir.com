# kamiledemir.com

Personal portfolio site built with [Astro](https://astro.build) and [Tailwind CSS v4](https://tailwindcss.com).

## Getting started

**Prerequisites:** Node.js (v18 or higher) and npm.

Install dependencies:

```bash
npm install
```

Start the dev server:

```bash
npm run dev
```

Opens at `http://localhost:4321`. The site hot-reloads as you edit files.

## Commands

| Command | Description |
|---|---|
| `npm run dev` | Start local dev server |
| `npm run build` | Build for production (outputs to `dist/`) |
| `npm run preview` | Preview the production build locally |

## Project structure

```
kamiledemir.com/
├── public/
│   └── images/
│       └── hero/       # Photos shown in the hero section
├── src/
│   ├── components/     # Astro components (Nav, Hero, About, etc.)
│   ├── layouts/        # Base HTML layout
│   ├── pages/          # index.astro (single page)
│   └── styles/         # CSS files per section
└── astro.config.mjs
```

## Adding hero photos

Drop images into `public/images/hero/`. Supported formats: `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`, `.jfif`.

The hero section picks them up automatically — no code changes needed.

## Deployment

The site is deployed via [Netlify](https://netlify.com), connected to this repo. Every push to `main` triggers an automatic deploy.
