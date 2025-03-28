$(document).ready(function() {
    $('#chat-toggle').click(function() {
        $('#chat-content').slideToggle('fast');
    });

    $('#user-input').on('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });

    $('#send-btn').click(sendMessage);
    $('#user-input').keypress(function(e) {
        if (e.which === 13 && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    function sendMessage() {
        const userInput = $('#user-input').val().trim();
        if (userInput) {
            // Agregar mensaje del usuario
            addMessage(userInput, 'user-message');
            $('#user-input').val('');
            $('#user-input').css('height', 'auto');
            
            // Mostrar "Escribiendo..." mientras se espera la respuesta
            const typingIndicator = addMessage('Yummies está escribiendo...', 'bot-message typing');
            
            // Enviar mensaje al servidor
            $.ajax({
                url: '/',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({ message: userInput }),
                success: function(response) {
                    // Eliminar "Escribiendo..." y mostrar la respuesta real
                    $('.typing').remove();
                    addMessage(response.response, 'bot-message');
                    scrollToBottom();
                },
                error: function() {
                    $('.typing').remove();
                    addMessage('Lo siento, hubo un error al procesar tu mensaje.', 'bot-message error');
                    scrollToBottom();
                }
            });
            
            scrollToBottom();
        }
    }

    function addMessage(text, messageClass) {
        const messageHtml = `
            <div class="message ${messageClass}">
                <p>${text.replace(/\n/g, '<br>')}</p>
            </div>
        `;
        $('#chat-messages').append(messageHtml);
        return $('#chat-messages .message').last();
    }

    function scrollToBottom() {
        $('#chat-messages').scrollTop($('#chat-messages')[0].scrollHeight);
    }
});