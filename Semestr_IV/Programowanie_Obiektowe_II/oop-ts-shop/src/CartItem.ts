import { Identifiable } from "./Identifiable.js";

export class CartItem<T extends Identifiable> {
  constructor(public readonly item: T, public quantity: number) {}

  changeQuantity(newQuantity: number): void {
    if (newQuantity < 0) {
      throw new Error("Ilość nie może być mniejsza od 0");
    }
    this.quantity = newQuantity;
  }
}