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

    $("#edit_role").click(function() {
        $("#role_text").html('<b>Role: </b><input id="new_role" placeholder="' + player_role + '">')
        const save = $('<button id="save_role" type="button" class="btn btn-outline-primary edit_btn">Save</button>').bind(
            "click", function(){
                $.ajax({
                    type: "POST",
                    url: "update_role",                
                    dataType : "json",
                    contentType: "application/json; charset=utf-8",
                    data : JSON.stringify({
                        "new_role": $("#new_role").val(),
                        "id": id_num,
                    }),
                    success: function(result){
                        location.reload()
                    },
                    error: function(request, status, error){
                        console.log("Error");
                        console.log(request)
                        console.log(status)
                        console.log(error)
                    }
                  })
              }
        )
        const discard = $('<button id="discard_role" type="button" class="btn btn-outline-primary edit_btn">Discard</button>').bind(
            "click", function(){
                location.reload()
            }
        )
        $("#role_buttons").html('')
        $("#role_buttons").append(save)
        $("#role_buttons").append(discard)
    })

    $("#edit_age").click(function() {
        $("#age_text").html('<b>Agew: </b><input id="new_age" placeholder="' + player_age + '">')
        const save = $('<button id="save_age" type="button" class="btn btn-outline-primary edit_btn">Save</button>').bind(
            "click", function(){
                $.ajax({
                    type: "POST",
                    url: "update_age",                
                    dataType : "json",
                    contentType: "application/json; charset=utf-8",
                    data : JSON.stringify({
                        "new_age": $("#new_age").val(),
                        "id": id_num,
                    }),
                    success: function(result){
                        location.reload()
                    },
                    error: function(request, status, error){
                        console.log("Error");
                        console.log(request)
                        console.log(status)
                        console.log(error)
                    }
                  })
              }
        )
        const discard = $('<button id="discard_age" type="button" class="btn btn-outline-primary edit_btn">Discard</button>').bind(
            "click", function(){
                location.reload()
            }
        )
        $("#age_buttons").html('')
        $("#age_buttons").append(save)
        $("#age_buttons").append(discard)
    })

    $("#edit_teams").click(function() {
        $("#teams_text").html('<b>Agew: </b><input id="new_teams" placeholder="' + player_teams + '">')
        const save = $('<button id="save_teams" type="button" class="btn btn-outline-primary edit_btn">Save</button>').bind(
            "click", function(){
                $.ajax({
                    type: "POST",
                    url: "update_teams",                
                    dataType : "json",
                    contentType: "application/json; charset=utf-8",
                    data : JSON.stringify({
                        "new_teams": $("#new_teams").val(),
                        "id": id_num,
                    }),
                    success: function(result){
                        location.reload()
                    },
                    error: function(request, status, error){
                        console.log("Error");
                        console.log(request)
                        console.log(status)
                        console.log(error)
                    }
                  })
              }
        )
        const discard = $('<button id="discard_teams" type="button" class="btn btn-outline-primary edit_btn">Discard</button>').bind(
            "click", function(){
                location.reload()
            }
        )
        $("#teams_buttons").html('')
        $("#teams_buttons").append(save)
        $("#teams_buttons").append(discard)
    })
})



