# PyCon Thailand Workshop Website

Go directly to the website for this content here: https://codess-aus.github.io/pycon-thailand/

This repository contains the source code and content for the PyCon Thailand workshop website, built with MkDocs Material.

## Features
- Accessibility-first design (WCAG compliant)
- Light/dark theme toggle
- Responsive layout
- Progressive learning chapters
- Syntax-highlighted code examples
- Easy navigation and search

## Structure
- `docs/` — Workshop content and chapters
- `docs/assets/` — Images and videos
- `docs/demos/` — Code samples
- `docs/stylesheets/` — Custom CSS
- `mkdocs.yml` — Site configuration

## How to Run Locally
1. Install dependencies:
   ```bash
   pip install mkdocs-material mkdocs
   ```
2. Start local server:
   ```bash
   mkdocs serve
   ```
3. View at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## How to Deploy
1. Build static site:
   ```bash
   mkdocs build
   ```
2. Deploy to GitHub Pages:
   ```bash
   mkdocs gh-deploy
   ```

## Contributing
Feel free to submit issues or pull requests for improvements, new chapters, or accessibility enhancements.

## License
See `LICENSE` for details.
