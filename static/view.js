$(document).ready(function(){
    $("#submit_button").click(function(){
        event.preventDefault()
        search = $("#search").val()
        window.location = '/search?player=' + search
    });

    $("#create_button").click(function(){
        event.preventDefault()
        window.location = '/create'
    })

    populate_teams()

    $("#edit_role").click(function() {
        const role_input = $('<input id="new_role" placeholder="' + player_role + '">')
        role_input.on("keyup", function(event) {
            console.log('test')
            if (event.keyCode == 13) {
                update_role()
              }
        })
        $("#role_text").html('<b>Role: </b>')
        $("#role_text").append(role_input)
        $("#new_role").focus()
        const save = $('<button id="save_role" type="button" class="btn btn-outline-primary edit_btn">Save</button>').bind(
            "click", function() {
                update_role()
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
        const age_input = $('<input id="new_age" placeholder="' + player_age + '">')
        age_input.on("keyup", function(event) {
            console.log('test')
            if (event.keyCode == 13) {
                update_age()
              }
        })
        $("#age_text").html('<b>Agew: </b>')
        $("#age_text").append(age_input)
        $("#new_age").focus()
        const save = $('<button id="save_age" type="button" class="btn btn-outline-primary edit_btn">Save</button>').bind(
            "click", function(){
                update_age()
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
})

var update_teams = function() {
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

var update_age = function() {
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

var update_role = function(){
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

    function populate_teams() {
        var missing = false
        for (var i = 0; i < player_teams.length; i++) {
            if (!player_teams[i].deleted) {
                const team = $("<div class='col-md-2 info_box' id='" + player_teams[i].team + "'>" + player_teams[i].team + "</div>")
                const delete_button = $("<button class='btn btn-secondary delete_team' id='delete_" + i + "'>X</button>").bind(
                    "click", function() {
                        $.ajax({
                            type: "POST",
                            url: "/mark_as_deleted",                
                            dataType : "json",
                            contentType: "application/json; charset=utf-8",
                            data : JSON.stringify({
                                "team_index": $(this).attr("id").substr(7),
                                "id": id_num,
                            }),
                            success: function(result){
                                $("#" + result["team"]).remove()
                                const undo = $("<button id='undo' class='btn btn-secondary undo'>Undo</button>").bind
                                    (
                                        "click", function() {
                                            $.ajax({
                                                type: "POST",
                                                url: "/undo_mark_as_deleted",                
                                                dataType : "json",
                                                contentType: "application/json; charset=utf-8",
                                                data : JSON.stringify({
                                                    "team": result["team"],
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
                                $("#undo").remove()
                                $("#team_section").append(undo)
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
                team.append(delete_button)
                $("#team_section").append(team)
            }
            // else {
            //     missing = true
            // }
      }
    //   if (missing) {
    //         const undo = $("<button class='btn btn-secondary undo'>Undo</button>").bind(
    //             "click", function() {
    //                 $.ajax({
    //                     type: "POST",
    //                     url: "/undo_mark_as_deleted",                
    //                     dataType : "json",
    //                     contentType: "application/json; charset=utf-8",
    //                     data : JSON.stringify({
    //                         "team_index": $(this).attr("id").substr(7),
    //                         "id": id_num,
    //                     }),
    //                     success: function(result){
    //                         location.reload()
    //                     },
    //                     error: function(request, status, error){
    //                         console.log("Error");
    //                         console.log(request)
    //                         console.log(status)
    //                         console.log(error)
    //                     }
    //                 })
    //             }
    //       )
          
    //   }
  }


