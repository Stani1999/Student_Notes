import { IProductRepository } from "../domain/IProductRepository.js";
export declare class ListProducts {
    private productRepository;
    constructor(productRepository: IProductRepository);
    execute(): Promise<import("../oop/Product.js").Product[]>;
}
//# sourceMappingURL=ListProducts.d.ts.map