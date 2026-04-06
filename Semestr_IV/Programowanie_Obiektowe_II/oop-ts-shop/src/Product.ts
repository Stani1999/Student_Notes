export class Product {
    private price: number;
    private description: string;
    private name: string;
    private ean: string;

    constructor(price: number, description: string, name: string, ean: string) {
        Product.validateName(name);
        Product.validatePrice(price);
        Product.validateDescription(description);
        Product.validateEan(ean);
        this.price = price;
        this.description = description;
        this.name = name;
        this.ean = ean;
    }

    public static validateName(name: string) {
        if (name.length == 0) {
            throw new Error("Invalid name!");
        }
    }

    public static validatePrice(price: number) {
        if (price <= 0) {
            throw new Error("Invalid price!");
        }
    }

    public static validateDescription(description: string) {
        if (description.length == 0) {
            throw new Error("Invalid description!");
        }
    }

    public static validateEan(ean: string) {
        if (ean.length != 13) {
            throw new Error("Invalid EAN!");
        }
        for (var chr of ean) {
            if (!(chr >= '0' && chr <= '9')) {
                throw new Error("Invalid EAN!");
            } 
        }
    }

    public getPrice() {
        return this.price;
    }
    public getDescription() {
        return this.description;
    }
    public getName() {
        return this.name;
    }
    public getEan() {
        return this.ean;
    }

    public setPrice(price: number) {
        Product.validatePrice(price);
        this.price = price;
    }
    public setDescription(description: string) {
        Product.validateDescription(description);
        this.description = description;
    }
    public setName(name: string) {
        Product.validateName(name);
        this.name = name;
    }
    public setEan(ean: string) {
        Product.validateEan(ean);
        this.ean = ean;
    }
}