export class Cart {
    items = [];
    constructor(items) {
        this.items = items;
    }
    printItems() {
        for (var item of this.items) {
            console.log(`Nazwa: ${item.getName()}`);
            console.log(`Opis: ${item.getDescription()}`);
            console.log(`Cena: ${item.getPrice()}`);
            console.log(`Ilość: ${item.getQuantity()}`);
            console.log(`EAN: ${item.getEan()}`);
            console.log("---------------------------");
        }
    }
    addItem(cartItem) {
        for (var existingItem of this.items) {
            if (existingItem.getEan() === cartItem.getEan()) {
                existingItem.setQuantity(existingItem.getQuantity() + cartItem.getQuantity());
                return;
            }
        }
        this.items.push(cartItem);
    }
    removeItem(cartItem) {
        this.items = this.items.filter(item => item.getEan() !== cartItem.getEan());
    }
}
//# sourceMappingURL=Cart.js.map