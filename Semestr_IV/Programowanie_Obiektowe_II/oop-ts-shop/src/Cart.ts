import { CartItem } from "./CartItem.js";
import { Identifiable } from "./Identifiable.js";

export class Cart<T extends Identifiable> {
  private items: CartItem<T>[] = [];

  getItems(): CartItem<T>[] {
    return this.items;
  }

  addItem(item: T): void {
    const existingItem = this.items.find(
      (cartItem) => cartItem.item.id === item.id
    );

    if (existingItem) {
      existingItem.quantity++;
    } else {
      this.items.push(new CartItem(item, 1));
    }
  }

  removeItem(itemId: string): void {
    this.items = this.items.filter((cartItem) => cartItem.item.id !== itemId);
  }

  changeQuantity(itemId: string, newQuantity: number): void {
    const cartItem = this.items.find((ci) => ci.item.id === itemId);
    if (cartItem) {
      cartItem.changeQuantity(newQuantity);
    }
  }

  clean(): void {
    this.items = [];
  }

  static getFeatusers<T>(list: T[], key: keyof T, value: T[keyof T]): T[] {
    return list.filter((item) => item[key] === value);
  }
}