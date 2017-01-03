$(document).ready(function() {


    for (var index = 1; index < 20; index++) {

        $("#AllJobs").append("<div class='well'><p>Job"+index+"</p><p><a href='#' class='btn btn-primary btn-large'>Select Job "+index+"</a></p></div>");

        
    }





    $('.well').click(function () {
        var id = $(this).attr('id');
        if (id == "m1") {
            //do your stuff here
        }



    });




});