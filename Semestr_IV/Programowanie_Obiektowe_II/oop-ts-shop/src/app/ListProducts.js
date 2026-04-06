export class ListProducts {
    repo;
    constructor(repo) {
        this.repo = repo;
    }
    async execute() {
        return await this.repo.list();
    }
}
//# sourceMappingURL=ListProducts.js.map