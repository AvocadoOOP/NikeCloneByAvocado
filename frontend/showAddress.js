document.addEventListener("DOMContentLoaded", function () {

    if (localStorage.getItem("user_id") == null){
        window.location.href = "/loginRegister.html";
    }

    document.getElementById("Back").addEventListener("click", function(){

        window.location.href = "/viewProfile.html";
    });

    axios.get("http://localhost:8000/account-detail/?customer_id=" + localStorage.getItem("user_id")).then((response) => {
        const number = document.getElementById("number");
        const soi = document.getElementById("soi");
        const road = document.getElementById("road");
        const province = document.getElementById("province");
        const postal_code = document.getElementById("postal_code");
        const name = document.getElementById("name");
        const phone = document.getElementById("phone");

        const data = response.data[3][0];
        console.log(data)
        const address = data.filter((item) => item._Address__id == localStorage.getItem("address_id"));

        number.value = address[0]._Address__house_number;
        soi.value = address[0]._Address__soi;
        road.value = address[0]._Address__road;
        province.value = address[0]._Address__province;
        postal_code.value = address[0]._Address__postal_code;
        name.value = address[0]._Address__name;
        phone.value = address[0]._Address__phone;



    })



});