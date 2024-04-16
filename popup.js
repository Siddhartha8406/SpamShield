document.getElementById('status-div').style.display="none";

document.getElementById("click-me-button").addEventListener('click', async function() {
    notSpamMail();
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        var activeTab = tabs[0];
        var activeTabId = activeTab.id;

        document.getElementById("status").textContent = tabs[0].id;
        chrome.scripting.executeScript({
            target: { tabId: activeTabId },
            function: DOMtoString,
        }).then((result) => {
            var user_mail = result[0].result;
            var recived_mail = String(user_mail)
            console.log(recived_mail);


            fetch('http://127.0.0.1:8000/predict/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email: recived_mail }),
            }).then(response => response.json()).then(response => console.log(JSON.stringify(response)))




            if (recived_mail.includes("Siddhartha Reddy")){
                notSpamMail();
            }
            else if(recived_mail.includes("null")){
                forNull();
            }
            else{
                spamMail();
            }
        });
    });
});

function DOMtoString(selector) {
    var temp_var = document.getElementsByClassName("a3s");
    return temp_var[0].textContent;
}

function spamMail(){
    document.getElementById("button-div").style.display = "none";
    document.getElementById("status-div").style.display = "flex";
    document.getElementById("status").textContent = "SPAM";

    document.body.style.backgroundColor = "#cc3300";
    document.getElementById("heading").style.color = "#ffcc00";

}

function notSpamMail(){
    document.getElementById("button-div").style.display = "none";
    document.getElementById("status-div").style.display = "flex";
    document.getElementById("status").textContent = "NOT SPAM";

    document.body.style.backgroundColor = "#99cc33";
    document.getElementById("status").style.color = "#40a6ce";
}

function forNull(){
    document.getElementById("button-div").style.display = "none";
    document.getElementById("status-div").style.display = "flex";
    document.getElementById("status").textContent = "Not a mail";

    document.body.style.backgroundColor = "#cc3300";
    document.getElementById("heading").style.color = "#ffcc00";

}