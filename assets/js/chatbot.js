function sendMessage() {
    var userMessage = $("#user-input").val();
    if (userMessage.trim() === "") return;
    
    $("#chat-box").append('<div class="user-message">' + userMessage + '</div>');
    $("#user-input").val("");
    
    $.ajax({
        type: "POST",
        contentType: "application/json",
        url: "/chatbot_response",
        data: JSON.stringify({ "message": userMessage }),
        dataType: "json",
        success: function(response) {
            var botMessage = response.response;
            $("#chat-box").append('<div class="bot-message">' + botMessage + '</div>');
        },
        error: function(err) {
            console.error("Error:", err);
        }
    });
}
