const navToggle = document.querySelector(".nav-toggle");
const header = document.querySelector(".site-header");

if (navToggle && header) {
    navToggle.addEventListener("click", () => {
        const open = header.classList.toggle("nav-open");
        navToggle.setAttribute("aria-expanded", String(open));
    });
}

const procedureButtons = document.querySelectorAll(".procedure-item");
const procedureDetail = document.querySelector(".procedure-detail");

procedureButtons.forEach((button) => {
    button.addEventListener("click", () => {
        procedureButtons.forEach((item) => item.classList.remove("is-active"));
        button.classList.add("is-active");
        if (procedureDetail) {
            procedureDetail.textContent = button.dataset.detail || "";
        }
    });
});
