import { CartItem } from "./CartItem.js";
export declare class Cart {
    private items;
    constructor(items: CartItem[]);
    printItems(): void;
    addItem(cartItem: CartItem): void;
    removeItem(cartItem: CartItem): void;
}
//# sourceMappingURL=Cart.d.ts.map