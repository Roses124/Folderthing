
var myKey = "5519769f5a993a98f1b4d51afdbbaa4d";

function getZipRequest(){
  var zip = document.getElementById("zip").value;
  request = new XMLHttpRequest();
  request.open('GET', "https://api.openweathermap.org/data/2.5/weather?zip=" + zip + "&appid=" + myKey, true);

  request.send();
  alert(request.status);
  var weather = request.responseText;
  var weatherInfo = JSON.parse(request.responseText);

  var description = weatherInfo[1].description;
  var temp = weatherInfo[3].temp;
  var tempNum = parseInt(temp);
  var tempC = (tempNum - 273);
  var tempF = (tempC * 9/5) + 32;

alert(tempF);
}
