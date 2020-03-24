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

    $("#submit_create").click(function(){
        if ($("#name").val().trim() == '' || $("#role").val().trim() == '' || $("#description").val().trim() == '' ||
        $("#age").val().trim() == '' || $("#team").val().trim() == '' || $("#image").val().trim() == '') {
            //Check each one - make backround light red if not filled in
            if ($("#name").val().trim() == '') {
                $("#name_section").css('background-color', 'pink')
                const warning = $('<p>Name field cannot be blank</p>')
                $("#name_section").append(warning)
            }
            if ($("#role").val().trim() == '') {
                $("#role_section").css('background-color', 'pink')
                const warning = $('<p>Role field cannot be blank</p>')
                $("#role_section").append(warning)
            }
            if ($("#description").val().trim() == '') {
                $("#description_section").css('background-color', 'pink')
                const warning = $('<p>Description field cannot be blank</p>')
                $("#description_section").append(warning)
            }
            if ($("#age").val().trim() == '') {
                $("#age_section").css('background-color', 'pink')
                const warning = $('<p>Age field cannot be blank</p>')
                $("#age_section").append(warning)
            }
            if ($("#team").val().trim() == '') {
                $("#team_section").css('background-color', 'pink')
                const warning = $('<p>Team field cannot be blank</p>')
                $("#team_section").append(warning)
            }
            if ($("#image").val().trim() == '') {
                $("#image_section").css('background-color', 'pink')
                const warning = $('<p>Image field cannot be blank</p>')
                $("#image_section").append(warning)
            }

        }
        else {
            new_player = {
                "player_name": $("#name").val(),
                "player_role": $("#role").val(),
                "player_description": $("#description").val(),
                "player_age": $("#age").val(),
                "player_teams": $("#team").val(),
                "player_image": $("#image").val(),
            }
            create_player(new_player)
        } 
      });
})

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