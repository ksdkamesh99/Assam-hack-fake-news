console.log('background running');

chrome.runtime.onMessage.addListener(receiver);

window.word = 'Fewz';

functiconsole.log('background running');

chrome.runtime.onMessage.addListener(receiver);

window.word = 'Fewz';

function receiver(request, sender, sendResponse) {
    console.log(request);
    window.word = request.text;
    fetch('http://detect-f-news.herokuapp.com/checkjs?query='+request.text).then((response) => {
        return response.json();
      }).then((myJson) => {
      try{
          chrome.runtime.sendMessage("oloaomebnahhjkdfgeogemdijnhhmlag",myJson.prediction);
          console.log(myJson.prediction);
          chrome.runtime.sendMessage("oloaomebnahhjkdfgeogemdijnhhmlag",myJson.citations);
          console.log(myJson.citations);
          alert("This news is " + myJson.prediction +"\n"+ myJson.citations);
          chrome.tabs.sendMessage(tab.id,myJson.prediction);
	}
	catch(err)
	{
		console.log("empty");
	}

      });
    
}

chrome.runtime.onMessage.addListener(urlRecv);
function urlRecv(request, sender, sendResponse) {
    console.log(request);
    window.word = request.text;
    fetch('http://127.0.0.1:5000//checkvalidation?query='+request.text).then((response) => {
        return response.json();
      }).then((myJson) => {
      try{
          chrome.runtime.sendMessage("oloaomebnahhjkdfgeogemdijnhhmlag",myJson.validation);
          console.log(myJson.validation);
          chrome.tabs.sendMessage(tab.id,myJson.validation);
          }
         catch
         {
         console.log("empty");
         }
      });
    
}
