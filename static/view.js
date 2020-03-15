$(document).ready(function(){
    $("#submit_button").click(function(){
        event.preventDefault()
        search = $("#search").val()
        window.location = '/?player=' + search
      });

    $("#edit").click(function() {
        // TOOD 
    })

})



