// ts - Exercise 2. Improve exercise 1 to have extra buttons and create them dynamically 
let color = "magenta";
let squareSizeNum = 100;
let squareSizeStr = squareSizeNum + 'px';
// Exercise 2
class ColorChange {
    constructor(div) {
        this.div = div;
    }
    changeColor(color) {
        this.div.style.backgroundColor = color;
        return true;
    }
}
var Colors;
(function (Colors) {
    Colors[Colors["Green"] = 0] = "Green";
    Colors[Colors["Red"] = 1] = "Red";
    Colors[Colors["Magenta"] = 2] = "Magenta";
    Colors[Colors["Yellow"] = 3] = "Yellow";
})(Colors || (Colors = {}));
let elementSets = [];
// Insert 4 pairs div+button
for (let i = 0; i < 4; i++) {
    elementSets.push({ div: document.createElement('div'), button: document.createElement('button') });
}
// For each pair div/button, set the size, change the color, set the OnClick event of each button
// and add them to the body
elementSets.map((element, index) => {
    let colorChange = new ColorChange(element.div);
    element.div.style.width = squareSizeStr;
    element.div.style.height = squareSizeStr;
    element.button.style.width = squareSizeStr;
    element.button.textContent = "Change color";
    document.body.appendChild(element.div);
    document.body.appendChild(element.button);
    element.button.onclick = (event) => {
        colorChange.changeColor(Colors[index]);
    };
});
//# sourceMappingURL=ts_exercise_2.js.map