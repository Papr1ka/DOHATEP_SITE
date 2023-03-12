menu_button = document.getElementById("burger")
go_back_button = document.getElementById("go_back")


function menu_handler(event){
    sidebar = document.getElementById("sidebar")
    sidebar.classList.toggle("visible")
}

function go_back_handler(event){
    window.history.back()
}

if (menu_button != null) {
    menu_button.addEventListener("click", menu_handler)
}

if (go_back_button != null) {
    go_back_button.addEventListener("click", go_back_handler)
}
