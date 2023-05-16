document.addEventListener('DOMContentLoaded', function() {

const themeBut = document.getElementById('themeBut');



themeBut.addEventListener('click', function() {
    const bodyElement = document.body;

    if (bodyElement.style.backgroundColor === 'rgb(0, 0, 0)') {
        bodyElement.style.backgroundColor = '#ffffff';
        bodyElement.style.color = '#000000';
    } else {
        bodyElement.style.backgroundColor = '#000000';
        bodyElement.style.color = '#ffffff';
    }
})});