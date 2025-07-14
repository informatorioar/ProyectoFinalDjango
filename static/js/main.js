document.addEventListener('DOMContentLoaded', function() {
    // Highlight active nav tab
    function highlightActiveTab() {
        const currentUrl = window.location.pathname;
        const navTabs = document.querySelectorAll('.nav-tab');
        
        navTabs.forEach(tab => {
            const tabUrl = tab.getAttribute('href');
            
            // Check if current URL matches tab URL
            if (currentUrl === tabUrl || 
               (currentUrl.startsWith(tabUrl) && tabUrl !== '/')) {
                tab.classList.add('active');
            } else {
                tab.classList.remove('active');
            }
        });
    }
    
    // Add hover effects
    function setupHoverEffects() {
        const navTabs = document.querySelectorAll('.nav-tab');
        
        navTabs.forEach(tab => {
            tab.addEventListener('mouseover', function() {
                if (!this.classList.contains('active')) {
                    this.style.color = '#ffc107';
                }
            });
            
            tab.addEventListener('mouseout', function() {
                if (!this.classList.contains('active')) {
                    this.style.color = '#bdbdbd';
                }
            });
        });
    }
    
    // Initialize functions
    highlightActiveTab();
    setupHoverEffects();
    
    // Re-run when navigating via AJAX/pjax if needed
    window.addEventListener('popstate', highlightActiveTab);
});