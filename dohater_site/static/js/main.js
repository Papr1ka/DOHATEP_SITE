sidebar = document.getElementById("sidebar")
menu_button = document.getElementById("burger")


function menu_handler(event){
    sidebar = document.getElementById("sidebar")
    sidebar.classList.toggle("visible")
}

menu_button.addEventListener("click", menu_handler)