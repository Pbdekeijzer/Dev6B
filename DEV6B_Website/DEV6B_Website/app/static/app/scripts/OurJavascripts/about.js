$(document).ready(function() {

    var JobNumber;
    var CrimeSelected;
    var JobTitle;
    var JobTasks;
    testList = [];

    //sends GET request to view.py and returns json
    $.ajax({
        url: "jobs/",
        //data is CHIEL for testing. This should be the actual logged in username
        data: { "username": "CHIEL" }
    }).done(function (json) {
        json = JSON.stringify(json);
        $.each(JSON.parse(json), function (idx, obj) {
            testList.push(obj);
            
        });

        var index = 0;
        testList.forEach(function (element) {
            index = index + 1;
            $("#AllJobs").append("<div class='well'><p>Job " + element.jobname + "</p><p><a id='TheJobButton' href='#' class='btn btn-primary btn-large'>Select Job "+index+"</a></p></div>");

        });
    });


    $('#AllJobs').on('click', '.well', function () {
        //Get the title of job selected
        JobTitle = $(this).text();
        JobTitle = JobTitle.split("Select");
        JobTitle = JobTitle[0];
        //Get jobnumber selected
        JobNumber = $(this).find('#TheJobButton').text();
        JobNumber = JobNumber.split(" ");
        JobNumber = JobNumber[JobNumber.length - 1];

        JobTasks = testList[JobNumber-1].tasks.split(",");


        $('#MiddleBoxDown').empty();
        //Now it only give the number of the job you selected, but must become the title of the crime #NeedDatabaseFirst
        $('#MiddleBoxDown').append("<h3>Selected job " + JobNumber + "</h3> <form action=''> ");
        JobTasks.forEach(function(element) {
            $('#MiddleBoxDown').append("<input type='radio' name='Crime' value='" + element + "'> " + element + "<br> ");
        });
        $('#MiddleBoxDown').append("</form><br> <a href='#' id='CommitCrime' class='btn btn-primary btn-large'>Commit crime</a>" +
            "<div id='NotSelectedAlert'> You first must select which crime you want to commit </div>");
        $('#MiddleBoxDown').css('padding-bottom', '40px');
        $('#NotSelectedAlert').hide();


    });


    $('#MiddleBoxDown').on('click', '#CommitCrime', function () {
        CrimeSelected = $('input[name=Crime]:checked').val();
        if (CrimeSelected == null) {
            $('#NotSelectedAlert').show();
            $('#NotSelectedAlert').delay(3500).hide(1000);
        } else {
            if (Math.floor((Math.random() * 2) + 1) == 1) {
                $('#MiddleBoxAbove').empty();
                $('#MiddleBoxAbove').append("<h1>Meme Wars</h1> <p> <h3>Current game information</h3> " +
                    "</p> <p><h4>" +
                    JobTitle + ", " + CrimeSelected.toString() + " was succesfully finished, Good job!</h4> </p> <p><h4>You gained " + testList[JobNumber].expreward.toString() + "xp</h4> </p> ");
                    

            } else {
                $('#MiddleBoxAbove').empty();
                $('#MiddleBoxAbove').append("<h1>Meme Wars</h1> <p> <h3>Current game information</h3> " +
                    "</p> <p><h4>" +
                    JobTitle + ", " + CrimeSelected.toString() + " was failed, Terrible job!</h4> </p> <p><h4>You lost " + testList[JobNumber].expreward + "xp</h4> </p> ");


            }


        }
    });


});