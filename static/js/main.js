document.addEventListener("DOMContentLoaded", () => {
    const loader = document.getElementById("pageLoader");
    if (loader) {
        window.setTimeout(() => loader.classList.add("hidden"), 180);
    }

    document.querySelectorAll("[data-confirm]").forEach((button) => {
        button.addEventListener("click", (event) => {
            const message = button.getAttribute("data-confirm") || "Are you sure?";
            if (!window.confirm(message)) {
                event.preventDefault();
            }
        });
    });

    const cityButtons = document.querySelectorAll("[data-city-filter]");
    const showItems = document.querySelectorAll("[data-city]");
    cityButtons.forEach((button) => {
        button.addEventListener("click", () => {
            const city = button.dataset.cityFilter;
            cityButtons.forEach((item) => item.classList.remove("active"));
            button.classList.add("active");
            showItems.forEach((item) => {
                item.hidden = city !== "all" && item.dataset.city !== city;
            });
        });
    });
});