import { Cart } from "../oop/Cart.js";
import type { ShippingMethod } from "../domain/shipping/ShippingMethod.ts";
import type { Money } from "../domain/Money.ts";

export class Checkout {
    constructor(private readonly shipping: ShippingMethod) {}

    calculate(cart: Cart): Money {
        const shippingCost = this.shipping.calculate(cart.getTotalWeight());
        return cart.getTotalPrice().add(shippingCost);
    }
}