// Authentication related JavaScript
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const registerBox = document.getElementById('registerBox');
    const showRegister = document.getElementById('showRegister');
    const showLogin = document.getElementById('showLogin');

    // Toggle between login and register forms
    showRegister.addEventListener('click', (e) => {
        e.preventDefault();
        document.querySelector('.auth-box').style.display = 'none';
        registerBox.style.display = 'block';
    });

    showLogin.addEventListener('click', (e) => {
        e.preventDefault();
        document.querySelector('.auth-box').style.display = 'block';
        registerBox.style.display = 'none';
    });

    // Handle login form submission
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        try {
            // TODO: Connect to backend login API
            // const response = await fetch('/api/auth/login', {
            //     method: 'POST',
            //     headers: { 'Content-Type': 'application/json' },
            //     body: JSON.stringify({ email, password })
            // });
            
            // if (response.ok) {
            //     const data = await response.json();
            //     // Store token in localStorage
            //     localStorage.setItem('token', data.token);
            //     // Redirect based on user role
            //     window.location.href = data.isAdmin ? '/admin.html' : '/dashboard.html';
            // }

            // Temporary: Simulate successful login
            if (email === 'admin@motoworld.com' && password === 'admin') {
                window.location.href = '/admin.html';
            } else {
                window.location.href = '/dashboard.html';
            }
        } catch (error) {
            console.error('Login failed:', error);
        }
    });

    // Handle registration form submission
    registerForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const name = document.getElementById('regName').value;
        const email = document.getElementById('regEmail').value;
        const password = document.getElementById('regPassword').value;
        const confirmPassword = document.getElementById('confirmPassword').value;

        if (password !== confirmPassword) {
            alert('Passwords do not match!');
            return;
        }

        try {
            // TODO: Connect to backend registration API
            // const response = await fetch('/api/auth/register', {
            //     method: 'POST',
            //     headers: { 'Content-Type': 'application/json' },
            //     body: JSON.stringify({ name, email, password })
            // });
            
            // if (response.ok) {
            //     // Show success message and switch to login form
            //     alert('Registration successful! Please login.');
            //     showLogin.click();
            // }

            // Temporary: Show success message
            alert('Registration successful! Please login.');
            showLogin.click();
        } catch (error) {
            console.error('Registration failed:', error);
        }
    });
});