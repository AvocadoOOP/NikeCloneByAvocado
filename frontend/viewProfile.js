document.addEventListener("DOMContentLoaded", function () {
    Array.from(document.getElementsByClassName("men_product")).forEach((card) => {
        card.addEventListener("click", function () {
            localStorage.setItem("product", "Men")
            window.location.href = "/productList.html";
        });
    });

    Array.from(document.getElementsByClassName("women_product")).forEach((card) => {
        card.addEventListener("click", function () {
            localStorage.setItem("product", "Women")
            window.location.href = "/productList.html";
        });
    });

    Array.from(document.getElementsByClassName("kids_product")).forEach((card) => {
        card.addEventListener("click", function () {
            localStorage.setItem("product", "Kids")
            window.location.href = "/productList.html";
        });
    });

    Array.from(document.getElementsByClassName("all_product")).forEach((card) => {
        card.addEventListener("click", function () {
            localStorage.setItem("product", "all")
            window.location.href = "/productList.html";
        });
    });

    document.getElementById("user").addEventListener("click", function(){
        if (localStorage.getItem("user_id") == null){
            window.location.href = "/login.html";
        }
        else{
            window.location.href = "/viewProfile.html";
        }
    });


    const one = document.querySelector(".one");
    const two = document.querySelector(".two");
    const three = document.querySelector(".three");
    const four = document.querySelector(".four");
    const five = document.querySelector(".five");

    one.onclick = function () {
        one.classList.add("active");
        two.classList.remove("active");
        three.classList.remove("active");
        four.classList.remove("active");
        five.classList.remove("active");
    }

    two.onclick = function () {
        one.classList.add("active");
        two.classList.add("active");
        three.classList.remove("active");
        four.classList.remove("active");
        five.classList.remove("active");
    }
    three.onclick = function () {
        one.classList.add("active");
        two.classList.add("active");
        three.classList.add("active");
        four.classList.remove("active");
        five.classList.remove("active");
    }
    four.onclick = function () {
        one.classList.add("active");
        two.classList.add("active");
        three.classList.add("active");
        four.classList.add("active");
        five.classList.remove("active");
    }
    five.onclick = function () {
        one.classList.add("active");
        two.classList.add("active");
        three.classList.add("active");
        four.classList.add("active");
        five.classList.add("active");
    }



});


