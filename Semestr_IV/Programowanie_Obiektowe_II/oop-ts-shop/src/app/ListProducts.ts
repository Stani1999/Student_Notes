import type{ IProductRepository } from "../domain/IProductRepository.js";

export class ListProducts {
    constructor(private readonly repo: IProductRepository) {}

    async execute() {
        return await this.repo.list();
    }

}

// Zadania dodatkowe
// 1. Dodaj FakeProductRepository do testów.
// 2. Dodaj metodę create(product).
// 3. Wprowadź generics do repozytorium.