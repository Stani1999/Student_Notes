import { Cart } from "../Cart";
import { ShippingFeature } from "../ShippingFeature";
import { Result, ok, fail } from "../shared/Result";
import { Money } from "../domain/Money";
import { Order } from "../domain/Order";
import { IOrderRepository } from "../domain/IOrderRepository";

type CheckoutError = "EMPTY_CART";

export class Checkout {
  constructor(
    private readonly cart: Cart,
    private readonly shipping: ShippingMethod,
    private readonly orderRepo: IOrderRepository
  ) {}

  async execute(): Promise<Result<Order, CheckoutError>> {
    if (this.cart.totalItems() === 0) {
      return fail("EMPTY_CART");
    }

    const total = this.cart.totalPrice();
    const shippingCost = this.shipping.calculate(this.cart.getTotalWeight());
    const finalAmount = total.add(shippingCost);

    const order = new Order(
      Math.random().toString(36).substring(2, 9),
      finalAmount
    );

    await this.orderRepo.save(order);
    return ok(order);
  }
}