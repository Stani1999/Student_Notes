import { Product } from "./Product.js";
import { CartItem } from "./CartItem.js";

export class Cart {
    private _items: CartItem[] = [];

    addProduct(product: Product, quantity: number): void {
        const existing = this._items.find(item => item.product.id === product.id);
        if (existing) {
            existing.increase(quantity);
        } else {
            this._items.push(new CartItem(product, quantity));
        }
    }

    get items(): CartItem[] {
        return this._items;
    }

    getTotalPrice(): number {
        return this._items.reduce((total, item) => total + (item.product.price * item.quantity), 0);
    }
}