import { ShippingMethod } from "./ShippingMethod.js";
import { Money } from "../Money.js";

export class ExpressShipping implements ShippingMethod {
    private readonly MAX_WEIGHT = 10;
    private readonly FREE_SHIPPING_THRESHOLD = 50000;

    calculate(weight: number, orderValue: Money): Money {
        this.validate(weight);

        if (orderValue.amount >= this.FREE_SHIPPING_THRESHOLD) {
            return new Money(0);
        }

        return new Money(5000 + weight * 100);
    }

    name(): string {
        return "Express Delivery";
    }

    estimateDeliveryDays(): number {
        return 1;
    }

    validate(weight: number): void {
        if (weight > this.MAX_WEIGHT) {
            throw new Error(`Express delivery weight limit exceeded (max ${this.MAX_WEIGHT}kg)`);
        }
    }
}