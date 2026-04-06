import { IProductRepository } from "../domain/IProductRepository.js";
import { Product } from "../Product.js";
// import { Money } from "../domain/Money";

export class InMemoryProductRepository implements IProductRepository {
    private products: Product[] = [
        new Product(5000, "laptop", "Laptop", "1111111111111"),
        new Product(700, "mouse", "Mouse", "2222222222222")
    ];

    async getByEan(ean: string): Promise<Product | null> {
        return this.products.find(p => p.getEan() === ean) ?? null;
    }

    async list(): Promise<Product[]> {
        return this.products;
    }
}
