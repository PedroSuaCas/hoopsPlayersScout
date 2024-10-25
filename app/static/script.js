async function sendMessage() {
    const input = document.getElementById("userInput").value;
    const responseDiv = document.getElementById("response");

    const response = await fetch("/consulta_jugador/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ nombre_jugador: input }),
    });

    const data = await response.json();
    responseDiv.innerText = data.respuesta || "Error al obtener la respuesta.";
    document.getElementById("userInput").value = "";  // Limpiar la caja de texto
}∫