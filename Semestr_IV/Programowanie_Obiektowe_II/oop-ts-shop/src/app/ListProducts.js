export class ListProducts {
    repo;
    constructor(repo) {
        this.repo = repo;
    }
    async execute() {
        return await this.repo.list();
    }
}
// Zadania dodatkowe
// 1. Dodaj FakeProductRepository do testów.
// 2. Dodaj metodę create(product).
// 3. Wprowadź generics do repozytorium.
//# sourceMappingURL=ListProducts.js.map