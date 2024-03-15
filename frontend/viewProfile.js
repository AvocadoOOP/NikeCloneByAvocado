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
    try {
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
    } catch (error) {

    }




    axios.get("http://localhost:8000/profile-view/?customer_id=" + localStorage.getItem("user_id")).then((response) => {
        console.log(response.data)
        const username = document.getElementById("username");
        const email = document.getElementById("email");

        username.innerHTML = response.data[0];
        email.innerHTML = response.data[1];



    })

    axios.get("http://localhost:8000/account-detail/?customer_id=" + localStorage.getItem("user_id")).then((response) => {
        console.log(response.data)
        const data = response.data[3][0];
        console.log(data)
        const list_address = document.getElementById("list_address");

        list_address.innerHTML = data.map((address, index) => {
            console.log(address)
            return ` <a id="drop-down-address${index + 1}" onclick="showAddress('${address._Address__id}')" >${address._Address__house_number}</a>`
        }).join("");


        list_address.innerHTML += `<a id="drop-down-more-address" href="./addAddress.html">Add New Address</a>`

    })

    document.getElementById("search_input").addEventListener("keypress", function (e) {
        if (e.key == "Enter") {
            localStorage.setItem("search_input", this.value);
            window.location.href = "/productList.html";
        }
    });


    axios.get("http://localhost:8000/credit-list/" + localStorage.getItem("user_id")).then((response) => {
        console.log(response.data)
        const data = response.data;
        console.log(data)
        const list_credit = document.getElementById("list_credit");

        list_credit.innerHTML = data.map((card, index) => {
            console.log(card)
            return ` <a id="drop-down-CreditCard${index + 1}" onclick="showCard('${card._CreditCard__id}')" >${card._CreditCard__number}</a>`
        }).join("");


        list_credit.innerHTML += `<a id="drop-down-more-CreditCard"  href="./addCreditCard.html">Add New Credit Card</a>`

    })

    axios.get("http://localhost:8000/order/" + localStorage.getItem("user_id")).then((response) => {
        console.log(response.data)
        const data = response.data;
        console.log(data)
        const list_order = document.getElementById("list-order");

        list_order.innerHTML = data.map((order, index) => {
            console.log(order)
            return ` <div class="status-delivery-pad"> 
            <div class="container">
                <div class="head">
                    <p class="head_1">Order <span id="order_number">${String(order._Order__order_id).padStart(4, '0')}</span></p>
                </div>
        
                    <ul>
                        <li>
                            <i class="icon uil uil-bill"></i>
                            <div class="progress one active">
                                <p>1</p>
                                <i class="ic uil uil-check"></i>
                            </div>
                            <p class="text">Order Placed</p>
                        </li>
                        <li>
                            <i class="icon uil uil-box"></i>
                            <div class="progress two">
                                <p>2</p>
                                <i class="ic uil uil-check"></i>
                            </div>
                            <p class="text">Order Shipped</p>
                        </li>
                        <li>
                            <i class="icon uil uil-truck"></i>
                            <div class="progress three">
                                <p>3</p>
                                <i class="ic uil uil-check"></i>
                            </div>
                            <p class="text">On The Way</p>
                        </li>
                        <li>
                            <i class="icon uil uil-house-user"></i>
                            <div class="progress four">
                                <p>4</p>
                                <i class="ic uil uil-check"></i>
                            </div>
                            <p class="text">Order Arrived</p>
                        </li>
                    </ul>
                
                
                
            </div>
            
        </div>`
        }).join("");

        const list_history = document.getElementById("list_history");
        const total_orders = document.getElementById("total_orders");

        total_orders.innerHTML = data.length;
        
        list_history.innerHTML = data.map((order, index) => {

            let date = new Date(order._Order__date);
            let formattedDate = date.getDate() + "-" + (date.getMonth() + 1) + "-" + date.getFullYear();


            return `<div class="flex-row order-row" onclick="view_history(${order._Order__order_id})" >
            <div class="flex-item order-row-item order-num">${String(order._Order__order_id).padStart(4, '0')}</div>
            <div class="flex-item order-row-item">${formattedDate}</div>
            <div class="flex-item order-row-item num-of-items">${order._Order__shopping_cart._ShoppingCart__amount

            }</div>
            <div class="flex-item order-row-item">฿${order._Order__shopping_cart._ShoppingCart__total_price}</div>
            <div class="flex-end-cap"><i class="fa fa-chevron-right" aria-hidden="true"></i></div>
          </div>`
        
        }).join("");

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
const view_history = (order_id) => {

    localStorage.setItem("order_id", order_id)
    window.location.href = "/history.html";
}

