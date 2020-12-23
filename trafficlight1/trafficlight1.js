// script.js
// when user 'clicks' on the div id 'red', evoke the function makeRed()
document.getElementById('red').onclick = makeRed;
document.getElementById('yellow').onclick = makeYellow;
document.getElementById('green').onclick = makeGreen;
document.getElementById('redlight').onclick = makeRed;
document.getElementById('yellowlight').onclick = makeYellow;
document.getElementById('greenlight').onclick = makeGreen;

function makeRed() {
    console.log("fn: makered")
    clearLight();
    document.getElementById('redlight').style.backgroundColor = "red";
}
function makeYellow() {
    clearLight();
    document.getElementById('yellowlight').style.backgroundColor = "yellow";
}
function makeGreen() {
    clearLight();
    document.getElementById('greenlight').style.backgroundColor =  "green";
}
function clearLight() {
    document.getElementById('redlight').style.backgroundColor =  "black";
    document.getElementById('yellowlight').style.backgroundColor = "black";
    document.getElementById('greenlight').style.backgroundColor = "black";
}
