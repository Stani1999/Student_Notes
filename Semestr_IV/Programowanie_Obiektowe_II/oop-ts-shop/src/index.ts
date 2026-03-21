class Item {
    private name: string;
    private price: number;
    private description: string;
    private EAN: string;

    constructor(name: string, price: number, description: string, EAN: string) {
        this.name = name;
        this.price = price;
        this.description = description;
        this.EAN = EAN;
    }

    public getName(): string { return this.name; }
    public getPrice(): number { return this.price; }
    public getDescription(): string { return this.description; }
    public getEAN(): string { return this.EAN; }
}

class Basket {
    private items: { product: Item, quantity: number }[] = [];

    addItem(item: Item, quantity: number): void {
        const existing = this.items.find(i => i.product.getEAN() === item.getEAN());
        if (existing) {
            existing.quantity += quantity;
        } else {
            this.items.push({ product: item, quantity: quantity });
        }
    }

    getItems(): { product: Item, quantity: number }[] {
        return this.items;
    }

    getTotalPrice(): number {
        return this.items.reduce((total, entry) => total + (entry.product.getPrice() * entry.quantity), 0);
    }

    removeItem(ean: string, quantity: number = 1): void {
        const index = this.items.findIndex(i => i.product.getEAN() === ean);
        if (index > -1) {
            this.items[index].quantity -= quantity;
            if (this.items[index].quantity <= 0) {
                this.items.splice(index, 1);
            }
        }
    }
}

const laptopCatalog: Item[] = [
    new Item("Laptop Pro", 5000, "RTX 6070TI 16GB DDR8, 32GB RAM, 2TB SSD Ryzen 7 6700X3D", "EAN1"),
    new Item("Laptop Home", 3000, "RTX 6050 6GB DDR7, 16GB RAM, 1TB SSD Core Ultra 367", "EAN2")
];

const basket = new Basket();
basket.addItem(laptopCatalog[0], 2);
basket.addItem(laptopCatalog[1], 1);

console.log("Items in the basket:");
for (let entry of basket.getItems()) {
    console.log(`${entry.product.getName()} x${entry.quantity} - ${entry.product.getPrice() * entry.quantity} PLN`);
}
console.log(`Total price: ${basket.getTotalPrice()} PLN`);