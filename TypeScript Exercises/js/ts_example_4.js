// example TS to JS 4
class Control {
}
class Button extends Control {
    select() { }
}
class Picture {
    select() { }
}
// A function that needs a SelectableControl implementation
function f(param) {
}
// Button is a SelectableControl
f(new Button());
// Picture is NOT a SelectableControl
f(new Picture());
//# sourceMappingURL=ts_example_4.js.map