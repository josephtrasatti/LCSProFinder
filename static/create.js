$(document).ready(function(){
    $("#submit_button").click(function(){
        event.preventDefault()
        search = $("#search").val()
        window.location = '/?player=' + search
    });

    $("#create_button").click(function(){
        event.preventDefault()
        window.location = '/create'
    })

    $("#submit").click(function(){
        $("#warning").remove()
        if ($("#name").val() == '' || $("#role").val() == '' || $("#description").val() == '' ||
        $("#age").val() == '' || $("#team").val() == '' || $("#image").val() == '') {
            make_warning("all fields must have input")
        }
        else {
            new_player = {
                "player_name": $("#name").val(),
                "player_role": $("#role").val(),
                "player_description": $("#description").val(),
                "player_age": $("#age").val(),
                "player_teams": $("#teams").val(),
                "player_image": $("#image").val(),
            }
            create_player(new_player)
        } 
      });
})

function make_warning(blank) {
    const warning = $('<div id="warning">' + blank + '</div>')
    $(".submit_section").append(warning)
}

var create_player = function(new_player) {
    $.ajax({
        type: "POST",
        url: "create_player",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(new_player),
        success: function(result){
            window.location.replace("http://127.0.0.1:5000/view/" + result["old_id"])
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}