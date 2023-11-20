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


document.addEventListener('DOMContentLoaded', (event) => {
    var form = document.querySelector('.Forms-reb');

    form.addEventListener('submit', function(event) {
        var formIsValid = true;
        var name = document.getElementById('name').value;

        if (name.trim() === '') {
            alert('Por favor, ingresa tu nombre.');
            formIsValid = false; // El formulario no es válido
        }

        var municipality = document.getElementById('municipality').value;

        if (municipality.trim() === '') {
            alert('Por favor, selecciona un municipio.');
            formIsValid = false; // El formulario no es válido
        }

        if (!formIsValid) {
            event.preventDefault();
        }
    });
});
