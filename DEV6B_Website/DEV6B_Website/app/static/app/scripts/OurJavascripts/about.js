$(document).ready(function() {

    var JobNumber;
    var CrimeSelected;



    for (var index = 1; index <= 20; index++) {

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
            "</form><br> <a href='#' id='CommitCrime' class='btn btn-primary btn-large'>Commit crime</a>" +
            "<div id='NotSelectedAlert'> You first must select which crime you want to commit </div>");
        $('#MiddleBoxDown').css('padding-bottom', '40px')
        $('#NotSelectedAlert').hide();


    });


    $('#MiddleBoxDown').on('click', '#CommitCrime', function () {
        CrimeSelected = $('input[name=Crime]:checked').val();
        if (CrimeSelected == null) {
            $('#NotSelectedAlert').show();
            $('#NotSelectedAlert').delay(3500).hide(1000);
        } else {
            $('#MiddleBoxAbove').empty();
            $('#MiddleBoxAbove').append("<h1>Meme Wars</h1> <p> <h3>Current game information</h3> " +
                "</p> <p><h4> Job "+ JobNumber.toString() +", "+ CrimeSelected.toString() +" was succesfully finished, Good job!</h4> </p> <p><h4>You gained 200xp</h4> </p> " +
                "<!--<img src='../../static/app/content/fear_m10.jpg' alt='meme.jpg'/>--> "); //Dont know what this comment was for in the html, decided to just copy paste it

        }
    });


});