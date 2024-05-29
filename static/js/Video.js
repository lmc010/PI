function toggleMenu() {
    var menu = document.getElementById("menu");
    if (menu.classList.contains("open-menu")) {
        menu.classList.remove("open-menu");
    } else {
        menu.classList.add("open-menu");
    }
}