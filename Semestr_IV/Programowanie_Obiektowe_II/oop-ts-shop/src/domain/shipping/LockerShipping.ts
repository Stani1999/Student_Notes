import { ShippingMethod } from "./ShippingMethod.js";
import { Money } from "../Money.js";

export class LockerShipping implements ShippingMethod {
    calculate(weight: number, orderValue: Money): Money {
        this.validate(weight);
        return new Money(100 + weight * 2);
    }

    name(): string {
        return "Locker";
    }

    estimateDeliveryDays(): number {
        return 2;
    }

    validate(weight: number): void {
        if (weight > 25) {
            throw new Error("Locker delivery weight limit exceeded (max 25kg)");
        }
    }
}