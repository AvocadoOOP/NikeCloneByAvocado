document.addEventListener("DOMContentLoaded", function () {
  if (localStorage.getItem("product") != null) {

    let list_like = [];

    axios.get(`http://localhost:8000/favorite-list/${localStorage.getItem("user_id")}`).then((response) => {
      const data = response.data;

      list_like = data.map((product) => {
        return product._Product__product_id;
      });

      console.log(list_like)
  });



    const productType = localStorage.getItem("product");
    const searchInput = localStorage.getItem("search_input");
    const favorite = localStorage.getItem("like_product_list");
    if (searchInput) {
      axios.get("http://localhost:8000/product/all").then((response) => {

        const filteredData = response.data.filter(product => product._Product__product_name.toLowerCase().includes(searchInput.toLowerCase()));

        const result = filteredData.map((product) => {

          let imageUrl = '';


          try {
            imageUrl = product._Product__list_images[0]?.list_images[0] || '';
          } catch (error) {
            console.log(error)
          }


          const card = `
            <div class="product_card">
              <div class="shoes_image">
                <img src="${imageUrl}">
                <h2>${product._Product__product_name}</h2>
              </div>

              <div class="buttons">
                <div onclick="buyProduct(${product._Product__product_id})" class="buy_button">
                  <div class="buy_button-wrapper">
                    <div  class="text">Buy</div>
                      <span class="icon">
                        <svg viewBox="0 0 16 16" class="bi bi-cart2" fill="currentColor" height="16" width="16" xmlns="http://www.w3.org/2000/svg">
                    <path d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5zM3.14 5l1.25 5h8.22l1.25-5H3.14zM5 13a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0zm9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"></path>
                  </svg>
                      </span>
                    </div>
                  </div>

                  <div class="favorite_button">
                    <input class="like" onclick="toggle_favorite(${product._Product__product_id})" type="checkbox" title="like" ${list_like.filter(id => id === product._Product__product_id).length > 0 ? "checked" : ""} >
                    <div class="checkmark">
                      <svg xmlns="http://www.w3.org/2000/svg" class="outline" viewBox="0 0 24 24">
                        <path d="M17.5,1.917a6.4,6.4,0,0,0-5.5,3.3,6.4,6.4,0,0,0-5.5-3.3A6.8,6.8,0,0,0,0,8.967c0,4.547,4.786,9.513,8.8,12.88a4.974,4.974,0,0,0,6.4,0C19.214,18.48,24,13.514,24,8.967A6.8,6.8,0,0,0,17.5,1.917Zm-3.585,18.4a2.973,2.973,0,0,1-3.83,0C4.947,16.006,2,11.87,2,8.967a4.8,4.8,0,0,1,4.5-5.05A4.8,4.8,0,0,1,11,8.967a1,1,0,0,0,2,0,4.8,4.8,0,0,1,4.5-5.05A4.8,4.8,0,0,1,22,8.967C22,11.87,19.053,16.006,13.915,20.313Z"></path>
                      </svg>
                      <svg xmlns="http://www.w3.org/2000/svg" class="filled" viewBox="0 0 24 24">
                        <path d="M17.5,1.917a6.4,6.4,0,0,0-5.5,3.3,6.4,6.4,0,0,0-5.5-3.3A6.8,6.8,0,0,0,0,8.967c0,4.547,4.786,9.513,8.8,12.88a4.974,4.974,0,0,0,6.4,0C19.214,18.48,24,13.514,24,8.967A6.8,6.8,0,0,0,17.5,1.917Z"></path>
                      </svg>
                      <svg xmlns="http://www.w3.org/2000/svg" height="100" width="100" class="celebrate">
                        <polygon class="poly" points="10,10 20,20"></polygon>
                        <polygon class="poly" points="10,50 20,50"></polygon>
                        <polygon class="poly" points="20,80 30,70"></polygon>
                        <polygon class="poly" points="90,10 80,20"></polygon>
                        <polygon class="poly" points="90,50 80,50"></polygon>
                        <polygon class="poly" points="80,80 70,70"></polygon>
                      </svg>
                    </div>
                  </div>
              </div>
            
            </div>`;
          document.getElementById("product-list").innerHTML += card;

          return product;
        });

        console.log(result);
      });

      localStorage.removeItem("search_input");
    }
    else if (favorite) {
      axios.get("http://localhost:8000/product/all").then((response) => {

      const filteredData = response.data.filter(product => list_like.filter(id => id === product._Product__product_id).length > 0);

      const result = filteredData.map((product) => {

        let imageUrl = '';


        try {
          imageUrl = product._Product__list_images[0]?.list_images[0] || '';
        } catch (error) {
          console.log(error)
        }


        const card = `
          <div class="product_card">
            <div class="shoes_image">
              <img src="${imageUrl}">
              <h2>${product._Product__product_name}</h2>
            </div>

            <div class="buttons">
              <div onclick="buyProduct(${product._Product__product_id})" class="buy_button">
                <div class="buy_button-wrapper">
                  <div  class="text">Buy</div>
                    <span class="icon">
                      <svg viewBox="0 0 16 16" class="bi bi-cart2" fill="currentColor" height="16" width="16" xmlns="http://www.w3.org/2000/svg">
                  <path d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5zM3.14 5l1.25 5h8.22l1.25-5H3.14zM5 13a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0zm9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"></path>
                </svg>
                    </span>
                  </div>
                </div>

                <div class="favorite_button">
                  <input class="like" onclick="toggle_favorite(${product._Product__product_id})" type="checkbox" title="like" ${list_like.filter(id => id === product._Product__product_id).length > 0 ? "checked" : ""} >
                  <div class="checkmark">
                    <svg xmlns="http://www.w3.org/2000/svg" class="outline" viewBox="0 0 24 24">
                      <path d="M17.5,1.917a6.4,6.4,0,0,0-5.5,3.3,6.4,6.4,0,0,0-5.5-3.3A6.8,6.8,0,0,0,0,8.967c0,4.547,4.786,9.513,8.8,12.88a4.974,4.974,0,0,0,6.4,0C19.214,18.48,24,13.514,24,8.967A6.8,6.8,0,0,0,17.5,1.917Zm-3.585,18.4a2.973,2.973,0,0,1-3.83,0C4.947,16.006,2,11.87,2,8.967a4.8,4.8,0,0,1,4.5-5.05A4.8,4.8,0,0,1,11,8.967a1,1,0,0,0,2,0,4.8,4.8,0,0,1,4.5-5.05A4.8,4.8,0,0,1,22,8.967C22,11.87,19.053,16.006,13.915,20.313Z"></path>
                    </svg>
                    <svg xmlns="http://www.w3.org/2000/svg" class="filled" viewBox="0 0 24 24">
                      <path d="M17.5,1.917a6.4,6.4,0,0,0-5.5,3.3,6.4,6.4,0,0,0-5.5-3.3A6.8,6.8,0,0,0,0,8.967c0,4.547,4.786,9.513,8.8,12.88a4.974,4.974,0,0,0,6.4,0C19.214,18.48,24,13.514,24,8.967A6.8,6.8,0,0,0,17.5,1.917Z"></path>
                    </svg>
                    <svg xmlns="http://www.w3.org/2000/svg" height="100" width="100" class="celebrate">
                      <polygon class="poly" points="10,10 20,20"></polygon>
                      <polygon class="poly" points="10,50 20,50"></polygon>
                      <polygon class="poly" points="20,80 30,70"></polygon>
                      <polygon class="poly" points="90,10 80,20"></polygon>
                      <polygon class="poly" points="90,50 80,50"></polygon>
                      <polygon class="poly" points="80,80 70,70"></polygon>
                    </svg>
                  </div>
                </div>
            </div>
          
          </div>`;
        document.getElementById("product-list").innerHTML += card;

        return product;
      });

      console.log(result);
    });


    localStorage.removeItem("like_product_list");

    }
    else {
      if (productType === "all") {
        axios.get("http://localhost:8000/product/all").then((response) => {
  
  
  
  
          const result = response.data.map((product) => {
  
            let imageUrl = '';
  
  
            try {
              imageUrl = product._Product__list_images[0]?.list_images[0] || '';
            } catch (error) {
              console.log(error)
            }
  
  
            const card = `
              <div class="product_card">
                <div class="shoes_image">
                  <img src="${imageUrl}">
                  <h2>${product._Product__product_name}</h2>
                </div>
  
                <div class="buttons">
                  <div onclick="buyProduct(${product._Product__product_id})" class="buy_button">
                    <div class="buy_button-wrapper">
                      <div  class="text">Buy</div>
                        <span class="icon">
                          <svg viewBox="0 0 16 16" class="bi bi-cart2" fill="currentColor" height="16" width="16" xmlns="http://www.w3.org/2000/svg">
                      <path d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5zM3.14 5l1.25 5h8.22l1.25-5H3.14zM5 13a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0zm9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"></path>
                    </svg>
                        </span>
                      </div>
                    </div>
  
                    <div class="favorite_button">
                      <input ${list_like.filter(id => id === product._Product__product_id).length > 0 ? "checked" : ""} class="like" onclick="toggle_favorite(${product._Product__product_id})" type="checkbox" title="like">
                      <div class="checkmark">
                        <svg xmlns="http://www.w3.org/2000/svg" class="outline" viewBox="0 0 24 24">
                          <path d="M17.5,1.917a6.4,6.4,0,0,0-5.5,3.3,6.4,6.4,0,0,0-5.5-3.3A6.8,6.8,0,0,0,0,8.967c0,4.547,4.786,9.513,8.8,12.88a4.974,4.974,0,0,0,6.4,0C19.214,18.48,24,13.514,24,8.967A6.8,6.8,0,0,0,17.5,1.917Zm-3.585,18.4a2.973,2.973,0,0,1-3.83,0C4.947,16.006,2,11.87,2,8.967a4.8,4.8,0,0,1,4.5-5.05A4.8,4.8,0,0,1,11,8.967a1,1,0,0,0,2,0,4.8,4.8,0,0,1,4.5-5.05A4.8,4.8,0,0,1,22,8.967C22,11.87,19.053,16.006,13.915,20.313Z"></path>
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" class="filled" viewBox="0 0 24 24">
                          <path d="M17.5,1.917a6.4,6.4,0,0,0-5.5,3.3,6.4,6.4,0,0,0-5.5-3.3A6.8,6.8,0,0,0,0,8.967c0,4.547,4.786,9.513,8.8,12.88a4.974,4.974,0,0,0,6.4,0C19.214,18.48,24,13.514,24,8.967A6.8,6.8,0,0,0,17.5,1.917Z"></path>
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" height="100" width="100" class="celebrate">
                          <polygon class="poly" points="10,10 20,20"></polygon>
                          <polygon class="poly" points="10,50 20,50"></polygon>
                          <polygon class="poly" points="20,80 30,70"></polygon>
                          <polygon class="poly" points="90,10 80,20"></polygon>
                          <polygon class="poly" points="90,50 80,50"></polygon>
                          <polygon class="poly" points="80,80 70,70"></polygon>
                        </svg>
                      </div>
                    </div>
                </div>
              
              </div>`;
            document.getElementById("product-list").innerHTML += card;
  
            return product;
          });
  
          console.log(result);
        });
      }
      else {
  
        axios.get("http://localhost:8000/product/all").then((response) => {
          // console.log(response.data);
  
          let imageUrl = '';
  
          const result =  response.data.filter(product => product._Product__category === productType).map((product) => {
            try {
              imageUrl = product._Product__list_images[0]?.list_images[0] || '';
            } catch (error) {
              console.log(error)
            }
  
  
            const card = `
              <div class="product_card">
                <div class="shoes_image">
                <img src="${imageUrl}">
                  <h2>${product._Product__product_name}</h2>
                </div>
  
                <div class="buttons">
                  <div onclick="buyProduct(${product._Product__product_id})" class="buy_button">
                    <div class="buy_button-wrapper">
                      <div  class="text">Buy</div>
                        <span  class="icon">
                          <svg viewBox="0 0 16 16" class="bi bi-cart2" fill="currentColor" height="16" width="16" xmlns="http://www.w3.org/2000/svg">
                      <path d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5zM3.14 5l1.25 5h8.22l1.25-5H3.14zM5 13a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0zm9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"></path>
                    </svg>
                        </span>
                      </div>
                    </div>
  
                    <div class="favorite_button">
                      <input ${list_like.filter(id => id === product._Product__product_id).length > 0 ? "checked" : ""} class="like" onclick="toggle_favorite(${product._Product__product_id})" type="checkbox" title="like">
                      <div class="checkmark">
                        <svg xmlns="http://www.w3.org/2000/svg" class="outline" viewBox="0 0 24 24">
                          <path d="M17.5,1.917a6.4,6.4,0,0,0-5.5,3.3,6.4,6.4,0,0,0-5.5-3.3A6.8,6.8,0,0,0,0,8.967c0,4.547,4.786,9.513,8.8,12.88a4.974,4.974,0,0,0,6.4,0C19.214,18.48,24,13.514,24,8.967A6.8,6.8,0,0,0,17.5,1.917Zm-3.585,18.4a2.973,2.973,0,0,1-3.83,0C4.947,16.006,2,11.87,2,8.967a4.8,4.8,0,0,1,4.5-5.05A4.8,4.8,0,0,1,11,8.967a1,1,0,0,0,2,0,4.8,4.8,0,0,1,4.5-5.05A4.8,4.8,0,0,1,22,8.967C22,11.87,19.053,16.006,13.915,20.313Z"></path>
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" class="filled" viewBox="0 0 24 24">
                          <path d="M17.5,1.917a6.4,6.4,0,0,0-5.5,3.3,6.4,6.4,0,0,0-5.5-3.3A6.8,6.8,0,0,0,0,8.967c0,4.547,4.786,9.513,8.8,12.88a4.974,4.974,0,0,0,6.4,0C19.214,18.48,24,13.514,24,8.967A6.8,6.8,0,0,0,17.5,1.917Z"></path>
                        </svg>
                        <svg xmlns="http://www.w3.org/2000/svg" height="100" width="100" class="celebrate">
                          <polygon class="poly" points="10,10 20,20"></polygon>
                          <polygon class="poly" points="10,50 20,50"></polygon>
                          <polygon class="poly" points="20,80 30,70"></polygon>
                          <polygon class="poly" points="90,10 80,20"></polygon>
                          <polygon class="poly" points="90,50 80,50"></polygon>
                          <polygon class="poly" points="80,80 70,70"></polygon>
                        </svg>
                      </div>
                    </div>
                </div>
              
              </div>`;
            document.getElementById("product-list").innerHTML += card;
            return product;
          });
  
  
          console.log(result);  
        });
  
  
      }
      
    }


  }

  
  document.getElementById("search_input").addEventListener("keypress" , function(e){
    if (e.key == "Enter"){
        localStorage.setItem("search_input" , this.value);
        window.location.href = "/productList.html";
    }
});


  document.getElementById("user").addEventListener("click", function () {
    if (localStorage.getItem("user_id") == null) {
      window.location.href = "/loginRegister.html";
    } else {
      window.location.href = "/viewProfile.html";
    }
  });

  Array.from(document.getElementsByClassName("men_product")).forEach((card) => {
    card.addEventListener("click", function () {
      localStorage.removeItem("search_input");
      localStorage.setItem("product", "Men");
      window.location.href = "/productList.html";
    });
  });

  Array.from(document.getElementsByClassName("women_product")).forEach(
    (card) => {
      card.addEventListener("click", function () {
        localStorage.removeItem("search_input");
        localStorage.setItem("product", "Women");
        window.location.href = "/productList.html";
      });
    }
  );

  Array.from(document.getElementsByClassName("kids_product")).forEach(
    (card) => {
      card.addEventListener("click", function () {
        localStorage.removeItem("search_input");
        localStorage.setItem("product", "Kids");
        window.location.href = "/productList.html";
      });
    }
  );

  Array.from(document.getElementsByClassName("all_product")).forEach((card) => {
    card.addEventListener("click", function () {
      localStorage.removeItem("search_input");
      localStorage.setItem("product", "all");
      window.location.href = "/productList.html";
    });
  });

  

});


const buyProduct = (productId) => {
  if (localStorage.getItem("user_id") == null) {
    window.location.href = "/loginRegister.html";
  }
  else {
    localStorage.setItem("product_id", productId);
    window.location.href = "/productPage.html";
  }
}

const toggle_favorite = (productId) => {
  axios.post(`http://localhost:8000/toggle-favorite/${localStorage.getItem("user_id")}/${productId}`).then((response) => {
    console.log(response.data);

});
}