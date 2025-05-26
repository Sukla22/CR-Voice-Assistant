$(document).ready(function () {
    //display speak  message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');
    } 

    //display hood
    eel.expose(ShowHood)
    function ShowHood(){
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }

    eel.expose(senderText)
    function senderText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() != "" ){
            chatbox.innerHTML += `<div class="row justify-content-end mb-4">
            <div class = "width-size">
            <div class = "sender_message>${message}</div>
        </div>`;
            // scroll to the bottom of the chatbox
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }
    eel.expose(receiverText)
    function receiverText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() != "" ){
            chatbox.innerHTML += `<div class="row justify-content-end mb-4">
            <div class = "width-size">
            <div class = "receiver_message>${message}</div>
        </div>`;
            // scroll to the bottom of the chatbox
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }
});