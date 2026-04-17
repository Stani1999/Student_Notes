import { Money } from "../Money.js";

export interface ShippingMethod {
        calculate(weight: number): Money;
        name(): string;
}