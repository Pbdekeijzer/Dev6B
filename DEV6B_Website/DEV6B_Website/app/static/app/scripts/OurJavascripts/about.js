$(document).ready(function() {


    for (var index = 1; index < 20; index++) {

        $("#AllJobs").append("<div class='well'><p>Job"+index+"</p><p><a href='#' class='btn btn-primary btn-large'>Select Job "+index+"</a></p></div>");

        
    }
    

    $('.well').click(function () {
        //Get jobnumber selected
        var JobNumber = $(this).text();
        JobNumber = JobNumber.split(" ");
        JobNumber = JobNumber[JobNumber.length - 1];

        $('#MiddleBoxDown').empty();
        //Now it only give the number of the job you selected, but must become the title of the crime #NeedDatabaseFirst
        $('#MiddleBoxDown').append("<h3>Selected job "+JobNumber+"</h3><p>Zoveel kans</p><p>Zoveel kans</p><p>Zoveel kans</p>");


        //if (id == "m1") {
        //    do your stuff here
        //}


    });




});