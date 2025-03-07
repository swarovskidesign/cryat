document.getElementById('registration-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const nickname = document.getElementById('nickname').value;
    const favoriteWord = document.getElementById('favorite_word').value;
    const password = document.getElementById('password').value;
    const repeatPassword = document.getElementById('repeat_password').value;

    if (password !== repeatPassword) {
        alert('Passwords do not match!');
        return;
    }

    const data = {
        nickname: nickname,
        favorite_word: favoriteWord,
        password: password,
    };

    fetch('path_to_reg_service', {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json', 
            'Accept': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Registration failed with status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        alert('Registration successful!');
    })
    .catch(error => {
        console.error('Error:', error.message);
        alert(error.message);
    });
});