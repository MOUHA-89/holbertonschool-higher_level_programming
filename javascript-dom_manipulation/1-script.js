// Select the element with id 'red_header'
const redHeaderButton = document.querySelector('#red_header');

// Add a click event listener to the selected element
redHeaderButton.addEventListener('click', () => {
  // Select the header element
  const header = document.querySelector('header');
  
  // Update the text color of the header to red (#FF0000)
  header.style.color = '#FF0000';
});
