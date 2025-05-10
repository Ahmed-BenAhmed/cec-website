/**
 * Ignite Tech Hub - Main JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {
    // Project filtering
    initProjectFilters();
    
    // Mobile menu toggle
    initMobileMenu();
  });
  
  /**
   * Initialize project filters
   */
  function initProjectFilters() {
    const filterButtons = document.querySelectorAll('.projects__filter-btn');
    const projectCards = document.querySelectorAll('.project-card');
    
    if (!filterButtons.length || !projectCards.length) return;
    
    filterButtons.forEach(button => {
      button.addEventListener('click', function() {
        // Update active button state
        filterButtons.forEach(btn => btn.classList.remove('projects__filter-btn--active'));
        this.classList.add('projects__filter-btn--active');
        
        const filterValue = this.getAttribute('data-filter');
        
        // Filter projects
        projectCards.forEach(card => {
          const category = card.getAttribute('data-category');
          
          if (filterValue === 'all' || filterValue === category) {
            card.style.display = 'flex';
            // Add animation class for smooth transition
            setTimeout(() => {
              card.style.opacity = '1';
              card.style.transform = 'translateY(0)';
            }, 50);
          } else {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            setTimeout(() => {
              card.style.display = 'none';
            }, 300);
          }
        });
      });
    });
  }
  
  /**
   * Initialize mobile menu
   */
  function initMobileMenu() {
    const menuToggle = document.querySelector('.header__menu-toggle');
    const navList = document.querySelector('.header__nav-list');
    
    if (!menuToggle || !navList) return;
    
    menuToggle.addEventListener('click', function() {
      this.classList.toggle('header__menu-toggle--active');
      navList.classList.toggle('header__nav-list--active');
      
      // Toggle aria-expanded for accessibility
      const expanded = this.getAttribute('aria-expanded') === 'true' || false;
      this.setAttribute('aria-expanded', !expanded);
    });
    
    // Close mobile menu on window resize
    window.addEventListener('resize', function() {
      if (window.innerWidth >= 992) {
        menuToggle.classList.remove('header__menu-toggle--active');
        navList.classList.remove('header__nav-list--active');
        menuToggle.setAttribute('aria-expanded', 'false');
      }
    });
  }
  
  /**
   * Animate elements when they come into view
   */
  function initScrollAnimations() {
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    
    if (!animatedElements.length) return;
    
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.2
    });
    
    animatedElements.forEach(element => {
      observer.observe(element);
    });
  }
  
  /**
   * Smooth scroll to anchors
   */
  function initSmoothScroll() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]:not([href="#"])');
    
    if (!anchorLinks.length) return;
    
    anchorLinks.forEach(link => {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
          const offsetTop = targetElement.getBoundingClientRect().top + window.pageYOffset;
          
          window.scrollTo({
            top: offsetTop - 80, // Adjust for header height
            behavior: 'smooth'
          });
          
          // Update URL hash
          history.pushState(null, null, targetId);
        }
      });
    });
  }