export class ListProducts {
    productRepository;
    constructor(productRepository) {
        this.productRepository = productRepository;
    }
    async execute() {
        return await this.productRepository.list();
    }
}
//# sourceMappingURL=ListProducts.js.map