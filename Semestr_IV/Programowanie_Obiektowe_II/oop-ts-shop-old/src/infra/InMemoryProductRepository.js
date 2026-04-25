import { Product } from "../Product.js";
// import { Money } from "../domain/Money";
export class InMemoryProductRepository {
    products = [
        new Product(5000, "laptop", "Laptop", "1111111111111"),
        new Product(700, "mouse", "Mouse", "2222222222222")
    ];
    async getByEan(ean) {
        return this.products.find(p => p.getEan() === ean) ?? null;
    }
    async list() {
        return this.products;
    }
}
//# sourceMappingURL=InMemoryProductRepository.js.map