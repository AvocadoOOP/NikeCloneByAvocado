const cardTypeInputs = document.querySelectorAll('input[name="type_card"]');
const backImage = document.querySelector('.back img[src="PictureForNike/visa.png"]');

let selectedCardType = "";

cardTypeInputs.forEach(input => {
    input.addEventListener('change', changeCardImage);
});

function changeCardImage() {
    const visaImage = document.querySelector('.image img[src="PictureForNike/visa.png"]');
    const masterImage = document.querySelector('.image img[src="PictureForNike/master.png"]');
    const jcbImage = document.querySelector('.image img[src="PictureForNike/jcb.png"]');

    if (this.value === "JCB") {
        visaImage.style.display = 'none';
        masterImage.style.display = 'none';
        jcbImage.style.display = 'block';
        backImage.src = 'PictureForNike/jcb.png';
        selectedCardType = "JCB";
    } else if (this.value === "Master") {
        visaImage.style.display = 'none';
        jcbImage.style.display = 'none';
        masterImage.style.display = 'block';
        backImage.src = 'PictureForNike/master.png';
        selectedCardType = "Master";
    } else {
        masterImage.style.display = 'none';
        jcbImage.style.display = 'none';
        visaImage.style.display = 'block';
        backImage.src = 'PictureForNike/visa.png';
        selectedCardType = "Visa";
    }
}

document.querySelector('.card-number-input').oninput = () =>{
    document.querySelector('.card-number-box').innerText = document.querySelector('.card-number-input').value;
}

document.querySelector('.card-holder-input').oninput = () =>{
    document.querySelector('.card-holder-name').innerText = document.querySelector('.card-holder-input').value;
}

document.querySelector('.cvv-input').onmouseenter = () =>{
    document.querySelector('.front').style.transform = 'perspective(1000px) rotateY(-180deg)';
    document.querySelector('.back').style.transform = 'perspective(1000px) rotateY(0deg)';
}

document.querySelector('.cvv-input').onmouseleave = () =>{
    document.querySelector('.front').style.transform = 'perspective(1000px) rotateY(0deg)';
    document.querySelector('.back').style.transform = 'perspective(1000px) rotateY(180deg)';
}

document.querySelector('.cvv-input').oninput = () =>{
    document.querySelector('.cvv-box').innerText = document.querySelector('.cvv-input').value;
}




  document.addEventListener("DOMContentLoaded", function () {

    if (localStorage.getItem("user_id") == null){
        window.location.href = "/loginRegister.html";
    }

    document.getElementById("Back").addEventListener("click", function(){

        window.location.href = "/viewProfile.html";
    });

    document.getElementById("Submit").addEventListener("click", function(){
          
        if (document.getElementById("card_name").value == "" || document.getElementById("number").value == "" || document.getElementById("pin").value == "" || selectedCardType == ""){
            alert("Please fill all the fields")
            return;
        }
       
        axios.post("http://localhost:8000/credit-add", {
            "customer_id": Number(localStorage.getItem("user_id")),
            "type_card": selectedCardType,
            "card_name": document.getElementById("card_name").value,
            "number": document.getElementById("number").value,
            "pin_number": Number(document.getElementById("pin").value),
          }).then((response) => {
            alert("Address added successfully")
            console.log(response)
            window.location.href = "/viewProfile.html";
          }).catch((error) => {
            alert("Please fill all the fields")
          });




    });



});