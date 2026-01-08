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
