import { Money } from "../Money.js";
import { ShippingMethod } from "./ShippingMethod.js";

export class ExpressShippingMethod implements ShippingMethod{
    calculate(weight: number): Money {
        return new Money(2000 + weight * 1000);
    }
    name(): string {
        return "Express";
    }
}