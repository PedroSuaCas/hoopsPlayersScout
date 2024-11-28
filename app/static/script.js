async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput) return;

    const chatBox = document.getElementById('chat-box');
    const userMessage = document.createElement('div');
    userMessage.className = 'message user-message';
    userMessage.textContent = userInput;
    chatBox.appendChild(userMessage);

    const response = await fetch('/api/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: userInput })
    });
    const result = await response.json();

    const assistantMessage = document.createElement('div');
    assistantMessage.className = 'message assistant-message';
    assistantMessage.textContent = result.gpt_response;
    chatBox.appendChild(assistantMessage);

    if (result.stats) {
        const statsMessage = document.createElement('div');
        statsMessage.className = 'message assistant-message';
        statsMessage.textContent = `Estadísticas:\nPuntos: ${result.stats.points}\nRebotes: ${result.stats.rebounds}\nAsistencias: ${result.stats.assists}`;
        chatBox.appendChild(statsMessage);
    }

    chatBox.scrollTop = chatBox.scrollHeight;
    document.getElementById('user-input').value = '';
}
