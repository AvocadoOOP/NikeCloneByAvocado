document.addEventListener("DOMContentLoaded", function() {
    document.querySelector(".one").addEventListener("click", function(){
        document.querySelector(".product-img").src = "PictureForNike/air-max-90-lv8-04.png";
        document.querySelectorAll(".variant").forEach(function(element) {
            element.classList.remove("active");
        });
        this.classList.add("active");
    });

    document.getElementById("user").addEventListener("click", function(){
        if (localStorage.getItem("user_id") == null){
            window.location.href = "/login.html";
        }
        else{
            window.location.href = "/viewProfile.html";
        }
    });

    Array.from(document.getElementsByClassName("men_product")).forEach((card) => {
        card.addEventListener("click", function() {
            localStorage.setItem("product" , "Men")
            window.location.href = "/productList.html";
        });
    });

    Array.from(document.getElementsByClassName("women_product")).forEach((card) => {
        card.addEventListener("click", function() {
            localStorage.setItem("product" , "Women")
            window.location.href = "/productList.html";
        });
    });

    Array.from(document.getElementsByClassName("kids_product")).forEach((card) => {
        card.addEventListener("click", function() {
            localStorage.setItem("product" , "Kids")
            window.location.href = "/productList.html";
        });
    });

    Array.from(document.getElementsByClassName("all_product")).forEach((card) => {
        card.addEventListener("click", function() {
            localStorage.setItem("product" , "all")
            window.location.href = "/productList.html";
        });
    });


    document.querySelector(".two").addEventListener("click", function(){
        document.querySelector(".product-img").src = "PictureForNike/air-max-90-lv8-01.png";
        document.querySelectorAll(".variant").forEach(function(element) {
            element.classList.remove("active");
        });
        this.classList.add("active");
        document.querySelector(".images").innerHTML = "";
    });

    document.querySelector(".three").addEventListener("click", function(){
        document.querySelector(".product-img").src = "PictureForNike/air-max-90-lv8-02.png";
        document.querySelectorAll(".variant").forEach(function(element) {
            element.classList.remove("active");
        });
        this.classList.add("active");
    });

    document.querySelector(".four").addEventListener("click", function(){
        document.querySelector(".product-img").src = "PictureForNike/air-max-90-lv8-03.png";
        document.querySelectorAll(".variant").forEach(function(element) {
            element.classList.remove("active");
        });
        this.classList.add("active");
    });
});

let slider = document.querySelector('.slider .list');
let items = document.querySelectorAll('.slider .list .item');
let next = document.getElementById('next');
let prev = document.getElementById('prev');
let dots = document.querySelectorAll('.slider .dots li');

let lengthItems = items.length - 1;
let active = 0;
next.onclick = function(){
    active = active + 1 <= lengthItems ? active + 1 : 0;
    reloadSlider();
}
prev.onclick = function(){
    active = active - 1 >= 0 ? active - 1 : lengthItems;
    reloadSlider();
}
let refreshInterval = setInterval(()=> {next.click()}, 3000);
function reloadSlider(){
    slider.style.left = -items[active].offsetLeft + 'px';
    // 
    let last_active_dot = document.querySelector('.slider .dots li.dotActive');
    last_active_dot.classList.remove('dotActive');
    dots[active].classList.add('dotActive');

    clearInterval(refreshInterval);
    refreshInterval = setInterval(()=> {next.click()}, 3000);

    
}


dots.forEach((li, key) => {
    li.addEventListener('click', ()=>{
         active = key;
         reloadSlider();
    })
})
window.onresize = function(event) {
    reloadSlider();
};
