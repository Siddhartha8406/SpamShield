// Read page data
chrome.runtime.sendMessage({ action: "getPageData" }, function(response) {
    const pageData = response.pageData;
    console.log(pageData);
});

document.getElementById("status").textContent = tabs[0].id;