"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Size = void 0;
var Size = /** @class */ (function () {
    function Size(quantity, unit) {
        this.validateQuantity(quantity);
        this._quantity = quantity;
        this._unit = unit;
    }
    Size.prototype.validateQuantity = function (quantity) {
        if (quantity < 0)
            throw new Error("Size cannot be negative");
    };
    Size.prototype.getQuantity = function () {
        return this._quantity;
    };
    Size.prototype.getUnit = function () {
        return this._unit;
    };
    Size.prototype.setQuantity = function (quantity) {
        this.validateQuantity(quantity);
        this._quantity = quantity;
    };
    Size.prototype.setUnit = function (unit) {
        this._unit = unit;
    };
    Size.prototype.toString = function () {
        return "".concat(this._quantity).concat(this._unit);
    };
    return Size;
}());
exports.Size = Size;
