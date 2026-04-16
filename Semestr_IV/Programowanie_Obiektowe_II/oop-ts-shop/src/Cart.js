import { CartItem } from "./CartItem.js";
export class Cart {
    items = [];
    getItems() {
        return this.items;
    }
    addItem(item) {
        const existingItem = this.items.find((cartItem) => cartItem.item.id === item.id);
        if (existingItem) {
            existingItem.quantity++;
        }
        else {
            this.items.push(new CartItem(item, 1));
        }
    }
    removeItem(itemId) {
        this.items = this.items.filter((cartItem) => cartItem.item.id !== itemId);
    }
    changeQuantity(itemId, newQuantity) {
        const cartItem = this.items.find((ci) => ci.item.id === itemId);
        if (cartItem) {
            cartItem.changeQuantity(newQuantity);
        }
    }
    clean() {
        this.items = [];
    }
    static getFeatusers(list, key, value) {
        return list.filter((item) => item[key] === value);
    }
}
//# sourceMappingURL=Cart.js.map