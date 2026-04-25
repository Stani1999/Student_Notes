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

    getProduct(): Product {
        return this._product;
    }

    getQuantity(): number {
        return this._quantity;
    }

    getPrice(): number {
        return this._product.price * this._quantity;
    }

    increase(quantity: number): void {
        if (quantity <= 0) {
            throw new Error("Quantity must be positive");
        }
        this._quantity += quantity;
    }
}