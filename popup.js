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
            let user_mail = result[0].result;
        });
    });
    console.log(user_mail);
});

function DOMtoString(selector) {
    return document.getElementById(":1a1").textContent;

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