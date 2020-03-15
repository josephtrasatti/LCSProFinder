$(document).ready(function(){

    $("#search").keyup(function(e){
        if (e.keyCode == 13) {
            //window.location.href = 'http://127.0.0.1:5000/search_list?q=Tralinky'
            check_search()
        }
    });

    $("#submit_button").click(function(){
        window.location.href = 'http://127.0.0.1:5000/search_list?q=Tralinky'
        check_search()
      });

})

function make_warning(blank) {
    const warning = $('<div id="warning">' + blank + '</div>')
    $(".input_section").append(warning)
}

function check_search(){
    $("#warning").remove()
  
    if ($.trim($("#search").val()) == '') {
      make_warning("Client text feild cannot be blank")
      $("#search").focus()
    }
    else {
      var search = $("#search").val()
      $("#search").val("")
      $("#search").focus()
      make_search({"search": search})
    }
}

var make_search = function(search) {
    console.log("test")
    window.location.href = 'http://127.0.0.1:5000/search_list?q=Tralinky'
    // $.ajax({
    //     type: "POST",
    //     url: "search",
    //     dataType : "json",
    //     contentType: "application/json; charset=utf-8",
    //     data : JSON.stringify(search),
    //     success: function(result){
    //         var player_info = result["player_info"]
    //         if (player_info == "not found") {
    //             make_warning("no results found")
    //         }
    //         else {
    //             var player_id = player_info["id"]
    //             var player_name = player_info["player"]
    //             var player_description = player_info["description"]
    //             var player_age = player_info["age"]
    //             var player_teams = player_info["teams"]
    //             display_player(player_id, player_name, player_description, player_age, player_teams)
    //         }
    //     },
    //     error: function(request, status, error){
    //         console.log("Error");
    //         console.log(request)
    //         console.log(status)
    //         console.log(error)
    //     }
    //   });
}

var display_player = function(player_id, player_name, player_description, player_age, player_teams) {
    const player_div = $('<div class="player_display"></div>')
    const a_ref = $('<a href=http://127.0.0.1:5000/view/' + player_id + '>' + player_name + '</a>')
    const delete_button = $('<button class="delete_player" id="delete_' + player_id + '">x</button>')
    delete_button.bind("click", function(){
        var id = $(this).attr("id")
        var num = id.substr(id.indexOf('_')+1)
        delete_player(num)
      })
    player_div.append(a_ref)
    player_div.append(delete_button)
    $(".search_results").html('')
    $(".search_results").append(player_div)
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



