setTimeout(function () {
    let alerts = document.querySelectorAll(".alert");
    alerts.forEach(function (alert) {
        alert.style.transition = "opacity 0.5s";
        alert.style.opacity = "0";
        setTimeout(() => alert.remove(), 500);
    });
}, 3000);  // Message disappears after 3 seconds



// function toggleDisplay(elementId) {
//     const element = document.getElementById(elementId);

//     console.log(element);
//     if (element.style.display === "none") {
//         element.style.display = "block";
//     } else {
//         element.style.display = "none";
//     }
// }


document.addEventListener("DOMContentLoaded", function () {
    let menu = document.getElementById("dropdown-list-id");
    let account_button = document.getElementById("account-dropdown-button");
    let menu_button = document.getElementById("menu-dropdown-button");

    account_button.addEventListener("click", function () {
        let currentDisplay = window.getComputedStyle(menu).display;
        menu.style.display = (currentDisplay === "none") ? "block" : "none";
    });

    menu_button.addEventListener("click", function () {
        let currentDisplay = window.getComputedStyle(menu).display;
        menu.style.display = (currentDisplay === "none") ? "block" : "none";
    });
});
