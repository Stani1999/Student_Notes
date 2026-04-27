import { ShippingMethod } from "./ShippingMethod.js";
import { Money } from "../Money.js";

export class PickupShipping implements ShippingMethod {
    calculate(weight: number, orderValue: Money): Money {
        return new Money(0);
    }

    name(): string {
        return "Pickup";
    }

    estimateDeliveryDays(): number {
        return 0;
    }

    validate(weight: number): void {}
}