var withOnions = 0;
var withoutOnions = 0;
var drinks = 0;
let apiAddress = "127.0.0.1:5000"

function fetchPrices() {
  var pricesAPI = apiAddress + "/pricing-fetch"

}

function refreshCounters() {
  document.getElementById('with-onions-count').innerHTML = withOnions;
  document.getElementById('without-onions-count').innerHTML = withoutOnions;
  document.getElementById('drinks-count').innerHTML = drinks;
}

function incrCount() {
  withOnions += 1;
  refreshCounters();

}