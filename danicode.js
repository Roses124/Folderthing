//variables
var map;
var ourloc;
var view;

function init() {
  ourloc = ol.proj.fromLonLat([-74.6329, 40.5695]);
  view = new ol.View({
    center: ourloc,
    zoom: 6
  });

  map = new ol.Map({
    target: "map",
    layers:[
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    loadTilesWhileAnimating: true,
    view: view
  });
}

function panHome() {
  view.animate({
    center: ourloc,
    duration: 2000
  });
}



function makeCountryRequest(){
  var countryName = document.getElementById("country-name").value;

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

function processCountryRequest(){
  if(countryRequest.readyState != 4){
    return;
  }
  if(countryRequest.status != 200 || countryRequest.responseText === ""){
    alert("We couldn't find your country!");
    return;
  }
  var countryInfo = JSON.parse(countryRequest.responseText);
  var lat = countryInfo[0].latlng[0];
  var lon = countryInfo[0].latlng[1];
  var location = ol.proj.fromLonLat([lon, lat]);

  view.animate({
    center: location,
    duration: 2000
  });
}
window.onload = init;
