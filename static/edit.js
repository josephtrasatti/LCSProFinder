$(document).ready(function(){
    $("#discard").click(function(){
        window.location.replace("http://127.0.0.1:5000/view/" + id_num)
    })

    $("#submit").click(function(){
        if ($("#new_age").val() == '') {
            make_warning("new data cannot be blank")
        }
        else {
            update = {
                "new_age": $("#new_age").val(),
                "id_num": id_num
            }
            update_age(update)
        }
    })
})

function make_warning(blank) {
    const warning = $('<div id="warning">' + blank + '</div>')
    $(".submit_section").append(warning)
}

var update_age = function() {
    $.ajax({
        type: "POST",
        url: "update_age",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(update),
        success: function(result){
            window.location.replace("http://127.0.0.1:5000/view/" + result["id_num"])
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}