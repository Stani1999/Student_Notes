import { IProductRepository } from "../domain/IProductRepository.js";
import { Product } from "../Product.js";

export class FakeProductRepository implements IProductRepository {
    private products: Product[] = [
            new Product(5000, "laptop", "Laptop", "1111111111111"),
            new Product(700, "mouse", "Mouse", "2222222222222")
    ];
}