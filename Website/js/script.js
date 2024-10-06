$(document).ready(function() {
    $('#chatbot-header').click(function() {
        $('#chatbot-body').slideToggle();
    });

    function sendMessage() {
        var userInput = $('#chatbot-input').val();
        $('#chatbot-input').val('');
        $('#chatbot-messages').append('<div class="user-message">' + userInput + '</div>');
        
        getBotResponse(userInput).then(function(response) {
            $('#chatbot-messages').append('<div class="bot-message">' + response + '</div>');
            $('#chatbot-messages').scrollTop($('#chatbot-messages')[0].scrollHeight);
        });
    }

    $('#chatbot-submit').click(function() {
        sendMessage();
    });

    $('#chatbot-input').keypress(function(e) {
        if (e.which == 13) { // Enter key pressed
            sendMessage();
        }
    });

    async function getBotResponse(input) {
        const response = await fetch('http://127.0.0.1:5000/generate-response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt: input })
        });
        const data = await response.json();
        return data.response;
    }
    
   
});
