const cardTypeInputs = document.querySelectorAll('input[name="type_card"]');
const backImage = document.querySelector('.back img[src="PictureForNike/visa.png"]');

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
    } else if (this.value === "Master") {
        visaImage.style.display = 'none';
        jcbImage.style.display = 'none';
        masterImage.style.display = 'block';
        backImage.src = 'PictureForNike/master.png';
    } else {
        masterImage.style.display = 'none';
        jcbImage.style.display = 'none';
        visaImage.style.display = 'block';
        backImage.src = 'PictureForNike/visa.png';
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


document.querySelector('.submit-btn').onclick = () => {
    if (!document.querySelector('input[name="type_card"]:checked')) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Password and confirm password do not match!',
        })
        return;
    }
};