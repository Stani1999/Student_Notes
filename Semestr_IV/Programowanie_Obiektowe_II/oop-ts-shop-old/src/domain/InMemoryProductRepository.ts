import { IProductRepository } from "./IProductRepository.js";
import { Product } from "../oop/Product.js";

export class InMemoryProductRepository
    implements IProductRepository {

        private products: Product[] = [
            new Product("1", "Laptop", 999.99),
            new Product("2", "Smartphone", 499.99)
        ];
    async getById(id: string): Promise<Product | null> {
        return this.products.find(p => p.id === id) || null;
    }
    async list(): Promise<Product[]> {
        return this.products;
    }
}