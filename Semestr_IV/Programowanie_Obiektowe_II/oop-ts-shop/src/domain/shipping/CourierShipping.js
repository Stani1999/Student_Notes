"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.CourierShipping = void 0;
var Money_js_1 = require("../Money.js");
var CourierShipping = /** @class */ (function () {
    function CourierShipping() {
    }
    CourierShipping.prototype.calculate = function (weight) {
        return new Money_js_1.Money(1500 + weight * 200);
    };
    CourierShipping.prototype.name = function () {
        return "Courier";
    };
    return CourierShipping;
}());
exports.CourierShipping = CourierShipping;
