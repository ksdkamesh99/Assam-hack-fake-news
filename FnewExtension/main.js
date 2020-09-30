search = function (word) {
  var query = word.selectionText;
  //query has your selected text
  //replace google with your api address
  fetch('http://www.google.com?q=' + query).then(r => r.text()).then(result => {
    alert(query); // result contains the api response
  })
};

chrome.contextMenus.create({
  title: "Search If Fake News",
  contexts: ["selection"],
search = function (word) {
  var query = word.selectionText;
  //query has your selected text
  //replace google with your api address
  fetch('http://www.google.com?q=' + query).then(r => r.text()).then(result => {
    alert(query); // result contains the api response
  })
};

chrome.contextMenus.create({
  title: "Search If Fake News",
  contexts: ["selection"],
  onclick: search
});
