$(document).ready(function() {

    var JobNumber;
    var CrimeSelected;

    for (var index = 1; index < 20; index++) {

        $("#AllJobs").append("<div class='well'><p>Job"+index+"</p><p><a href='#' class='btn btn-primary btn-large'>Select Job "+index+"</a></p></div>");

        
    }
    

    $('.well').click(function () {
        //Get jobnumber selected
        JobNumber = $(this).text();
        JobNumber = JobNumber.split(" ");
        JobNumber = JobNumber[JobNumber.length - 1];

        $('#MiddleBoxDown').empty();
        //Now it only give the number of the job you selected, but must become the title of the crime #NeedDatabaseFirst
        $('#MiddleBoxDown').append("<h3>Selected job "+JobNumber+"</h3> <form action=''> " +
            "<input type='radio' name='Crime' value='CrimeOne'> CrimeOne<br> " +
            "<input type='radio' name='Crime' value='CrimeTwo'> CrimeTwo<br> " +
            "<input type='radio' name='Crime' value='CrimeThree'> CrimeThree " +
            "</form><br> <a href='#' id='CommitCrime' class='btn btn-primary btn-large'>Commit crime</a>");



    });


    $('#MiddleBoxDown').on('click', 'CommitCrime', function () {
        CrimeSelected = $('input[name=Crime]:checked').val();


    });


});