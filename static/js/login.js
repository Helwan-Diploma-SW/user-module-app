document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();  // Prevent the form from submitting the usual way

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch('/api/users/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => {
        if (response.status === 200) {
            // If login is successful (status 200), redirect manually
            window.location.href = '/dashboard';  // Redirect to the dashboard page
        } else if (response.status === 401) {
            // If login failed (status 401), show error message
            return response.json();  // Parse the error message
        }
    })
    .then(data => {
        if (data && data.error) {
            document.getElementById("error-message").textContent = data.error;  // Show the error message to the user
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred, please try again later.');
    });
});
