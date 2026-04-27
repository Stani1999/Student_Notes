"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Checkout = void 0;
var Money_js_1 = require("../domain/Money.js");
var Checkout = /** @class */ (function () {
    function Checkout(shipping) {
        this.shipping = shipping;
    }
    Checkout.prototype.calculate = function (cart) {
        var shippingCost = this.shipping.calculate(cart.getTotalWeight());
        return new Money_js_1.Money(cart.getTotal()).add(shippingCost);
    };
    return Checkout;
}());
exports.Checkout = Checkout;
