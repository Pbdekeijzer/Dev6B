function loginToDatabase(name, password) {
    ajaxCall(/LoginURL/ + name)
    ajaxCall("/API/Products/" + id, "application/json", {}, function (json) {
        product = json;
        onComplete(json, entry);
    });
}

function login_post() {
    console.log("hello")
}