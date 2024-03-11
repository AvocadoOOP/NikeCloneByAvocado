function img(anything) {
    document.querySelector('.slide').src = anything;
}

function change(change) {
    const line = document.querySelector('.home');
    line.style.background = change;
}


// Get the elements for minus and plus buttons
const minusBtns = document.querySelectorAll('.minus');
const plusBtns = document.querySelectorAll('.plus');
const amountLabels = document.querySelectorAll('.add label');

// Add event listeners for minus buttons
minusBtns.forEach((minusBtn, index) => {
    minusBtn.addEventListener('click', () => {
        // Get the current amount value
        let currentAmount = parseInt(amountLabels[index].textContent);
        // Ensure the amount doesn't go below 1
        if (currentAmount > 1) {
            currentAmount--;
            // Update the amount label
            amountLabels[index].textContent = currentAmount;
        }
    });
});

// Add event listeners for plus buttons
plusBtns.forEach((plusBtn, index) => {
    plusBtn.addEventListener('click', () => {
        // Get the current amount value
        let currentAmount = parseInt(amountLabels[index].textContent);
        // Increase the amount
        currentAmount++;
        // Update the amount label
        amountLabels[index].textContent = currentAmount;
    });
});

const openCart = document.getElementById('open_cart');
const cart = document.getElementById('sideCart');
const closeCart = document.getElementById('close_cart');

openCart.addEventListener('click', openSideCart);
closeCart.addEventListener('click', closeSideCart);

function openSideCart() {
    cart.classList.add('open');
}

function closeSideCart() {
    cart.classList.remove('open');
}

document.addEventListener("DOMContentLoaded", function () {

    axios.get("http://localhost:8000/product-detail/" + localStorage.getItem("product_id")).then((response) => { 

    const product = response.data;
    
    console.log (product);
    const imageUrl = product._Product__list_images[0]?.list_images[1] || '';
    const selectedColor = product._Product__list_images[0]?.name;
    

    console.log(selectedColor)


    const  mainImage = document.getElementsByClassName("slide")[0];
    const nameProduct = document.getElementById("name_product");
    const category = document.getElementById("category");
    const price = document.getElementById("price");
    const slide = document.getElementById("slider");

    

    mainImage.src = imageUrl;
    nameProduct.innerHTML = product._Product__product_name;
    category.innerHTML = product._Product__category;
    price.innerHTML = ` <small>฿ </small>${product._Product__price} `;

    slide.innerHTML = product._Product__list_images.filter(color => color.name === selectedColor)[0].list_images.map((item, index) => {
        if (item.split(".")[0][item.split(".")[0].length-1] < "1"){
            return
        }
        return `<img src="${item}" onclick="img('${item}')">`
        
    }).join("");


})


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

});