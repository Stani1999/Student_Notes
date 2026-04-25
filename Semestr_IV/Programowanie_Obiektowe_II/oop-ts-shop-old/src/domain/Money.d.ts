export type Currency = "PLN" | "EUR" | "USD";
export declare class Money {
    private readonly _amount;
    private readonly _currency;
    constructor(amount: number, currency?: Currency);
    get amount(): number;
    get currency(): Currency;
    add(other: Money): Money;
    multiply(factor: number): Money;
    equals(other: Money): boolean;
    format(): string;
    private assertSameCurrency;
}
//# sourceMappingURL=Money.d.ts.map