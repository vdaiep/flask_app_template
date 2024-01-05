$(document).ready(function() {
    testMessageApp();
    $("#test_app_route").click(function() {
        testAppRoute();
    });
});

function testMessageApp(){
    console.log("This is executed each time route /app is loaded");
}

function testAppRoute() {
    var jsonData = {
        data_from_js: "data",
        username: username
    };
    $.post({
        url: "/test_app",
        data: JSON.stringify(jsonData),
        contentType: "application/json",
        success: function(response) {
            console.log("Success:", response);
        },
        error: function(xhr, status, error) {
            console.error("Error:", error);
        }
    });
}
