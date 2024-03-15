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
            amount = currentAmount;
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
        amount = currentAmount
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

let selectedColor = ""
let selectedColorId = 1
let selectedSize = ""
let productShow = {}
let amount = 1;

let list_like = [];
document.addEventListener("DOMContentLoaded", function () {


    axios.get(`http://localhost:8000/favorite-list/${localStorage.getItem("user_id")}`).then((response) => {
      const data = response.data;

      list_like = data.map((product) => {
        return product._Product__product_id;
      });

      console.log(list_like)
  });




    axios.get("http://localhost:8000/product-detail/" + localStorage.getItem("product_id")).then((response) => {

        const product = response.data;

        console.log(product)

        // console.log(product);
        const imageUrl = product._Product__list_images[0]?.list_images[1] || '';
        selectedColor = product._Product__list_images[0]?.name;


        // console.log(selectedColor)


        const mainImage = document.getElementsByClassName("slide")[0];
        const nameProduct = document.getElementById("name_product");
        const category = document.getElementById("category");
        const price = document.getElementById("price");
        const slide = document.getElementById("slider");
        const list_colors = document.getElementById("list_colors");
        const list_size = document.getElementById("list_size");

        document.getElementById("like").checked = list_like.includes(Number(localStorage.getItem("product_id")));


        mainImage.src = imageUrl;
        nameProduct.innerHTML = product._Product__product_name;
        category.innerHTML = product._Product__category;
        price.innerHTML = ` <small>฿ </small>${product._Product__price} `;
        let i = 1;
        slide.innerHTML = product._Product__list_images.filter(color => color.name === selectedColor)[0].list_images.map((item, index) => {

            if (item.split(".")[0][item.split(".")[0].length - 1] === i.toString()) {
                i += 1;
                return `<img src="${item}" onclick="img('${item}')">`;
            }


        }).join("");

        list_colors.innerHTML = product._Product__list_images.map((color, index) => {
            if (index === 0) {
                return `<span onclick="handleSelectedColor('${color.name}')" style="background-color: ${color.name}" class="selected"></span>`
            }
            return `<span onclick="handleSelectedColor('${color.name}')" style="background-color: ${color.name}" ></span>`
        }).join("");

        list_size.innerHTML = product._Product__list_product_style.map((style, index) => {
            if (index === 0) {
                // selectedSize = style._ProductStyle__size
                selectedColorId = style._ProductStyle__product_style_id
            }

            if (style._ProductStyle__color === selectedColor) {

                if (style._ProductStyle__size === selectedSize) {
                    return `
                <button onclick="handleSelectedSize('${style._ProductStyle__size}')"  class="size-btn selected">${style._ProductStyle__size}</button>
                `
                }
                else {
                    return `
                <button onclick="handleSelectedSize('${style._ProductStyle__size}')"  class="size-btn">${style._ProductStyle__size}</button>
                `

                }
            }
            return
        }).join("");

        productShow = product;


    })


    Array.from(document.getElementsByClassName("men_product")).forEach((card) => {
        card.addEventListener("click", function () {
            localStorage.removeItem("search_input");
            localStorage.setItem("product", "Men")
            window.location.href = "/productList.html";
        });
    });

    Array.from(document.getElementsByClassName("women_product")).forEach((card) => {
        card.addEventListener("click", function () {
            localStorage.removeItem("search_input");
            localStorage.setItem("product", "Women")
            window.location.href = "/productList.html";
        });
    });

    Array.from(document.getElementsByClassName("kids_product")).forEach((card) => {
        card.addEventListener("click", function () {
            localStorage.removeItem("search_input");
            localStorage.setItem("product", "Kids")
            window.location.href = "/productList.html";
        });
    });

    Array.from(document.getElementsByClassName("all_product")).forEach((card) => {
        card.addEventListener("click", function () {
            localStorage.removeItem("search_input");
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

    document.getElementById("search_input").addEventListener("keypress" , function(e){
        if (e.key == "Enter"){
            localStorage.setItem("search_input" , this.value);
            window.location.href = "/productList.html";
        }
    });

    document.getElementById("addToCart").addEventListener("click", function () {


        if (localStorage.getItem("user_id") == null) {
            window.location.href = "/loginRegister.html";
        }
        else {
            if (!selectedSize || !selectedColor) {

                alert("Please select size and color")

                return
            }
            axios.post("http://localhost:8000/product-add-cart", {
                product_id: Number(localStorage.getItem("product_id")),
                customer_id: Number(localStorage.getItem("user_id")),
                amount: Number(amount),
                color_id: Number(selectedColorId),
                size: selectedSize
            }).then((response) => {
                console.log(response.data)
                alert("Add to cart success")
                getData();
            }).catch((error) => {
                console.log(error)
                alert("Add to cart fail")
            })

            
        }
    });

    document.getElementById("pay_button").addEventListener("click", function () {
        if (localStorage.getItem("user_id") == null) {
            window.location.href = "/loginRegister.html";
        }
        else {
            window.location.href = "/confirmOrder.html";
        }
    });

    // Assuming this is inside an async function

    

    getData();




});

const getData = async () => {
    try {
        const response = await axios.get(`http://localhost:8000/cart/${localStorage.getItem("user_id")}`);
        const cart = response.data;

        console.log(cart)
        document.getElementById("subtotal_price").innerHTML = cart._ShoppingCart__total_price;
        const cart_items = document.getElementById("cart_items");
        const item_number = document.getElementById("item_number");
        

        if (list_like.includes(Number(localStorage.getItem("product_id")))) {
                toggle_favorite.ariaChecked = true;
        }

        item_number.innerText = cart._ShoppingCart__amount
        const cartItemsHtml = await Promise.all(cart._ShoppingCart__list_product_cart.map(async (product, index) => {
            try {
                const response = await axios.get(`http://localhost:8000/product-detail/${product._SelectedProduct__id}`);
                const productDetail = response.data;
                // console.log(productDetail)
                // console.log(product)
                const list_colors = productDetail._Product__list_product_style.map((color, index) => {
                    if (color.name === product._ProductStyle__product_style_id) {
                        return color
                    }
                })
                // console.log(list_colors)
                const name_color = list_colors.filter( color => color._ProductStyle__product_style_id === product._SelectedProduct__color_id )[0]._ProductStyle__color
                // console.log(name_color)
                
                const imageUrl = productDetail._Product__list_images.filter(color => color.name === name_color)[0].list_images[0] || '';
                
                console.log(product)
                return `<div class="cart_item">
                <div onclick="deleteItem(${product._SelectedProduct__id},${product._SelectedProduct__color_id},'${product._SelectedProduct__size}')" class="remove_item">
                  <span>&times;</span>
                </div>
                
                <div class="item_img">
                  <img src=./${imageUrl}>
                </div>
                
                <div class="item_details">
                  <p>${productDetail._Product__product_name}</p>
                  <strong> <small>฿ </small> ${productDetail._Product__price}</strong>
                  <p style="font-size:13px;">Size : ${product._SelectedProduct__size}</p>
                  <p style="font-size:13px;">Amount : ${product._SelectedProduct__amount}</p>
                </div>
              </div>`
            } catch (error) {
                console.error("Error fetching product details:", error);
                return ''; // Return an empty string or some error placeholder
            }
        }));

        cart_items.innerHTML = cartItemsHtml.join("");
    } catch (error) {
        console.error("Error fetching cart:", error);
    }
};

const handleSelectedColor = (color) => {
    selectedColor = color;
    selectedSize = ""
    const list_colors = document.getElementById("list_colors");
    const list_size = document.getElementById("list_size");

    list_colors.innerHTML = productShow._Product__list_images.map((color, index) => {
        if (color.name === selectedColor) {
            return `<span onclick="handleSelectedColor('${color.name}')" style="background-color: ${color.name}" class="selected"></span>`
        }

        return `<span onclick="handleSelectedColor('${color.name}')" style="background-color: ${color.name}" ></span>`
    }).join("");

    list_size.innerHTML = productShow._Product__list_product_style.map((style, index) => {
        if (style._ProductStyle__color === selectedColor) {
            return `
            <button onclick="handleSelectedSize('${style._ProductStyle__size}')"  class="size-btn">${style._ProductStyle__size}</button>
            `
        }
        return
    }).join("");

    const slide = document.getElementById("slider");
    const mainImage = document.getElementsByClassName("slide")[0];


    let i = 1;
    slide.innerHTML = productShow._Product__list_images.filter(color => color.name === selectedColor)[0].list_images.map((item, index) => {
        if (index === 0) {
            mainImage.src = item;
        }
        if (item.split(".")[0][item.split(".")[0].length - 1] === i.toString()) {
            i += 1;
            return `<img src="${item}" onclick="img('${item}')">`;
        }


    }).join("");
}
const handleSelectedSize = (size) => {
    selectedSize = size
    const list_size = document.getElementById("list_size");

    list_size.innerHTML = productShow._Product__list_product_style.map((style, index) => {
        if (style._ProductStyle__color === selectedColor) {
            selectedColorId = style._ProductStyle__product_style_id
            if (style._ProductStyle__size === size) {
                return `
                <button onclick="handleSelectedSize('${style._ProductStyle__size}')"  class="size-btn selected">${style._ProductStyle__size}</button>
                `
            }
            else {
                return `
                <button onclick="handleSelectedSize('${style._ProductStyle__size}')"  class="size-btn">${style._ProductStyle__size}</button>
                `

            }
        }
        return
    }).join("");

}


const deleteItem = (product_id , color_id , size) => {
    console.log("delete" , product_id , color_id , size)

    axios.delete(`http://localhost:8000/product-delete-cart/${window.localStorage.getItem("user_id")}/${product_id}/${color_id}/${size}`).then((response) => {
        console.log(response.data)
        // alert("Delete item success")
        getData();
    }).catch((error) => {
        console.log(error)
        alert("Delete item fail")
    })
}

const toggle_favorite = (productId) => {
    axios.post(`http://localhost:8000/toggle-favorite/${localStorage.getItem("user_id")}/${productId}`).then((response) => {
      console.log(response.data);
  
  });
  }

document.getElementById("like").addEventListener("click", function () {
    if (localStorage.getItem("user_id") == null) {
        window.location.href = "/loginRegister.html";
    }
    else {
        toggle_favorite(localStorage.getItem("product_id"));
    }
});
        