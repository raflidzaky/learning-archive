// Fetch local host --> feature
// Request POST
// Send the response of the request
// Dedicated for POST method
fetch('http://[LOCALHOST-ROUTE]/feature', {
    method: 'POST', // Specify the method as POST
    headers: {
        'Content-Type': 'application/json', // Set the Content-Type to JSON
    },
    body: JSON.stringify({
        "X": 5 // Replace this with the value you want to send
    }),
})
.then(response => response.json())  // Parse the response as JSON
.then(data => console.log(data))     // Log the response to the console
.catch(error => console.error('Error:', error));  // Handle any errors
