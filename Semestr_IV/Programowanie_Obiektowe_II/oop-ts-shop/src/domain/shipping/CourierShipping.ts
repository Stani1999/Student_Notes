import { ShippingMethod } from "./ShippingMethod.js";
import { Money } from "../Money.js";

export class CourierShipping implements ShippingMethod {
    calculate(weight: number, orderValue: Money): Money {
        this.validate(weight);
        return new Money(1500 + weight * 200);
    }

    name(): string {
        return "Courier";
    }

    estimateDeliveryDays(): number {
        return 3;
    }

    validate(weight: number): void {
        if (weight > 1000) {
            throw new Error("Courier delivery weight limit exceeded");
        }
    }
}