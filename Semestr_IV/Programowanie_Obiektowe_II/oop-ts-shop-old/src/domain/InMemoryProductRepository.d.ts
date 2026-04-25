import { IProductRepository } from "./IProductRepository.js";
import { Product } from "../oop/Product.js";
export declare class InMemoryProductRepository implements IProductRepository {
    private products;
    getById(id: string): Promise<Product | null>;
    list(): Promise<Product[]>;
}
//# sourceMappingURL=InMemoryProductRepository.d.ts.map