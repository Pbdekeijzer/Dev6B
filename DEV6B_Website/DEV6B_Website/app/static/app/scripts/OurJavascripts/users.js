$(document)
    .ready(function() {

        testList = [];

        //sends GET request to view.py and returns json
        $.ajax({
            url: "users/",
            //data is CHIEL for testing. This should be the actual logged in username
            //data: { "username": "CHIEL" }
        }).done(function (json) {
            json = JSON.stringify(json);
            $.each(JSON.parse(json), function (idx, obj) {
                testList.push(obj.username);
                console.log("userstest");
            });



            //Just for testing
            console.log("userstest");
            testList.forEach(function (element) {
                console.log(element);

            });
        });

    });