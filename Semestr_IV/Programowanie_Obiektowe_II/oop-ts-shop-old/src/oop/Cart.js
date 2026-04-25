import { CartItem } from "./CartItem.js";
export class Cart {
    _items = [];
    addProduct(product, quantity) {
        const existing = this._items.find(item => item.product.id === product.id);
        if (existing) {
            existing.increase(quantity);
        }
        else {
            this._items.push(new CartItem(product, quantity));
        }
    }
    get items() {
        return this._items;
    }
    getTotalPrice() {
        return this._items.reduce((total, item) => total + (item.product.price * item.quantity), 0);
    }
}
//# sourceMappingURL=Cart.js.map