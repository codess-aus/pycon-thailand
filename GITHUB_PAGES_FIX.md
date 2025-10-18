# GitHub Pages Deployment Fix

## Issues Fixed

### 1. **Missing i18n Plugin in Deployment**
**Problem:** The `mkdocs-static-i18n` plugin wasn't being installed during GitHub Actions deployment.

**Solution:** Updated `.github/workflows/deploy.yml` to include the plugin:
```yaml
pip install mkdocs-material mkdocs mkdocs-static-i18n
```

### 2. **404 Errors and Broken Language Switcher**
**Problem:** GitHub Pages serves from `/pycon-thailand/` base URL, but the language switcher was using absolute paths like `/th/`, causing 404 errors.

**Solution:** Updated configuration to handle GitHub Pages base URL:

#### mkdocs.yml Changes:
```yaml
site_url: https://codess-aus.github.io/pycon-thailand/
repo_url: https://github.com/codess-aus/pycon-thailand
repo_name: codess-aus/pycon-thailand

extra:
  alternate:
    - name: English
      link: /pycon-thailand/
      lang: en
    - name: ไทย
      link: /pycon-thailand/th/
      lang: th
```

#### overrides/main.html Changes:
Updated the `switchLanguage()` function to properly handle the base URL:
```javascript
const baseUrl = '/pycon-thailand'; // GitHub Pages base URL

// Extract the path after the base URL
let relativePath = currentPath;
if (currentPath.startsWith(baseUrl)) {
  relativePath = currentPath.substring(baseUrl.length);
}
```

### 3. **Accessibility Issues (Header/Menu Contrast)**
**Problem:** Header navigation text had poor contrast against the purple gradient background.

**Solution:** Already fixed in `docs/stylesheets/extra.css` with:
```css
.md-header__title,
.md-header__button,
.md-tabs__link {
    color: #ffffff !important;
}
```

## Deployment Workflow

When you push to `main`:
1. GitHub Actions installs all dependencies (including i18n plugin)
2. MkDocs builds both English and Thai versions
3. Site is deployed to GitHub Pages at: `https://codess-aus.github.io/pycon-thailand/`

## Testing Locally

To test with the GitHub Pages base URL locally:
```bash
mkdocs build
cd site
python -m http.server 8000
# Visit: http://localhost:8000/pycon-thailand/
```

Or use MkDocs serve (no base URL):
```bash
mkdocs serve
# Visit: http://localhost:8000/
```

## Language Switcher Behavior

- **English pages**: `https://codess-aus.github.io/pycon-thailand/`
- **Thai pages**: `https://codess-aus.github.io/pycon-thailand/th/`
- Clicking EN/TH buttons switches between corresponding pages
- Active language button is highlighted with purple gradient

## Files Modified

1. `.github/workflows/deploy.yml` - Added i18n plugin to dependencies
2. `mkdocs.yml` - Added site_url, repo_url, and updated alternate links
3. `overrides/main.html` - Updated language switcher to handle base URL
4. `docs/stylesheets/extra.css` - Already had accessibility fixes

All changes are committed and ready to push!
