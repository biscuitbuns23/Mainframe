// kairos landing2 sidebar toggle
let sidebar = document.querySelector('.sidebar');
let menu = document.querySelector('#menu');
let mainArea = document.querySelector('.js-main-area')

const sidebarToggle = () => sidebar.classList.toggle('active')

const sidebarToggleOff = () => sidebar.classList.contains('active') ? sidebarToggle() : null

menu.addEventListener('click', () => sidebarToggle())

mainArea.addEventListener('click', () => sidebarToggleOff())
mainArea.addEventListener('scroll', () => sidebarToggleOff())

// mainArea.addEventListener('click', (e) => {
//     if (e.target.closest('.sidebar.active')) return; // Ignore clicks inside active sidebar
//     sidebarToggle(); // Close sidebar if clicked outside
// });