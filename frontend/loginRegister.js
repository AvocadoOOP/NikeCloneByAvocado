document.getElementById('register-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
    
    // Get form data
    var formData = {
        username: document.getElementById('register_username').value,
        email: document.getElementById('register_email').value,
        password: document.getElementById('register_password').value,
        confirm_password: document.getElementById('register_confirm_password').value
    };

    // Check if password and confirm_password match
    if (formData.password !== formData.confirm_password) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Password and confirm password do not match!',
        })
        return; // Stop further execution
    }

    
    // Send form data as JSON using Axios
    axios.post('http://127.0.0.1:8000/register/', formData)
    .then(response => {
        console.log(response.data);
        container.classList.remove("register-mode");
        

    })
    .catch(error => {
        console.error('There was an error!', error);
    });
});

document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
    
    // Get form data
    var formData = {
        email: document.getElementById('login_email').value,
        password: document.getElementById('login_password').value
    };

    // Send form data as JSON using Axios
    axios.post('http://127.0.0.1:8000/login/', formData)
    .then(response => {
        console.log(response.data);
        localStorage.setItem("user_id",response.data); 
        window.location.href = "/index.html";
        // Handle response data
    })
    .catch(error => {
        console.error('There was an error!', error);
    });
});

// const login_btn = document.querySelector("#login-btn");
// const register_btn = document.querySelector("#register-btn");
// const container = document.querySelector(".container");
// const login_btn2 = document.querySelector("#login-btn2");
// const register_btn2 = document.querySelector("#register-btn2");

// register_btn.addEventListener("click", () => {
//     container.classList.add("register-mode");
// });
// login_btn.addEventListener("click", () => {
//     container.classList.remove("register-mode");
// });
// register_btn2.addEventListener("click", () => {
//     container.classList.add("register-mode2");
// });
// login_btn2.addEventListener("click", () => {
//     container.classList.remove("register-mode2");
// });



const login_btn = document.querySelector("#login-btn");
const register_btn = document.querySelector("#register-btn");
const container = document.querySelector(".container");
const login_btn2 = document.querySelector("#login-btn2");
const register_btn2 = document.querySelector("#register-btn2");


// เพิ่ม event listener เข้าไปในฟังก์ชัน register และ login
register_btn.addEventListener("click", () => {
    container.classList.add("register-mode");
});
login_btn.addEventListener("click", () => {
    container.classList.remove("register-mode");
});
register_btn2.addEventListener("click", () => {
    container.classList.add("register-mode2");
});
login_btn2.addEventListener("click", () => {
    container.classList.remove("register-mode2");
});
