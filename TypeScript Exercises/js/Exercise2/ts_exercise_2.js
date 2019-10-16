// ts - Exercise 2. Improve exercise 1 to have extra buttons and create them dynamically 
var color = "magenta";
var squareSizeNum = 100;
var squareSizeStr = squareSizeNum + 'px';
// Exercise 2
var ColorChange = /** @class */ (function () {
    function ColorChange(div) {
        this.div = div;
        this.div = div;
    }
    ColorChange.prototype.changeColor = function (color) {
        this.div.style.backgroundColor = color;
        return true;
    };
    return ColorChange;
}());
var Colors;
(function (Colors) {
    Colors[Colors["Green"] = 0] = "Green";
    Colors[Colors["Red"] = 1] = "Red";
    Colors[Colors["Magenta"] = 2] = "Magenta";
    Colors[Colors["Yellow"] = 3] = "Yellow";
})(Colors || (Colors = {}));
var elementSets = [];
// Insert 4 pairs div+button
for (var i = 0; i < 4; i++) {
    elementSets.push({ div: document.createElement('div'), button: document.createElement('button') });
}
// For each pair div/button, set the size, change the color, set the OnClick event of each button
// and add them to the body
elementSets.map(function (element, index) {
    var colorChange = new ColorChange(element.div);
    element.div.style.width = squareSizeStr;
    element.div.style.height = squareSizeStr;
    element.button.style.width = squareSizeStr;
    element.button.textContent = "Change color";
    document.body.appendChild(element.div);
    document.body.appendChild(element.button);
    element.button.onclick = function (event) {
        colorChange.changeColor(Colors[index]);
    };
});
//# sourceMappingURL=ts_exercise_2.js.map