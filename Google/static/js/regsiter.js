let username = document.getElementById("id_username");
let email = document.getElementById("id_email");


username.addEventListener('change', ajax(username));
email.addEventListener('change', ajax(email));


function ajax(type) {
    let value = type.value;

    let xhr = new XMLHttpRequest();
    xhr.open("GET", "${type}s/", safe=false);
    xhr.onreadystatechange = function() {
        if (xhr.status >= 200 && xht.status <= 400) {
            var responce = xhr.responseText;
            console.log(responce);
        }
    };
    xhr.send();
};
