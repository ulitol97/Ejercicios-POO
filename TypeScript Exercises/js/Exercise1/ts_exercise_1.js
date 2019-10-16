// ts - Exercise 1.Generate a button to change the background color of the <div> tag 
var color = "magenta";
var squareSizeNum = 100;
var squareSizeStr = squareSizeNum + 'px';
var button = document.createElement('button');
var div = document.createElement('div');
button.textContent = 'Go magenta';
document.body.appendChild(button);
document.body.appendChild(div);
// Function in TS controlling types
var colorChange = function (elem, color) {
    elem.style.backgroundColor = color;
    return true;
};
div.style.width = squareSizeStr;
div.style.height = squareSizeStr;
button.style.width = squareSizeStr;
button.onclick = function (event) {
    colorChange(div, color);
};
//# sourceMappingURL=ts_exercise_1.js.map