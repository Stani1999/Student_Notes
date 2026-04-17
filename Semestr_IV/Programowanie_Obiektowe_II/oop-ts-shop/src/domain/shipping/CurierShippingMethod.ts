import { Money } from "../Money.js";
import { ShippingMethod } from "./ShippingMethod.js";

export class CourierShippingMethod implements ShippingMethod{
    calculate(weight: number): Money {
        return new Money(1500 + weight * 200);
    }
    name(): string {
        return "Courier";
    }
}