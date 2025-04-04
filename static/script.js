document.getElementById('predict-btn').addEventListener('click', function(event) {
    event.stopPropagation(); // Prevents immediate hiding

    let fighter1 = document.getElementById('fighter1').value.trim();
    let fighter2 = document.getElementById('fighter2').value.trim();

    if (fighter1 === "" || fighter2 === "") {
        alert("Please enter both fighter names correctly.");
        return;
    }

    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ fighter_1: fighter1, fighter_2: fighter2 })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            let popup = document.getElementById('popup');
            document.getElementById('prediction-result').innerText = data.predicted_winner + " is predicted to win!";
            popup.classList.remove('hidden');
            popup.style.display = "flex";  // Use flex to display the popup in full-screen mode
        }
    })
    .catch(error => console.error('Error:', error));
});

// Close popup when clicking anywhere on the screen
document.addEventListener('click', function() {
    let popup = document.getElementById('popup');
    popup.style.display = "none";  // Hide the popup
    popup.classList.add('hidden'); // Optionally re-add hidden class
});
