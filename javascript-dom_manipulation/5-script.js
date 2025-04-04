// Select the element with id "update_header"
const updateHeader = document.getElementById('update_header');

// Add a click event listener to the element
updateHeader.addEventListener('click', function () {
    // Select the header element
    const header = document.querySelector('header');
    // Update the text content of the header element
    header.textContent = 'New Header!!!';
});
