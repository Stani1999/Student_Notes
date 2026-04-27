import { Product } from "./Product.js";

export class CartItem {
    private item: Product;
    private quantity: number;

    constructor(item: Product, quantity: number) {
        CartItem.validateQuantity(quantity);
        this.item = item;
        this.quantity = quantity;
    }

    public static validateQuantity(quantity: number) {
        if (quantity <= 0) {
            throw new Error("Invalid quantity!");
        }
    }

    public getQuantity() {
        return this.quantity; 
    }

    public setQuantity(quantity: number) {
        CartItem.validateQuantity(quantity);
        this.quantity = quantity;
    }

    public getName() {
        return this.item.getName();
    }
    public getDescription() {
        return this.item.getDescription();
    }
    public getPrice() {
        return this.item.getPrice();
    }
    public getEan() {
        return this.item.getEan();
    }
}