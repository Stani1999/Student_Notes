export class CartItem {
    item;
    quantity;
    constructor(item, quantity) {
        CartItem.validateQuantity(quantity);
        this.item = item;
        this.quantity = quantity;
    }
    static validateQuantity(quantity) {
        if (quantity <= 0) {
            throw new Error("Invalid quantity!");
        }
    }
    getQuantity() {
        return this.quantity;
    }
    setQuantity(quantity) {
        CartItem.validateQuantity(quantity);
        this.quantity = quantity;
    }
    getName() {
        return this.item.getName();
    }
    getDescription() {
        return this.item.getDescription();
    }
    getPrice() {
        return this.item.getPrice();
    }
    getEan() {
        return this.item.getEan();
    }
}
//# sourceMappingURL=CartItem.js.map