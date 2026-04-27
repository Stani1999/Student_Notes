"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.ShippingFeature = void 0;
var Feature_js_1 = require("./Feature.js");
var ShippingFeature = /** @class */ (function (_super) {
    __extends(ShippingFeature, _super);
    function ShippingFeature(size, weight) {
        var _this = _super.call(this) || this;
        _this.size = size;
        _this.weight = weight;
        if (weight < 0)
            throw new Error("Weight cannot be negative");
        return _this;
    }
    ShippingFeature.prototype.getType = function () {
        return "Shipping";
    };
    ShippingFeature.prototype.getSize = function () {
        return this.size;
    };
    ShippingFeature.prototype.getWeight = function () {
        return this.weight;
    };
    return ShippingFeature;
}(Feature_js_1.Feature));
exports.ShippingFeature = ShippingFeature;
