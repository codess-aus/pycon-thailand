/**
 * Language Switcher for PyCon Thailand Workshop
 * Handles switching between English and Thai versions
 */

class LanguageSwitcher {
  constructor() {
    this.currentLang = this.detectLanguage();
    this.init();
  }

  detectLanguage() {
    const path = window.location.pathname;
    return path.startsWith('/th/') ? 'th' : 'en';
  }

  init() {
    // Update active buttons on page load
    this.updateActiveButtons();
    
    // Set up event listeners
    document.addEventListener('DOMContentLoaded', () => {
      this.updateActiveButtons();
    });
  }

  updateActiveButtons() {
    const enBtn = document.querySelector('[data-lang="en"]');
    const thBtn = document.querySelector('[data-lang="th"]');
    
    if (enBtn && thBtn) {
      if (this.currentLang === 'th') {
        enBtn.classList.remove('active');
        thBtn.classList.add('active');
      } else {
        enBtn.classList.add('active');
        thBtn.classList.remove('active');
      }
    }
  }

  switchLanguage(targetLang) {
    if (targetLang === this.currentLang) {
      return; // Already on target language
    }

    const currentPath = window.location.pathname;
    let newPath;

    if (targetLang === 'th') {
      // Switch to Thai
      if (currentPath === '/' || currentPath === '/index.html') {
        newPath = '/th/';
      } else {
        newPath = '/th' + currentPath;
      }
    } else {
      // Switch to English
      if (currentPath.startsWith('/th/')) {
        newPath = currentPath.replace(/^\/th/, '') || '/';
      } else {
        newPath = currentPath;
      }
    }

    // Add loading animation
    document.body.classList.add('language-switching');
    
    // Store scroll position
    sessionStorage.setItem('scrollPosition', window.scrollY.toString());
    
    // Navigate to new path
    window.location.href = newPath;
  }

  // Restore scroll position after language switch
  restoreScrollPosition() {
    const savedPosition = sessionStorage.getItem('scrollPosition');
    if (savedPosition) {
      window.scrollTo(0, parseInt(savedPosition));
      sessionStorage.removeItem('scrollPosition');
    }
  }
}

// Global function for template use
function switchLanguage(lang) {
  if (window.langSwitcher) {
    window.langSwitcher.switchLanguage(lang);
  }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  window.langSwitcher = new LanguageSwitcher();
  
  // Restore scroll position if coming from language switch
  setTimeout(() => {
    window.langSwitcher.restoreScrollPosition();
  }, 100);
});

// Handle browser back/forward buttons
window.addEventListener('popstate', function() {
  window.langSwitcher = new LanguageSwitcher();
});