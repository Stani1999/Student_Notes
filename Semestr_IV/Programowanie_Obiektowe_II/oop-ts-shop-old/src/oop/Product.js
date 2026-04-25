export class Product {
    _id;
    _name;
    _price;
    constructor(id, name, price) {
        if (!id)
            throw new Error("Product id cannot be empty");
        if (!name)
            throw new Error("Product name cannot be empty");
        if (price < 0)
            throw new Error("Price cannot be negative");
        this._id = id;
        this._name = name;
        this._price = price;
    }
    get id() {
        return this._id;
    }
    get name() {
        return this._name;
    }
    get price() {
        return this._price;
    }
}
//# sourceMappingURL=Product.js.map