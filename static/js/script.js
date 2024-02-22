// navbar = document.querySelector(".li-active").querySelectorAll("a");
// console.log(navbar);

// navbar.forEach(element => {
//     element.addEventListener("click", function(){
//         navbar.forEach(nav=>nav.classList.remove("active"))
//         this.classList.add("active");
//     })
// });

let menuIcon = document.querySelector('#menu-icon');
// console.log(menuIcon)
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x')
    navbar.classList.toggle('active')
}

menuIcon.classList.remove('bx-x')
navbar.classList.remove('active')