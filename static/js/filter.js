document.addEventListener('DOMContentLoaded', function() {
    const filterLinks = document.querySelectorAll('.item-link');
    const projectImages = document.querySelectorAll('.project-img');

    filterLinks.forEach(link => {
        link.addEventListener('click', function() {
            const filterValue = this.getAttribute('data-filter');

            // Remove active class from all links
            filterLinks.forEach(item => item.classList.remove('menu-active'));
            // Add active class to the clicked link
            this.classList.add('menu-active');

            projectImages.forEach(image => {
                const imageType = image.getAttribute('data-type');
                if (filterValue === 'all' || imageType === filterValue) {
                    image.style.display = 'block'; // Show image
                } else {
                    image.style.display = 'none'; // Hide image
                }
            });
        });
    });
});