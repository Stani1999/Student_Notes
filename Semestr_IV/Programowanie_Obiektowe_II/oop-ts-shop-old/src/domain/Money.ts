export type Currency = "PLN" | "EUR" | "USD";

export class Money {
    private readonly _amount: number;
    private readonly _currency: Currency;

    constructor(amount: number, currency: Currency = "PLN") {
        if (amount < 0) {
            throw new Error("Money cannot be negative");
        }

        this._amount = amount;
        this._currency = currency;
    }

    get amount(): number {
        return this._amount;
    }

    get currency(): Currency { 
        return this._currency;
    }

    add(other: Money): Money {
        this.assertSameCurrency(other);
        return new Money(this._amount + other._amount, this._currency);
    }

    multiply(factor: number): Money {
        return new Money(this._amount * factor, this._currency);
    }

    equals(other: Money): boolean {
        return this._amount === other._amount && this._currency === other._currency;
    }

    format(): string {
        return `${(this._amount / 100).toFixed(2)} ${this._currency}`;
    }

    private assertSameCurrency(other: Money): void {
        if (this._currency !== other._currency) {
            throw new Error("Currency mismatch");
        }
    }
}