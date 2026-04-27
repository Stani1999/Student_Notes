export declare class Product {
    private price;
    private description;
    private name;
    private ean;
    constructor(price: number, description: string, name: string, ean: string);
    static validateName(name: string): void;
    static validatePrice(price: number): void;
    static validateDescription(description: string): void;
    static validateEan(ean: string): void;
    getPrice(): number;
    getDescription(): string;
    getName(): string;
    getEan(): string;
    setPrice(price: number): void;
    setDescription(description: string): void;
    setName(name: string): void;
    setEan(ean: string): void;
}
//# sourceMappingURL=Product.d.ts.map