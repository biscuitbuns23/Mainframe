// kairos landing2 sidebar toggle
let sidebar = document.querySelector('.sidebar');
let menu = document.querySelector('#menu');

menu.addEventListener('click', () => {
    sidebar.classList.toggle('active')
})