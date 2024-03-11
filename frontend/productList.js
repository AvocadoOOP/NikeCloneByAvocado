document.addEventListener("DOMContentLoaded", function () {

    document.getElementById("user").addEventListener("click", function(){
        if (localStorage.getItem("user_id") == null){
            window.location.href = "/login.html";
        }
        else{
            window.location.href = "/viewProfile.html";
        }
    });
    
    
    Array.from(document.getElementsByClassName("men_product")).forEach((card) => {
        card.addEventListener("click", function () {
            localStorage.setItem("product", "men")
            window.location.href = "/productList.html";
        });
    });

    Array.from(document.getElementsByClassName("women_product")).forEach((card) => {
        card.addEventListener("click", function () {
            localStorage.setItem("product", "women")
            window.location.href = "/productList.html";
        });
    });

    Array.from(document.getElementsByClassName("kids_product")).forEach((card) => {
        card.addEventListener("click", function () {
            localStorage.setItem("product", "kids")
            window.location.href = "/productList.html";
        });
    });

    Array.from(document.getElementsByClassName("all_product")).forEach((card) => {
        card.addEventListener("click", function () {
            localStorage.setItem("product", "all")
            window.location.href = "/productList.html";
        });
    });
});