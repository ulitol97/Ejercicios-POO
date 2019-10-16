// ts - Exercise 1. Generate a button to change the background color of the <div> tag 
let color = "magenta";
let squareSizeNum = 100;
let squareSizeStr = squareSizeNum + 'px';
let button = document.createElement('button');
let div = document.createElement('div');
button.textContent = 'Go magenta';
document.body.appendChild(button);
document.body.appendChild(div);
// Function in TS controlling types
let colorChange = (elem, color) => {
    elem.style.backgroundColor = color;
    return true;
};
div.style.width = squareSizeStr;
div.style.height = squareSizeStr;
button.style.width = squareSizeStr;
button.onclick = (event) => {
    colorChange(div, color);
};
//# sourceMappingURL=ts_exercise_1.js.map