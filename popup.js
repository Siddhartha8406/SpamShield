notSpamMail();

// document.getElementById('status-div').style.display="none";

// document.getElementById("click-me-button").addEventListener('click', function() {
//     notSpamMail();
// });

// function spamMail(){
//     document.getElementById("button-div").style.display = "none";
//     document.getElementById("status-div").style.display = "flex";
//     document.getElementById("status").textContent = "SPAM";

//     document.body.style.backgroundColor = "#cc3300";
//     document.getElementById("heading").style.color = "#ffcc00";

// }

function notSpamMail(){
    document.getElementById("button-div").style.display = "none";
    document.getElementById("status-div").style.display = "flex";
    document.getElementById("status").textContent = "NOT SPAM";

    document.body.style.backgroundColor = "#99cc33";
    document.getElementById("status").style.color = "#40a6ce";

}