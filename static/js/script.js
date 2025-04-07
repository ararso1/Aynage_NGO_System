document.querySelector(".jsFilter").addEventListener("click", function () {
  document.querySelector(".filter-menu").classList.toggle("active");
});

document.querySelector(".grid").addEventListener("click", function () {
  document.querySelector(".list").classList.remove("active");
  document.querySelector(".grid").classList.add("active");
  document.querySelector(".products-area-wrapper").classList.add("gridView");
  document
    .querySelector(".products-area-wrapper")
    .classList.remove("tableView");
});

document.querySelector(".list").addEventListener("click", function () {
  document.querySelector(".list").classList.add("active");
  document.querySelector(".grid").classList.remove("active");
  document.querySelector(".products-area-wrapper").classList.remove("gridView");
  document.querySelector(".products-area-wrapper").classList.add("tableView");
});

var modeSwitch = document.querySelector('.mode-switch');
modeSwitch.addEventListener('click', function () {                      
  document.documentElement.classList.toggle('light');
 modeSwitch.classList.toggle('active');
});


document.addEventListener('DOMContentLoaded', function() {
  const toggleButton = document.getElementById('sidebarToggle');
  const sidebar = document.querySelector('.sidebar'); // Target the sidebar class
  
  // Toggle sidebar when button is clicked
  if (toggleButton && sidebar) {
      toggleButton.addEventListener('click', function() {
          sidebar.classList.toggle('collapsed');
          
          // Save state to localStorage
          localStorage.setItem('sidebarCollapsed', sidebar.classList.contains('collapsed'));
      });
      
      // Restore sidebar state on page load
      const isCollapsed = localStorage.getItem('sidebarCollapsed') === 'true';
      if (isCollapsed) {
          sidebar.classList.add('collapsed');
      }
  }
});