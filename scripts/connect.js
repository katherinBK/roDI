
function connectRODI() {
    fetch('/conectar',{
        method: "POST",
        headers: {
            'content-Type':'application/json'
        },
        body: JSON.stringify({ip: document.getElementById('ip').value})
    }
    )
    .then(reponse => {
        if (response.ok) {
            alert("Conectado exiosamente!!");
        }
        else{
            alert("error al conectar");
        }
    });
}