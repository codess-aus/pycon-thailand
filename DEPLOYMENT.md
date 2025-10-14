# 🚀 GitHub Pages Deployment Setup

This repository is configured to automatically deploy the MkDocs site to GitHub Pages using GitHub Actions.

## 📋 Required GitHub Settings

### 1. Enable GitHub Actions Workflow Permissions

Go to your repository settings and configure the following:

**Settings → Actions → General → Workflow permissions**

✅ Select: **"Read and write permissions"**  
✅ Check: **"Allow GitHub Actions to create and approve pull requests"**

Click **Save**

### 2. Configure GitHub Pages Source

**Settings → Pages → Build and deployment**

⚠️ **IMPORTANT**: Choose the correct deployment method:

**Option A: Deploy from Branch (RECOMMENDED for this setup)**
- **Source**: Deploy from a branch
- **Branch**: Select `gh-pages` and `/` (root)

Click **Save**

**Note**: The workflow pushes to the `gh-pages` branch, so this is the correct setting for our setup.

## 🔄 How It Works

The workflow (`.github/workflows/deploy.yml`) will:

1. **Trigger automatically** when you push to the `main` branch
2. **Install dependencies** (mkdocs-material, mkdocs)
3. **Build the site** using MkDocs
4. **Deploy to GitHub Pages** using the `gh-pages` branch

## 📝 Manual Deployment (Optional)

You can also manually deploy using the command line:

```bash
mkdocs gh-deploy
```

## 🌐 Accessing Your Site

After the first successful deployment, your site will be available at:

```
https://codess-aus.github.io/pycon-thailand/
```

⏱️ **Note**: The first deployment may take 2-5 minutes to become available.

## 🔍 Monitoring Deployments

- Go to the **Actions** tab in your repository
- Click on the latest workflow run to see deployment status
- Check for any errors in the workflow logs

## 🛠️ Troubleshooting

### If the workflow fails:

1. **Check workflow permissions** (see step 1 above)
2. **Verify the gh-pages branch** is selected in Pages settings
3. **Check the Actions tab** for specific error messages

### If the site doesn't update:

1. **Clear your browser cache** (Ctrl+Shift+R or Cmd+Shift+R)
2. **Wait a few minutes** for GitHub Pages to propagate changes
3. **Check GitHub Pages status** in Settings → Pages

## 📦 Dependencies

The workflow automatically installs:
- `mkdocs` - Static site generator
- `mkdocs-material` - Material theme for MkDocs

These are specified in `.github/workflows/deploy.yml`
