var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
// example TS to JS 4
var Control = /** @class */ (function () {
    function Control() {
    }
    return Control;
}());
var Button = /** @class */ (function (_super) {
    __extends(Button, _super);
    function Button() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Button.prototype.select = function () { };
    return Button;
}(Control));
var Picture = /** @class */ (function () {
    function Picture() {
    }
    Picture.prototype.select = function () { };
    return Picture;
}());
// A function that needs a SelectableControl implementation
function f(param) {
}
// Button is a SelectableControl
f(new Button());
// Picture is NOT a SelectableControl
f(new Picture());
//# sourceMappingURL=ts_example_4.js.map