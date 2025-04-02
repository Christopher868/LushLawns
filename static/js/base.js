setTimeout(function () {
    let alerts = document.querySelectorAll(".alert");
    alerts.forEach(function (alert) {
        alert.style.transition = "opacity 0.5s";
        alert.style.opacity = "0";
        setTimeout(() => alert.remove(), 500);
    });
}, 3000);  // Message disappears after 3 seconds


// toggles dropdown menu
document.addEventListener("DOMContentLoaded", function () {
    let menu = document.getElementById("dropdown-list-id");
    let account_button = document.getElementById("account-dropdown-button");
    let menu_button = document.getElementById("menu-dropdown-button");

    // toggles menu when account button is displayed
    account_button.addEventListener("click", function () {
        let currentDisplay = window.getComputedStyle(menu).display;
        menu.style.display = (currentDisplay === "none") ? "block" : "none";
    });

    // toggles menu when menu symbol is displayed
    menu_button.addEventListener("click", function () {
        let currentDisplay = window.getComputedStyle(menu).display;
        menu.style.display = (currentDisplay === "none") ? "block" : "none";
    });

    // Closes menu if someone clicks elsewhere on screen
    document.addEventListener("click", function (event) {
        if (!menu_button.contains(event.target) && !account_button.contains(event.target) && !menu.contains(event.target)) {
            menu.style.display = "none";
        }
    });
});
