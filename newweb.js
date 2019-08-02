function catfact(){
  var catstuff = document.getElementById("").value;

  if(countryName ===""){
    alert("You didn't enter a country name!");
    return;
  }
  var query = "https://restcountries.eu/rest/v2/name/" + countryName;
  query  = query.replace(/ /g, "%20");

  countryRequest = new XMLHttpRequest();
  countryRequest.open('GET', query, true);
  countryRequest.onload = processCountryRequest;
  countryRequest.send();
}
