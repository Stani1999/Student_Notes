import { Product } from "./Product.js";
export declare class CartItem {
    private item;
    private quantity;
    constructor(item: Product, quantity: number);
    static validateQuantity(quantity: number): void;
    getQuantity(): number;
    setQuantity(quantity: number): void;
    getName(): string;
    getDescription(): string;
    getPrice(): number;
    getEan(): string;
}
//# sourceMappingURL=CartItem.d.ts.map