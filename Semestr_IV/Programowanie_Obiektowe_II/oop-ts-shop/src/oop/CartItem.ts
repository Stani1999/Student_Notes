import { Product } from "./Product.js";

export class CartItem {
    constructor(
        private readonly _product: Product,
        private _quantity: number
    ) {
        if (_quantity <= 0) {
            throw new Error("Quantity must be positive");
        }
    }

    get product(): Product {
        return this._product;
    }

    get quantity(): number {
        return this._quantity;
    }

    increase(quantity: number): void {
        if (quantity <= 0) {
            throw new Error("Quantity must be positive");
        }
        this._quantity += quantity;
    }
}