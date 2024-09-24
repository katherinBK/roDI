document.addEventListener('keydown', function(event) {
    let action;
    let keyPressed = '';

    if (event.key === "ArrowUp") {
        action = 'forward';
        keyPressed = 'Arriba';
    } else if (event.key === "ArrowDown") {
        action = 'backward';
        keyPressed = 'Abajo';
    } else if (event.key === "ArrowLeft") {
        action = 'left';
        keyPressed = 'Izquierda';
    } else if (event.key === "ArrowRight") {
        action = 'right';
        keyPressed = 'Derecha';
    }

    if (action) {
        sendCommand(action);
        document.getElementById('key-pressed').innerText = keyPressed;
    }
});

document.addEventListener('keyup', function(event) {
    sendCommand('stop');
    document.getElementById('key-pressed').innerText = 'Ninguno';
});

function sendCommand(action) {
    fetch('/control/' + action, { method: 'POST' })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
}

