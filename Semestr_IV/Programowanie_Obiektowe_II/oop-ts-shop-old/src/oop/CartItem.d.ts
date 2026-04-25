import { Product } from "./Product.js";
export declare class CartItem {
    private readonly _product;
    private _quantity;
    constructor(_product: Product, _quantity: number);
    get product(): Product;
    get quantity(): number;
    increase(quantity: number): void;
}
//# sourceMappingURL=CartItem.d.ts.map