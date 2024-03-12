document.addEventListener("DOMContentLoaded", function () {

    if (localStorage.getItem("user_id") == null){
        window.location.href = "/loginRegister.html";
    }

    document.getElementById("Back").addEventListener("click", function(){

        window.location.href = "/viewProfile.html";
    });

    document.getElementById("Submit").addEventListener("click", function(){

        

        axios.post("http://localhost:8000/address-add", {
            "customer_id": Number(localStorage.getItem("user_id")),
            "house_number": document.getElementById("number").value,
            "soi": document.getElementById("soi").value,
            "road": document.getElementById("road").value,
            "province": document.getElementById("province").value,
            "postal_code": document.getElementById("postal_code").value,
          }).then((response) => {
            alert("Address added successfully")
            console.log(response)
            window.location.href = "/viewProfile.html";
          }).catch((error) => {
            alert("Please fill all the fields")
          });




    });



});