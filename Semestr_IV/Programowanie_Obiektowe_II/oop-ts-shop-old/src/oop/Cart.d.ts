import { Product } from "./Product.js";
import { CartItem } from "./CartItem.js";
export declare class Cart {
    private _items;
    addProduct(product: Product, quantity: number): void;
    get items(): CartItem[];
    getTotalPrice(): number;
}
//# sourceMappingURL=Cart.d.ts.map