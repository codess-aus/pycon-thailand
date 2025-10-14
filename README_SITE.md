# PyCon Thailand Workshop Site

## Build & Deployment Guide

### 1. Install Dependencies

```bash
pip install mkdocs-material mkdocs
```

### 2. Local Development

```bash
mkdocs serve
# Site available at http://127.0.0.1:8000/
```

### 3. Build Static Site

```bash
mkdocs build
# Generates site/ directory
```

### 4. Deploy to GitHub Pages

```bash
mkdocs gh-deploy
# Builds and pushes to gh-pages branch
```

## Directory Structure

- `docs/` — All content source files
- `docs/assets/` — Media and static files
- `docs/demos/` — Code demonstration files
- `docs/stylesheets/` — Custom CSS
- `site/` — Generated output (not in repo)

## Accessibility & Best Practices
- WCAG-compliant color contrast
- Focus indicators for keyboard navigation
- Responsive design for all devices
- Optimized images and videos

## Customization
- Edit `mkdocs.yml` for navigation, theme, and social links
- Add new chapters in `docs/` and update navigation
- Place images/videos in `docs/assets/` with descriptive names
- Update `docs/stylesheets/extra.css` for custom styles
