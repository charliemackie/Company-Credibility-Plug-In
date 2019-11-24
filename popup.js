let verifySafety = document.getElementById('verifySafety');
  chrome.storage.sync.get('color', function(data) {
    verifySafety.setAttribute('value', data.color);
});

verifySafety.onclick = function(element) {
  let db = new sqlite3.Database('./Transactions.db', sqlite3.OPEN_READWRITE, (err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Connected to the transactions database.');
  });

  let color = element.target.value;
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.tabs.executeScript(
        tabs[0].id,
        {code: 'document.body.style.backgroundColor = "' + color + '";'});
  });
};