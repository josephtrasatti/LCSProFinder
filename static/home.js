$(document).ready(function(){

    display_players()

    $("#submit_button").click(function(){
        event.preventDefault()
        search = $("#search").val()
        window.location = '/?player=' + search
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

        new_row.html(player_row.map(player => (
            `
            <div class="card col-md-3" onclick="location.href='/view/${player.id}'">
                <img class="card-img-top" src="${player.picture}" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">${player.player}</h5>
                    <p class="card-text">${player.role}</p>
                </div>
            </div>
            `
        )).join(''))

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



