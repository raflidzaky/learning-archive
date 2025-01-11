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

// Since Javascript needs a runtime environment to run on client-side for any HTTP requests 
// To make HTTP requests from local server to client-side, I need runtime called Node.js
// But, I could also just copy my Javascript on Chrome console, since it provides runtime
// However, we have to copy and paste back-and-forth whenever we wants different requests
// It is a best practice to do it on Node.js
// Node.js is not only for HTTP requests, but also running outside the browser.
// To trigger and automate, use Makefile all the way through
