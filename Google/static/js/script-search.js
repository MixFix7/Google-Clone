document.addEventListener('DOMContentLoaded', function() {
const base = document.getElementById('base')
const ser = document.getElementById('ser')
const img = document.getElementById('img')
const vid = document.getElementById('vid')



base.addEventListener('input', function() {
    ser.value = base.value;
    img.value = base.value;
    vid.value = base.value;
})})