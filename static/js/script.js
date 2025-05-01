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

function toggleDropdown() {
  var dropdown = document.getElementById("profileDropdown");
  var button = document.querySelector(".account-info-more");
  var isOpen = dropdown.style.display === "block";
  dropdown.style.display = isOpen ? "none" : "block";
  button.setAttribute("aria-expanded", !isOpen);
}

function toggleSidebar() {
  var sidebar = document.querySelector(".sidebar");
  var appContent = document.querySelector(".app-content");
  var toggleButton = document.getElementById("sidebarToggle");
  var isCollapsed = sidebar.classList.contains("collapsed");

  // Toggle the collapsed class
  sidebar.classList.toggle("collapsed");

  // Update aria-expanded attribute
  toggleButton.setAttribute("aria-expanded", isCollapsed ? "true" : "false");

  // Force layout recalculation to ensure content expands
  if (isCollapsed) {
    appContent.style.marginLeft = "250px";
  } else {
    appContent.style.marginLeft = "0";
  }
}

// Close dropdown when clicking outside
document.addEventListener("click", function (event) {
  var dropdown = document.getElementById("profileDropdown");
  var profileButton = document.querySelector(".account-info-more");
  if (!profileButton.contains(event.target) && !dropdown.contains(event.target)) {
    dropdown.style.display = "none";
    profileButton.setAttribute("aria-expanded", "false");
  }
});

// Attach event listeners
document.getElementById("sidebarToggle").addEventListener("click", toggleSidebar);
document.querySelector(".account-info-more").addEventListener("click", toggleDropdown);



//VACANCY SCRIPT

  function openDeleteModal(button) {
    var blogId = button.getAttribute("data-blog-id");
    var form = document.getElementById("deleteForm");
    form.action = `/delete_vacancy/${blogId}/`;  // Ensure this matches your URL pattern
    var modal = document.getElementById("deleteModal");
    
    modal.style.display = "block";
    setTimeout(() => modal.classList.add("show"), 10); // Delay to trigger animation
  }

  function closeDeleteModal() {
    var modal = document.getElementById("deleteModal");
    modal.classList.remove("show");
    setTimeout(() => (modal.style.display = "none"), 300); // Delay hiding until animation ends
  }

  // Close modal when clicking outside of it
  window.onclick = function(event) {
    var modal = document.getElementById("deleteModal");
    if (event.target === modal) {
      closeDeleteModal();
    }
  }
