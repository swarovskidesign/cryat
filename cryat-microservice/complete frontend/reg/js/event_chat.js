document.getElementById('chat-link').addEventListener('click', function(event) {
    event.preventDefault();

    fetch('path_to_fedback', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Request failed with status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Chat Page Data:', data);
        document.getElementById('content').innerHTML = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error loading chat page: ' + error.message);
    });
});