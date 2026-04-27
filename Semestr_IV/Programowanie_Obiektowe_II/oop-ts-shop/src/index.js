"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
    return g.next = verb(0), g["throw"] = verb(1), g["return"] = verb(2), typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
var CartItem_js_1 = require("./CartItem.js");
var Product_js_1 = require("./Product.js");
var InMemoryProductRepository_js_1 = require("./infra/InMemoryProductRepository.js");
var ListProducts_js_1 = require("./app/ListProducts.js");
var CourierShipping_js_1 = require("./domain/shipping/CourierShipping.js");
var Cart_js_1 = require("./Cart.js");
var Checkout_js_1 = require("./app/Checkout.js");
function main() {
    return __awaiter(this, void 0, void 0, function () {
        var repo, listProducts, products, product1, item1, product2, item2, product3, item3, product4, item4, cart, checkout, total;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    repo = new InMemoryProductRepository_js_1.InMemoryProductRepository();
                    listProducts = new ListProducts_js_1.ListProducts(repo);
                    return [4 /*yield*/, listProducts.execute()];
                case 1:
                    products = _a.sent();
                    console.log(products);
                    product1 = new Product_js_1.Product(100.99, "description1", "name1", "1111111111111");
                    item1 = new CartItem_js_1.CartItem(product1, 1);
                    product2 = new Product_js_1.Product(233.29, "description2", "name2", "1111111111112");
                    item2 = new CartItem_js_1.CartItem(product2, 2);
                    product3 = new Product_js_1.Product(52.69, "description3", "name3", "1111111111113");
                    item3 = new CartItem_js_1.CartItem(product3, 3);
                    product4 = new Product_js_1.Product(10.79, "description4", "name4", "1111111111114");
                    item4 = new CartItem_js_1.CartItem(product4, 4);
                    cart = new Cart_js_1.Cart([item1, item2, item3]);
                    checkout = new Checkout_js_1.Checkout(new CourierShipping_js_1.CourierShipping());
                    total = checkout.calculate(cart);
                    console.log("Total price with shipping: ".concat(total.format()));
                    return [2 /*return*/];
            }
        });
    });
}
main();
