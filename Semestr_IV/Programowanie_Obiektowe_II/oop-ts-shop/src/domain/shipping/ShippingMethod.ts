import { Money } from "../Money.js";

export interface ShippingMethod {
    calculate(weight: number, orderValue: Money): Money;
    name(): string;
    estimateDeliveryDays(): number;
    validate(weight: number): void;
}