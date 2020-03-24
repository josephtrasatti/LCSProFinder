$(document).ready(function(){

    display_players()

    $("#submit_button").click(function(){
        event.preventDefault()
        search = $("#search").val()
        window.location = '/search?player=' + search
    });

    $("#create_button").click(function(){
        event.preventDefault()
        window.location = '/create'
    })
})


var display_players = function() {
    for (var i = 0; i < players.length; i += 4) {

        player_row = players.slice(i, i+4)

        const new_row = $('<div class="row"></div>')

        for (var j = 0; j < player_row.length; j++) {
            const button = $('<button class="delete_player btn btn-secondary" id="' + player_row[j].id + '">X</button>').bind(
                "click", function() {
                    const id = $(this).attr('id')
                    $.ajax({
                        type: "POST",
                        url: "/mark_as_deleted",                
                        dataType : "json",
                        contentType: "application/json; charset=utf-8",
                        data : JSON.stringify(id),
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

            const card = $('<div class="card col-md-3"></div>')
            //card.append(button)
            const picture = $(`<img class="card-img-top" src="` + player_row[j].picture + `" alt="Player Headshot" onclick="location.href='/view/` + player_row[j].id + `'">`)
            card.append(picture)
            const content = $('<div class="card-body"></div>')
            var name = $('<h5 class="card-title">' + player_row[j].player + '</h5>')
            var role = $('<p class="card-text">' + player_row[j].role + '</p>')
            console.log(last_search)
            if (player_row[j].player.toLowerCase().indexOf(last_search) !== -1) {
                name = $('<h5 class="card-title"><b>' + player_row[j].player + '</b></h5>')
            }
            if (player_row[j].role.toLowerCase().indexOf(last_search) !== -1) {
                role = $('<p class="card-text"><b>' + player_row[j].role + '</b></p>')
            }
            content.append(name)
            content.append(role)
            card.append(content)
            new_row.append(card)
        }

        $("#display_players").append(new_row)
    }
}

var delete_player = function(id) {
    $.ajax({
        type: "POST",
        url: "delete_player",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : id,
        success: function(result){
            $(".search_results").html('')
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
      });
}



