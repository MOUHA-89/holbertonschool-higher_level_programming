// Define the URL
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Use Fetch API to get the data from the URL
fetch(url)
  .then(response => {
    // Check if the response is successful (status code 200-299)
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    // Parse the JSON response
    return response.json();
  })
  .then(data => {
    // Extract the character name from the data
    const characterName = data.name;

    // Select the HTML tag with id "character"
    const characterElement = document.getElementById('character');

    // Set the text content of the HTML tag to the character name
    characterElement.textContent = characterName;
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('Error fetching character:', error);

    // Optionally, display an error message in the characterElement
    const characterElement = document.getElementById('character');
    characterElement.textContent = 'Error fetching character.';
  });
