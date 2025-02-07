function sendMessage() {
    let inputField = document.getElementById("user-input");
    let message = inputField.value.trim();

    if (message === "") return;

    let chatBox = document.getElementById("chat-box");
    
    // Display user's message
    let userMessage = `<div class="message user-message"><strong>You:</strong> ${message}</div>`;
    chatBox.innerHTML += userMessage;

    // Send message to Flask server
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        // Display bot's response
        let botMessage = `<div class="message bot-message"><strong>Bot:</strong> ${data.response}</div>`;
        chatBox.innerHTML += botMessage;
        
        // Auto-scroll to the latest message
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        console.error("Fetch error:", error);
        let errorMessage = `<div class="message bot-message"><strong>Bot:</strong> Error: ${error.message}</div>`;
        chatBox.innerHTML += errorMessage;
    });

    // Clear input field
    inputField.value = "";
    
}

// Listen for Enter key press to send message
document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {  // Check if Enter key is pressed
        event.preventDefault();  // Prevent default form submission
        sendMessage();  // Call sendMessage function
    }
});

