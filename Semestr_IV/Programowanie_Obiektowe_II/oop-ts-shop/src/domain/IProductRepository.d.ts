import { Product } from "../oop/Product.js";
export interface IProductRepository {
    getById(id: string): Promise<Product | null>;
    list(): Promise<Product[]>;
}
//# sourceMappingURL=IProductRepository.d.ts.map