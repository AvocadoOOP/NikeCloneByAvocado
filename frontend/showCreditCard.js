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






document.addEventListener("DOMContentLoaded", function () {

    if (localStorage.getItem("user_id") == null) {
        window.location.href = "/loginRegister.html";
    }

    document.getElementById("Back").addEventListener("click", function () {

        window.location.href = "/viewProfile.html";
    });


    axios.get("http://localhost:8000/credit-list/" + localStorage.getItem("user_id")).then((response) => {
        console.log(response.data)
        const data = response.data;
        console.log(data)
        const creditCard = data.filter((item) => item._CreditCard__id == localStorage.getItem("card_id"))[0];
        console.log(creditCard)
        const type_card = creditCard._CreditCard__type_card;

        const visaImage = document.querySelector('.image img[src="PictureForNike/visa.png"]');
        const masterImage = document.querySelector('.image img[src="PictureForNike/master.png"]');
        const jcbImage = document.querySelector('.image img[src="PictureForNike/jcb.png"]');

        if (type_card === "JCB") {
            visaImage.style.display = 'none';
            masterImage.style.display = 'none';
            jcbImage.style.display = 'block';
            backImage.src = 'PictureForNike/jcb.png';
            selectedCardType = "JCB";
        } else if (type_card === "Master") {
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
        document.getElementById(type_card.toLowerCase()).checked = true;

        document.getElementById("card_name").value = creditCard._CreditCard__card_name;

        document.getElementById("number").value = creditCard._CreditCard__number;

        document.getElementById("pin").value = creditCard._CreditCard__pin;

        document.querySelector('.card-number-box').innerText = document.querySelector('.card-number-input').value;

        document.querySelector('.card-holder-name').innerText = document.querySelector('.card-holder-input').value;

        document.querySelector('.front').style.transform = 'perspective(1000px) rotateY(-180deg)';
        document.querySelector('.back').style.transform = 'perspective(1000px) rotateY(0deg)';

        document.querySelector('.front').style.transform = 'perspective(1000px) rotateY(0deg)';
        document.querySelector('.back').style.transform = 'perspective(1000px) rotateY(180deg)';

        document.querySelector('.cvv-box').innerText = document.querySelector('.cvv-input').value;



    })

});