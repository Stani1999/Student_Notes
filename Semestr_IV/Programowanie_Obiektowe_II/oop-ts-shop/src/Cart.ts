import { Product } from "../Product.js";
import { Money } from "../domain/Money";
import { CartItem } from "../CartItem";

export class Cart {
  private items: CartItem[] = [];

  add(product: Product, quantity: number): void {
    this.items.push(new CartItem(product, quantity));
  }

  totalItems(): number {
    return this.items.length;
  }

  totalPrice(): Money {
    return this.items.reduce(
      (sum, item) => sum.add(item.product.price.multiply(item.quantity)),
      new Money(0, "PLN")
    );
  }

  getTotalWeight(): number {
    return this.items.reduce(
      (sum, item) => sum + (item.product.weight * item.quantity),
      0
    );
  }
}