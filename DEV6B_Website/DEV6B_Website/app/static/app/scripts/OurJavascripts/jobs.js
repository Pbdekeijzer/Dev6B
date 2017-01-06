$(document)
    .ready(function () {

        var testList = [];

        //sends GET request to view.py and returns json
        $.ajax({
            url: "jobs/",
            //data is CHIEL for testing. This should be the actual logged in username
            data: {"username" : "CHIEL"}
        }).done(function (json) {
            json = JSON.stringify(json);
            $.each(JSON.parse(json), function (idx, obj) {
                testList.push(obj.expreward);
                console.log("All jobs below");
            }); 
            


            //Just for testing
            
            testList.forEach(function (element) {
                console.log(element);
            console.log("These were all the jobs");
            });
        });

    });