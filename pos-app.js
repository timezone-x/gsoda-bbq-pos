var withOnions = 0;
var withoutOnions = 0;
var drinks = 0;

function refreshCounters() {
  document.getElementById('with-onions-count').innerHTML = withOnions;
  document.getElementById('without-onions-count').innerHTML = withoutOnions;
  document.getElementById('drinks-count').innerHTML = drinks;
}

function incrCount() {
    withOnions++;
    refreshCounters();
    
}