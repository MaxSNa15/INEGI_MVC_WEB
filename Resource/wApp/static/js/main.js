var form = document.querySelector("form");

form.addEventListener("submit", function (event) {
    var username = form.querySelector('input[name="username"]').value;
    var password = form.querySelector('input[name="password"]').value;

    if (username.trim() === "") {
        alert("Por favor, ingresa tu nombre de usuario.");
        event.preventDefault();
    }

    else if (password.trim() === "") {
        alert("Por favor, ingresa tu contraseña.");
        event.preventDefault();
    }

});