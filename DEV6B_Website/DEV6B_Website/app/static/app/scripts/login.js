$(document).ready(function() {

    //$('#submitButton')
    //    .click(function(e) {
    //        console.log("clicked");
    //        create_post();

    //    });

    $('#post-form').on('submit', function (event) {
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_post();
    });
   
    function create_post() {
        console.log("create post is working!") // sanity check

        var meme = { the_post: document.getElementById("dbusername").value };

        $.ajax({
            url: "register/", // the endpoint
            type: "POST", // http method
            data: meme, // data sent with the post request

            // handle a successful response
            success: function (json) {
                $('#post-text').val(''); // remove the value from the input
                console.log(meme); // log the returned json to the console
                console.log("success"); // another sanity check
            },

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
        //$.ajax({
        //    url: "register/", // the endpoint
        //    type: "POST", // http method
        //    data: { the_post: $('#post-text').val() }, // data sent with the post request

        //    // handle a successful response
        //    success: function (json) {
        //        $('#post-text').val(''); // remove the value from the input
        //        console.log(json); // log the returned json to the console
        //        console.log("success"); // another sanity check
        //    },

        //    // handle a non-successful response
        //    error: function (xhr, errmsg, err) {
        //        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
        //            " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
        //        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        //    }
        //});
   


    //function create_post() {
    //    console.log("create post is working!") // sanity check
    //    console.log($('#post-text').val())
    //};


    //$('#post-form').on('Submit', function (event) {
    //    event.preventDefault();
    //    console.log("form submitted!")  // sanity check
    //    create_post();
    //});
    $.ajaxSetup({ 
        beforeSend: function(xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        } 
    });

});
