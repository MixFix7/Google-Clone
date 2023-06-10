var username = document.getElementById("id_username");
var email = document.getElementById("id_email");

var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
console.log(csrfToken)

function ajax(type) {
    var value = type.value;

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "usernames/", safe=false);
    xhr.onreadystatechange = function() {
        if (xhr.status >= 200 && xhr.status <= 400) {
            var responce = JSON.parse(xhr.responseText);
            console.log(responce);
        } else {
            console.error(xhr.statusText)
        }
    
        xhr.onerror = function() {
            console.error("Error response")
        };

    };
    xhr.send();
};

// username.addEventListener('input', ajax(username));


username.addEventListener('input', function() {
    var inputValue = username.value;

    // Створити новий об'єкт XMLHttpRequest
    var xhr = new XMLHttpRequest();

    // Визначити обробник події завершення запиту
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          // Обробити відповідь сервера
          console.log(xhr.responseText);
        } else {
          // Обробити помилку
          console.log('Помилка: ' + xhr.status);
        }
      }
    };

    // Відправити AJAX-запит на Django-сервер
    xhr.open('POST', 'usernames/');
    xhr.setRequestHeader("X-CSRFToken", csrfToken);
    xhr.send(JSON.stringify({ input: inputValue }));
  });
// email.addEventListener('change', ajax(email));


