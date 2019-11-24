let verifySafety = document.getElementById('verifySafety');
  chrome.storage.sync.get('color', function(data) {
    verifySafety.setAttribute('value', data.color);
});

verifySafety.onclick = function(element) {
  let color = element.target.value;
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.tabs.executeScript(
        tabs[0].id,
        {code: 'document.body.style.backgroundColor = "' + color + '";'});
  });
};