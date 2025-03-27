document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("darkModeToggle");
    const body = document.body;

    // Comprobar si el usuario tenía activado el modo oscuro
    if (localStorage.getItem("darkMode") === "enabled") {
        body.classList.add("dark-mode");
        toggleButton.textContent = "☀️ Modo Claro";
    }

    toggleButton.addEventListener("click", function() {
        body.classList.toggle("dark-mode");

        // Cambiar texto del botón
        if (body.classList.contains("dark-mode")) {
            localStorage.setItem("darkMode", "enabled");
            toggleButton.textContent = "☀️ Modo Claro";
        } else {
            localStorage.setItem("darkMode", "disabled");
            toggleButton.textContent = "🌙 Modo Oscuro";
        }
    });
});
