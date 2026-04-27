"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Product = void 0;
var ShippingFeature_js_1 = require("./ShippingFeature.js");
var Product = /** @class */ (function () {
    function Product(price, description, name, ean, features) {
        if (features === void 0) { features = []; }
        var _this = this;
        this.features = [];
        Product.validateName(name);
        Product.validatePrice(price);
        Product.validateDescription(description);
        Product.validateEan(ean);
        this.price = price;
        this.description = description;
        this.name = name;
        this.ean = ean;
        features.forEach(function (f) { return _this.addFeature(f); });
    }
    Product.validateName = function (name) {
        if (name.length == 0)
            throw new Error("Invalid name!");
    };
    Product.validatePrice = function (price) {
        if (price <= 0)
            throw new Error("Invalid price!");
    };
    Product.validateDescription = function (description) {
        if (description.length == 0)
            throw new Error("Invalid description!");
    };
    Product.validateEan = function (ean) {
        if (ean.length != 13)
            throw new Error("Invalid EAN!");
        for (var _i = 0, ean_1 = ean; _i < ean_1.length; _i++) {
            var chr = ean_1[_i];
            if (!(chr >= '0' && chr <= '9'))
                throw new Error("Invalid EAN!");
        }
    };
    Product.prototype.getPrice = function () { return this.price; };
    Product.prototype.getDescription = function () { return this.description; };
    Product.prototype.getName = function () { return this.name; };
    Product.prototype.getEan = function () { return this.ean; };
    Product.prototype.setPrice = function (price) {
        Product.validatePrice(price);
        this.price = price;
    };
    Product.prototype.setDescription = function (description) {
        Product.validateDescription(description);
        this.description = description;
    };
    Product.prototype.setName = function (name) {
        Product.validateName(name);
        this.name = name;
    };
    Product.prototype.setEan = function (ean) {
        Product.validateEan(ean);
        this.ean = ean;
    };
    Product.prototype.getFeatures = function (type) {
        return this.features.filter(function (f) { return f instanceof type; });
    };
    Product.prototype.addFeature = function (feature) {
        if (feature instanceof ShippingFeature_js_1.ShippingFeature) {
            var hasShipping = this.features.some(function (f) { return f instanceof ShippingFeature_js_1.ShippingFeature; });
            if (hasShipping) {
                throw new Error("Product cannot have more than one ShippingFeature!");
            }
        }
        this.features.push(feature);
    };
    return Product;
}());
exports.Product = Product;
