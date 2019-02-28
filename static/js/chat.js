var socket = io.connect("http://" + document.domain + ":" + location.port)

socket.on("connect", function() {
    
    socket.emit("user-connect", {})

    $("#input-form").on("submit", function(e) {
        e.preventDefault()
        socket.emit("user-chat", {
            user_name : $("#username").val(),
            message : $("#message").val()
        } )
        $("#message").val("").focus()
    })

    socket.on("response", function(message) {
        $( "#message-div" ).append( "<div><b>" + message.user_name + "</b>" + message.message + "</div>" )
    })
})