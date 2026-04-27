"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Money = void 0;
var Money = /** @class */ (function () {
    function Money(amount, currency) {
        if (currency === void 0) { currency = "PLN"; }
        if (amount < 0) {
            throw new Error("Money cannot be negative");
        }
        this._amount = amount;
        this._currency = currency;
    }
    Money.prototype.equals = function (other) {
        if (!(other instanceof Money)) {
            return false;
        }
        return this._amount === other.amount && this._currency === other.currency;
    };
    Object.defineProperty(Money.prototype, "amount", {
        get: function () {
            return this._amount;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Money.prototype, "currency", {
        get: function () {
            return this._currency;
        },
        enumerable: false,
        configurable: true
    });
    Money.prototype.add = function (other) {
        this.assertSameCurrency(other);
        return new Money(this._amount + other._amount, this._currency);
    };
    Money.prototype.multiply = function (factor) {
        return new Money(this._amount * factor, this._currency);
    };
    Money.prototype.format = function () {
        return "".concat((this._amount / 100).toFixed(2), " ").concat(this._currency);
    };
    Money.prototype.assertSameCurrency = function (other) {
        if (this._currency !== other._currency) {
            throw new Error("Currency mismatch");
        }
    };
    return Money;
}());
exports.Money = Money;
// Dodaj metodę equals() w Money
// Zrób walutę jako union type "PLN" | "EUR" | "USD"
