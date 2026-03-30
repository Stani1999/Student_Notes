import { IProductRepository } from "../domain/IProductRepository.js";

export class ListProducts {
    constructor(private productRepository: IProductRepository) {}
    
    async execute() {
        return await this.productRepository.list();
    }
}