export class Product {
    price;
    description;
    name;
    ean;
    constructor(price, description, name, ean) {
        Product.validateName(name);
        Product.validatePrice(price);
        Product.validateDescription(description);
        Product.validateEan(ean);
        this.price = price;
        this.description = description;
        this.name = name;
        this.ean = ean;
    }
    static validateName(name) {
        if (name.length == 0) {
            throw new Error("Invalid name!");
        }
    }
    static validatePrice(price) {
        if (price <= 0) {
            throw new Error("Invalid price!");
        }
    }
    static validateDescription(description) {
        if (description.length == 0) {
            throw new Error("Invalid description!");
        }
    }
    static validateEan(ean) {
        if (ean.length != 13) {
            throw new Error("Invalid EAN!");
        }
        for (var chr of ean) {
            if (!(chr >= '0' && chr <= '9')) {
                throw new Error("Invalid EAN!");
            }
        }
    }
    getPrice() {
        return this.price;
    }
    getDescription() {
        return this.description;
    }
    getName() {
        return this.name;
    }
    getEan() {
        return this.ean;
    }
    setPrice(price) {
        Product.validatePrice(price);
        this.price = price;
    }
    setDescription(description) {
        Product.validateDescription(description);
        this.description = description;
    }
    setName(name) {
        Product.validateName(name);
        this.name = name;
    }
    setEan(ean) {
        Product.validateEan(ean);
        this.ean = ean;
    }
}
//# sourceMappingURL=Product.js.map