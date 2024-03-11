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

