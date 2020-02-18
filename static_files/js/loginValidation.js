function validateUserCred() {
    var x = document.forms["loginForm"]["username"].value;
    var y = document.forms["loginForm"]["password"].value;
    if (x != "admin" && y != "admin@123"){
        alert("Please enter right login details!!");
        return false;
    }
}