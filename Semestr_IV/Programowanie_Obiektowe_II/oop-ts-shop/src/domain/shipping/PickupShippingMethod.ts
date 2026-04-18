import { ShippingMethod } from "./ShippingMethod.js";
import { Money } from "../Money.js";

export class PickupShippingMethod implements ShippingMethod {
    calculate(): Money {
        return new Money(0);
    }
    name(): string {
        return "Pickup";
    }
}