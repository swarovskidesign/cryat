document.getElementById('logo-link').addEventListener('click', function(event) {
    event.preventDefault();

    fetch('vk.com', {
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
        console.log('Logo Page Data:', data);
        document.getElementById('content').innerHTML = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error loading logo page: ' + error.message);
    });
});