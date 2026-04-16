export class Money {
    _amount;
    _currency;
    constructor(amount, currency = "PLN") {
        if (amount < 0) {
            throw new Error("Money cannot be negative");
        }
        this._amount = amount;
        this._currency = currency;
    }
    get amount() {
        return this._amount;
    }
    get currency() {
        return this._currency;
    }
    add(other) {
        this.assertSameCurrency(other);
        return new Money(this._amount + other._amount, this._currency);
    }
    multiply(factor) {
        return new Money(this._amount * factor, this._currency);
    }
    equals(other) {
        return this._amount === other._amount && this._currency === other._currency;
    }
    format() {
        return `${(this._amount / 100).toFixed(2)} ${this._currency}`;
    }
    assertSameCurrency(other) {
        if (this._currency !== other._currency) {
            throw new Error("Currency mismatch");
        }
    }
}
//# sourceMappingURL=Money.js.map