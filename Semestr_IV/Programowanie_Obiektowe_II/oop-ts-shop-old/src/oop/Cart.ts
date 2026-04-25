import { Product } from "./Product.js";
import { CartItem } from "./CartItem.js";

export class Cart {
    private _items: CartItem[] = [];

    addProduct(product: Product, quantity: number): void {
        const existing = this._items.find(item => item.getProduct().id === product.id);
        if (existing) {
            existing.increase(quantity);
        } else {
            this._items.push(new CartItem(product, quantity));
        }
    }

    getItems(): CartItem[] {
        return this._items;
    }

    getTotalWeight(): number {
        return this.getItems().reduce((sum, item) => sum + (item.getQuantity() * 1), 0);
    }
        getTotalPrice(): number {
        return this._items.reduce((total, item) => total + (item.getPrice()), 0);
    }
}