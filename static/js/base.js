setTimeout(function () {
    let alerts = document.querySelectorAll(".alert");
    alerts.forEach(function (alert) {
        alert.style.transition = "opacity 0.5s";
        alert.style.opacity = "0";
        setTimeout(() => alert.remove(), 500);
    });
}, 3000);  // Message disappears after 3 seconds