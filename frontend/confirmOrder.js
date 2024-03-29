// function pay()
// {
//   $(".receipt").slideUp("slow");
//   $(".paid").slideDown("slow");
// }

document.addEventListener("DOMContentLoaded", function () {

    if (localStorage.getItem("user_id") == null) {
        window.location.href = "/loginRegister.html";
    }

    document.getElementById("Back").addEventListener("click", function () {

        window.location.href = "/productPage.html";
    });

    document.getElementById("Submit").addEventListener("click", function () {
        axios.get(`http://localhost:8000/pay-money/${localStorage.getItem("user_id")}/${localStorage.getItem("address_id")}/${localStorage.getItem("card_number")}`).then((response) => {
        
        console.log(response.data)
    
    
    });
        window.location.href = "/viewProfile.html";


    });


    axios.get("http://localhost:8000/account-detail/?customer_id=" + localStorage.getItem("user_id")).then((response) => {
        console.log(response.data)
        const data = response.data[3][0];
        console.log(data)
        const list_address = document.getElementById("list_address");

        list_address.innerHTML = data.map((address, index) => {
            if (index == 0) {
                showAddress(address._Address__id)
                return ` <a id="drop-down-address${index + 1}" class="selected_address" onclick="showAddress(${address._Address__id})" >${address._Address__house_number}</a>`
            }
            return ` <a id="drop-down-address${index + 1}" onclick="showAddress(${address._Address__id})" >${address._Address__house_number}</a>`
        }).join("");


        list_address.innerHTML += `<a id="drop-down-more-address" href="./addAddress.html">Add New Address</a>`

    })


    axios.get("http://localhost:8000/credit-list/" + localStorage.getItem("user_id")).then((response) => {
        console.log(response.data)
        const data = response.data;
        console.log(data)
        const list_credit = document.getElementById("list_credit");

        list_credit.innerHTML = data.map((card, index) => {
            if (index == 0) {
                showCard(card._CreditCard__id)
                return ` <a id="drop-down-CreditCard${index + 1}" class="selected_credit"  onclick="showCard(${card._CreditCard__id})" >${card._CreditCard__card_name}</a>`
            }
            return ` <a id="drop-down-CreditCard${index + 1}" onclick="showCard(${card._CreditCard__id})" >${card._CreditCard__card_name}</a>`
        }).join("");


        list_credit.innerHTML += `<a id="drop-down-more-CreditCard"  href="./addCreditCard.html">Add New Credit Card</a>`

    })






});
const showCard = (card_id) => {

    axios.get("http://localhost:8000/credit-list/" + localStorage.getItem("user_id")).then((response) => {
        console.log(response.data);
        const data = response.data;
        console.log(data);

        const card = data.filter((item) => item._CreditCard__id == Number(card_id))[0];

        console.log(card)

        const card_name = document.getElementById("card_holder");
        const number = document.getElementById("card_number");
        const pin = document.getElementById("pin_number");
        const type = document.getElementById("type_card");


        card_name.innerText = card._CreditCard__card_name;
        number.innerText = card._CreditCard__number;
        pin.innerText = card._CreditCard__pin_number;
        type.innerText = card._CreditCard__type_card;


        document.querySelectorAll(".selected_credit").forEach((item) => {
            item.classList.remove("selected_credit");
        })


        document.getElementById(`drop-down-CreditCard${card_id}`).classList.add("selected_credit");

        localStorage.setItem("card_id", card_id)
        localStorage.setItem("card_number", card._CreditCard__number)
    })


}








const showAddress = (address_id) => {
    axios.get("http://localhost:8000/account-detail/?customer_id=" + localStorage.getItem("user_id")).then((response) => {

        const data = response.data[3][0];

        console.log(data)
        const name = document.getElementById("name");
        const phone = document.getElementById("phone");
        const number = document.getElementById("number");
        const soi = document.getElementById("soi");
        const road = document.getElementById("road");
        const province = document.getElementById("province");
        const postal_code = document.getElementById("postal_code");

        console.log(address_id)
        const address = data.filter((item) => item._Address__id == Number(address_id));

        console.log(address)


        number.innerText = address[0]._Address__house_number;
        soi.innerText = address[0]._Address__soi;
        road.innerText = address[0]._Address__road;
        province.innerText = address[0]._Address__province;
        postal_code.innerText = address[0]._Address__postal_code;
        name.innerText = address[0]._Address__name;
        phone.innerText = address[0]._Address__phone;

        document.querySelectorAll(".selected_address").forEach((item) => {
            item.classList.remove("selected_address");
        })


        document.getElementById(`drop-down-address${address_id}`).classList.add("selected_address");



        localStorage.setItem("address_id", address_id)
    });

}