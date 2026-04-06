import type { IProductRepository } from "../domain/IProductRepository.js";
export declare class ListProducts {
    private readonly repo;
    constructor(repo: IProductRepository);
    execute(): Promise<import("../Product.js").Product[]>;
}
//# sourceMappingURL=ListProducts.d.ts.map