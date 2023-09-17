document.addEventListener("DOMContentLoaded", function () {
    const emailField = document.getElementById("id_email"); // Corrected ID
    const passwordField = document.getElementById("id_password"); // Corrected ID
    const emailError = document.getElementById("email-error");
    const passwordError = document.getElementById("password-error");

    emailField.addEventListener("blur", function () {
        if (!emailField.value.trim()) {
            emailError.textContent = "Email is required";
        } else {
            emailError.textContent = ""; // Clear the error message
        }
    });

    passwordField.addEventListener("blur", function () {
        if (!passwordField.value.trim()) {
            passwordError.textContent = "Password is required";
        } else {
            passwordError.textContent = ""; // Clear the error message
        }
    });

    $(document).ready(function () {
        // Check if there's a server error message
        if (serverErrorMessage) {
            // Replace the error message in the HTML with the server error message
            $('#password-error').text(serverErrorMessage);
        }
    });
});
