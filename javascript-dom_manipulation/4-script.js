document.getElementById('add_item').addEventListener('click', function() {
    // Create the new <li> element
    var newItem = document.createElement('li');
    newItem.textContent = 'Item';

    // Get the <ul> element with class 'my_list'
    var list = document.querySelector('.my_list');

    // Append the new <li> element to the list
    list.appendChild(newItem);
});
