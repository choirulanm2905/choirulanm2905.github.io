// animations.js
document.addEventListener("DOMContentLoaded", function () {
    const animatedElement = document.querySelector(".animated-element");

    if (animatedElement) {
        animatedElement.addEventListener("mouseenter", function () {
            animatedElement.style.transform = "scale(1.2)";
        });

        animatedElement.addEventListener("mouseleave", function () {
            animatedElement.style.transform = "scale(1)";
        });
    }
});
