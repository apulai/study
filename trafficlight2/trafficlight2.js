// script.js
// when user 'clicks' on the div id 'red', evoke the function makeRed()
function makeRed() {
  if( document.getElementById(event.target.id).className != "bulb") return;
  clearLight();
  document.getElementById(event.target.id).style.backgroundColor = "red";
}

function makeYellow() {
  if( document.getElementById(event.target.id).className != "bulb") return;
  clearLight();
  document.getElementById(event.target.id).style.backgroundColor = "yellow";
}

function makeGreen() {
  if( document.getElementById(event.target.id).className != "bulb") return;
  clearLight();
  document.getElementById(event.target.id).style.backgroundColor = "green";
}

function clearLight() {
  var pNode = document.getElementById(event.target.id).parentNode;
  var children = pNode.childNodes;
  var i;
  for (i = 1; i < children.length; i++) {
    try {
      children[i].style.backgroundColor = "black";
    } catch (e) {
    }
  }
}

//document.getElementById('red').onclick = makeRed;
//document.getElementById('yellow').onclick = makeYellow;
//document.getElementById('green').onclick = makeGreen;

document.getElementById('redlight').onclick = makeRed;
document.getElementById('yellowlight').onclick = makeYellow;
document.getElementById('greenlight').onclick = makeGreen;

document.getElementById('redlight2').onclick = makeRed;
document.getElementById('yellowlight2').onclick = makeYellow;
document.getElementById('greenlight2').onclick = makeGreen;

document.getElementById('redlight3').onclick = makeRed;
document.getElementById('yellowlight3').onclick = makeYellow;
document.getElementById('greenlight3').onclick = makeGreen;
