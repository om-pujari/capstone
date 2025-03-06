// Authentication related functions
const users = [
    {
        email: 'demo@example.com',
        password: 'password123',
        name: 'Demo User'
    }
];

// Handle login
function handleLogin(e) {
    e.preventDefault();
    
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('errorMessage');

    const user = users.find(u => u.email === email && u.password === password);

    if (user) {
        localStorage.setItem('isLoggedIn', 'true');
        localStorage.setItem('user', JSON.stringify({
            email: user.email,
            name: user.name
        }));
        window.location.href = '../index.html';
    } else {
        errorMessage.textContent = 'Invalid email or password';
        errorMessage.style.display = 'block';
    }
}

// Handle registration
function handleRegister(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('errorMessage');

    if (users.some(u => u.email === email)) {
        errorMessage.textContent = 'Email already exists';
        errorMessage.style.display = 'block';
        return;
    }

    users.push({
        email,
        password,
        name
    });

    localStorage.setItem('isLoggedIn', 'true');
    localStorage.setItem('user', JSON.stringify({
        email,
        name
    }));

    window.location.href = '../index.html';
}

// Check if user is logged in
function checkAuth() {
    const isLoggedIn = localStorage.getItem('isLoggedIn');
    if (!isLoggedIn) {
        window.location.href = '../login/login.html';
    }
}

// Initialize auth related elements
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');

    if (loginForm) {
        loginForm.addEventListener('submit', handleLogin);
    }

    if (registerForm) {
        registerForm.addEventListener('submit', handleRegister);
    }
});
