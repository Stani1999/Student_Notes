export class CartItem {
    item;
    quantity;
    constructor(item, quantity) {
        this.item = item;
        this.quantity = quantity;
    }
    changeQuantity(newQuantity) {
        if (newQuantity < 0) {
            throw new Error("Ilość nie może być mniejsza od 0");
        }
        this.quantity = newQuantity;
    }
}
//# sourceMappingURL=CartItem.js.map