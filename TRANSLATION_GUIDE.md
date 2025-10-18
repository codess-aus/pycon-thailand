# 🌐 Thai Translation Guide for PyCon Thailand Workshop

## ✅ Translation System Implemented

Your website now supports **bilingual content** with English and Thai versions!

### 📁 File Naming Convention

The mkdocs-static-i18n plugin uses **file suffixes** to identify translations:

- **English files**: `filename.md` (e.g., `index.md`, `the-expert.md`)
- **Thai files**: `filename.th.md` (e.g., `index.th.md`, `the-expert.th.md`)

### 🎯 How It Works

1. **English version** is accessed at: `http://yoursite.com/`
2. **Thai version** is accessed at: `http://yoursite.com/th/`
3. Users can switch between languages using the **language toggle button** in the top-right corner
4. The navigation menu is automatically translated to Thai when viewing Thai pages

### 📝 Translation Status

#### ✅ Fully Translated Pages:
- `index.th.md` - Home page (หน้าแรก)
- `imposter-syndrome.th.md` - Imposter Syndrome page (ซินโดรมผู้แอบอ้าง)
- `the-expert.th.md` - The Expert page (partially translated - ผู้เชี่ยวชาญ)

#### 📋 Pages Ready for Translation:
These files exist but contain English content (copies of original files):
- `contact.th.md`
- `key-takeaways.th.md`
- `resources.th.md`
- `the-natural-genius.th.md`
- `the-perfectionist.th.md`
- `the-soloist.th.md`
- `the-superperson.th.md`

### 🚀 How to Add/Edit Translations

1. **To translate a page**: Open the corresponding `.th.md` file in the `docs/` directory
2. **Replace the English content** with Thai translations
3. **Keep the same structure**: Maintain headings, images, and links
4. **Test locally**: Run `mkdocs serve` and visit `http://localhost:8000/th/` to see your changes

### 🎨 Language Switcher

The language switcher appears as a floating button in the top-right with:
- 🇺🇸 **EN** button - Switch to English
- 🇹🇭 **TH** button - Switch to Thai (เปลี่ยนเป็นภาษาไทย)

The active language is highlighted in purple.

### 📌 Navigation Translations

The navigation menu items are automatically translated when viewing Thai pages:

| English | Thai |
|---------|------|
| Home | หน้าแรก |
| Imposter Syndrome | ซินโดรมผู้แอบอ้าง |
| The Expert | ผู้เชี่ยวชาญ |
| The Perfectionist | นักสมบูรณ์นิยม |
| The Superperson | ซุปเปอร์เปอร์สัน |
| The Natural Genius | อัจฉริยะโดยธรรมชาติ |
| The Soloist | นักเดี่ยว |
| Key Takeaways | ประเด็นสำคัญ |
| Resources | แหล่งข้อมูล |
| Contact Page | ติดต่อเรา |

### 🛠️ Development Commands

```bash
# Build the site
mkdocs build

# Serve locally for testing
mkdocs serve

# Clean build
mkdocs build --clean
```

### 📂 Directory Structure

```
docs/
├── index.md              # English home page
├── index.th.md           # Thai home page
├── imposter-syndrome.md  # English page
├── imposter-syndrome.th.md  # Thai page
├── the-expert.md         # English page
├── the-expert.th.md      # Thai page
└── ...                   # Other pages
```

### ⚠️ Important Notes

1. **Do NOT use the `/th/` directory** - The plugin generates this automatically during build
2. **Keep `.th.md` files in the same `docs/` directory** as the English files
3. **Image paths should be the same** in both language versions (e.g., `assets/image.png`)
4. **Links to other pages** work automatically - the language switcher handles routing

### 🎯 Next Steps

1. **Translate remaining pages**: Edit the `.th.md` files with Thai content
2. **Review translations**: Check the Thai site at `/th/` to ensure proper display
3. **Test language switching**: Click between EN/TH buttons to verify smooth transitions
4. **Deploy**: When ready, build and deploy your bilingual site!

---

**Happy translating! 🎉**
