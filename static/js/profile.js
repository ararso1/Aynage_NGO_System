document.getElementById('profileUpdateForm').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Profile updated successfully! ');
    window.location.href = 'profileview.html';
});

document.getElementById('cancelUpdateBtn').addEventListener('click', function() {
    window.location.href = 'profileview.html';
});