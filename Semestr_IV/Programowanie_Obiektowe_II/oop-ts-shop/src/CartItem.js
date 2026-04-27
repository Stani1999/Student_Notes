"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.CartItem = void 0;
var CartItem = /** @class */ (function () {
    function CartItem(item, quantity) {
        CartItem.validateQuantity(quantity);
        this.item = item;
        this.quantity = quantity;
    }
    CartItem.validateQuantity = function (quantity) {
        if (quantity <= 0) {
            throw new Error("Invalid quantity!");
        }
    };
    CartItem.prototype.getQuantity = function () {
        return this.quantity;
    };
    CartItem.prototype.setQuantity = function (quantity) {
        CartItem.validateQuantity(quantity);
        this.quantity = quantity;
    };
    CartItem.prototype.getName = function () {
        return this.item.getName();
    };
    CartItem.prototype.getDescription = function () {
        return this.item.getDescription();
    };
    CartItem.prototype.getPrice = function () {
        return this.item.getPrice();
    };
    CartItem.prototype.getEan = function () {
        return this.item.getEan();
    };
    return CartItem;
}());
exports.CartItem = CartItem;
