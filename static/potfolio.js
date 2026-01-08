// Smooth scroll for anchor links (if you ever use #section)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
            target.scrollIntoView({
                behavior: "smooth"
            });
        }
    });
});document.addEventListener('DOMContentLoaded', () => {
  const content = document.querySelector('.content-section');
  
  let isDragging = false;
  let startX, startY;
  let origX = 0, origY = 0;
  
  content.style.position = 'absolute';  // Make sure it can move freely
  
  content.addEventListener('mousedown', (e) => {
    isDragging = true;
    startX = e.clientX;
    startY = e.clientY;
    
    // Get current position
    const rect = content.getBoundingClientRect();
    origX = rect.left;
    origY = rect.top;
    
    content.style.cursor = 'grabbing';
  });
  
  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    
    const dx = e.clientX - startX;
    const dy = e.clientY - startY;
    
    content.style.left = origX + dx + 'px';
    content.style.top = origY + dy + 'px';
  });
  
  window.addEventListener('mouseup', () => {
    if (isDragging) {
      isDragging = false;
      content.style.cursor = 'grab';
    }
  });
  
  // Set initial cursor style
  content.style.cursor = 'grab';
});


// Toggle mobile sidebar
document.addEventListener("DOMContentLoaded", () => {
    const hamburger = document.querySelector(".hamburger");
    const navList = document.querySelector("nav ul");

    if (hamburger && navList) {
        hamburger.addEventListener("click", () => {
            navList.classList.toggle("show");
        });
    }
});
