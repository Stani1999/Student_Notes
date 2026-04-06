import { IProductRepository } from "../domain/IProductRepository.js";
import { Product } from "../Product.js";
export declare class InMemoryProductRepository implements IProductRepository {
    private products;
    getByEan(ean: string): Promise<Product | null>;
    list(): Promise<Product[]>;
}
//# sourceMappingURL=InMemoryProductRepository.d.ts.map