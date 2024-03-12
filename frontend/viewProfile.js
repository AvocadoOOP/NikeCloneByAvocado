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

    document.getElementById("user").addEventListener("click", function () {
        if (localStorage.getItem("user_id") == null) {
            window.location.href = "/loginRegister.html";
        }
        else {
            window.location.href = "/viewProfile.html";
        }
    });

    document.getElementById("logout").addEventListener("click", function () {
        localStorage.removeItem("user_id");
        window.location.href = "/loginRegister.html";
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


    try {

        five.onclick = function () {
            one.classList.add("active");
            two.classList.add("active");
            three.classList.add("active");
            four.classList.add("active");
            five.classList.add("active");
        }
    } catch (error) {

    }




    axios.get("http://localhost:8000/profile-view/?customer_id=" + localStorage.getItem("user_id")).then((response) => {
        console.log(response.data)
        const username = document.getElementById("username");
        const email = document.getElementById("email");
        const phone = document.getElementById("phone");

        username.innerHTML = response.data[0];
        email.innerHTML = response.data[1];
        phone.innerHTML = response.data[2];


    })

    axios.get("http://localhost:8000/account-detail/?customer_id=" + localStorage.getItem("user_id")).then((response) => {
        console.log(response.data)
        const data = response.data[3][0];
        console.log(data)
        const list_address = document.getElementById("list_address");

        list_address.innerHTML = data.map((address, index) => {
            console.log(address)
            return ` <a id="drop-down-address${index+1}" onclick="showAddress('${address._Address__id}')" >${address._Address__house_number}</a>`
        }).join("");


        list_address.innerHTML += `<a id="drop-down-more-address" href="./addAddress.html">Add New Address</a>`

    })


    axios.get("http://localhost:8000/credit-list/" + localStorage.getItem("user_id")).then((response) => {
        console.log(response.data)
        const data = response.data;
        console.log(data)
        const list_credit = document.getElementById("list_credit");

        list_credit.innerHTML = data.map((card, index) => {
            console.log(card)
            return ` <a id="drop-down-CreditCard${index+1}" onclick="showCard('${card._CreditCard__id}')" >${card._CreditCard__card_name}</a>`
        }).join("");


        list_credit.innerHTML += `<a id="drop-down-more-CreditCard"  href="./addCreditCard.html">Add New Credit Card</a>`

    })
    



});


const showAddress = (address_id) => {

    localStorage.setItem("address_id", address_id)
    window.location.href = "/showAddress.html";
}

const showCard = (card_id) => {

    localStorage.setItem("card_id", card_id)
    window.location.href = "/showCreditCard.html";
}
