import { Product } from "../oop/Product.js";
export class InMemoryProductRepository {
    products = [
        new Product("1", "Laptop", 999.99),
        new Product("2", "Smartphone", 499.99)
    ];
    async getById(id) {
        return this.products.find(p => p.id === id) || null;
    }
    async list() {
        return this.products;
    }
}
//# sourceMappingURL=InMemoryProductRepository.js.map