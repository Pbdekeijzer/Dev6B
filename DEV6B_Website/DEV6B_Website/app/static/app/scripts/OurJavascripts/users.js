$(document)
    .ready(function() {

        testList = [];
        var username = "CHIEL";
        //var user_id;
        //var level;
        //var experience;


        //sends GET request to view.py and returns json
        $.ajax({
            url: "users/",
            //data is CHIEL for testing. This should be the actual logged in username
            //data: { "username": "CHIEL" }
        }).done(function (json) {
            json = JSON.stringify(json);
            $.each(JSON.parse(json), function (idx, obj) {
                testList.push(obj);
                console.log("userstest1111");
            });

            //console.log(element["username"]);
            //console.log(element.findByName{ 'username': "CHIEL" });

            testList.forEach(function (element) {
                console.log(element);
                console.log(element.username);
                if (element.username === username) {
                    $('#AllUsers').empty();
                    $("#AllUsers").append("<p><h3 id='username'>Username: " + element.username + "<br/> </h3></p><p><div id='user_id'>User id: " + element.username + "</div></p><p><div id='lvl'>Level: " + element.cash + "</div></p><p><div id='exp'>Experience: " + element.experience + "</div></p>");
                }
            });

        });

    });