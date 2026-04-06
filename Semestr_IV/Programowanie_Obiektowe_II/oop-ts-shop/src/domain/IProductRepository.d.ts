import { Product } from "../Product.js";
export interface IProductRepository {
    getByEan(ean: string): Promise<Product | null>;
    list(): Promise<Product[]>;
}
//# sourceMappingURL=IProductRepository.d.ts.map