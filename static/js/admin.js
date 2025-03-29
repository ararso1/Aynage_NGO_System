const menuIcon = document.getElementById("menuIcon");
const sidebar = document.getElementById("sidebar");
const mainContent = document.querySelector(".main-content");
const header = document.querySelector(".main-content .header");

menuIcon.addEventListener("click", () => {
  sidebar.classList.toggle("hidden");
  
  if (sidebar.classList.contains("hidden")) {
    mainContent.style.marginLeft = "0"; 
    header.style.left = "0"; 
  } else {
    mainContent.style.marginLeft = "250px"; 
    header.style.left = "250px";
  }
});

document.getElementById("fullscreenToggle").addEventListener("click", () => {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen();
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }
});

document.getElementById("darkModeToggle").addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
});

//vacancy
document.getElementById("vacancyLink").addEventListener("click", function(event) {
    event.preventDefault();

    fetch("vacancy.html")
      .then(response => {
        if (response.ok) {
          return response.text(); 
        } else {
          throw new Error("Failed to load the page.");
        }
      })
      .then(htmlContent => {
        document.getElementById("vacancyContent").innerHTML = htmlContent;
      })
      .catch(error => {
        console.error("Error loading vacancy page:", error);
      });
  });




  //blog
  document.getElementById("blogsLink").addEventListener("click", function(event) {
    event.preventDefault();

    fetch("blogs.html")
      .then(response => {
        if (response.ok) {
          return response.text(); 
        } else {
          throw new Error("Failed to load the page.");
        }
      })
      .then(htmlContent => {
        document.getElementById("vacancyContent").innerHTML = htmlContent;
      })
      .catch(error => {
        console.error("Error loading vacancy page:", error);
      });
  });

 
document.getElementById("analyticsLink").addEventListener("click", function(event) {
  event.preventDefault();

  fetch("analytics.html")
    .then(response => {
      if (response.ok) {
        return response.text(); 
      } else {
        throw new Error("Failed to load the analytics page.");
      }
    })
    .then(htmlContent => {
      document.getElementById("vacancyContent").innerHTML = htmlContent;  
    })
    .catch(error => {
      console.error("Error loading the analytics page:", error);
    });
});


function countUp(element, start, end, duration) {
  let range = end - start;
  let current = start;
  let increment = range / (duration / 50); // Divide by number of steps (50 ms interval)

  function step() {
      current += increment;
      if (current >= end) {
          element.innerText = end;
      } else {
          element.innerText = Math.round(current);
          requestAnimationFrame(step); // Keep updating until we reach the target
      }
  }

  step(); // Start the animation
}

window.onload = function() {
  // Call countUp for each statistic when the page loads
  countUp(document.getElementById('totalBlogs'), 0, 120, 2000); // 2 seconds for blogs
  countUp(document.getElementById('totalVacancies'), 0, 45, 2000); // 2 seconds for vacancies
  countUp(document.getElementById('totalUsers'), 0, 500, 2000); }