let lastScrollTop = 0;
const navbar = document.querySelector('nav');

// Initialize transition on navbar
navbar.style.transition = 'top 0.4s ease, opacity 0.4s ease';

window.addEventListener('scroll', function() {
  let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

  if (scrollTop > lastScrollTop) {
    // Scroll down - hide navbar
    navbar.style.top = '-80px';  // adjust to your navbar height
    navbar.style.opacity = '0';
  } else {
    // Scroll up - show navbar
    navbar.style.top = '0';
    navbar.style.opacity = '1';
  }

  lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
});

document.addEventListener("DOMContentLoaded", () => {
    const hamburger = document.querySelector(".hamburger");
    const navList = document.querySelector("nav ul");

    if (hamburger && navList) {
        hamburger.addEventListener("click", () => {
            navList.classList.toggle("show");
        });
    }
});
