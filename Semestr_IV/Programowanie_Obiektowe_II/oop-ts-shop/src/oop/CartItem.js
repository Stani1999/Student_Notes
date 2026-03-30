export class CartItem {
    _product;
    _quantity;
    constructor(_product, _quantity) {
        this._product = _product;
        this._quantity = _quantity;
        if (_quantity <= 0) {
            throw new Error("Quantity must be positive");
        }
    }
    get product() {
        return this._product;
    }
    get quantity() {
        return this._quantity;
    }
    increase(quantity) {
        if (quantity <= 0) {
            throw new Error("Quantity must be positive");
        }
        this._quantity += quantity;
    }
}
//# sourceMappingURL=CartItem.js.map