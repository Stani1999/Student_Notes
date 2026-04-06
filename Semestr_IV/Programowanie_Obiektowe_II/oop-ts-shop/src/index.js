// import { CartItem } from "./CartItem.js";
// import { Cart } from "./Cart.js";
// import { Product } from "./Product.js";
// const product1 = new Product(100.99, "description1", "name1", "1111111111111");
// const item1 = new CartItem(product1, 1);
// const product2 = new Product(233.29, "description2", "name2", "1111111111112");
// const item2 = new CartItem(product2, 2);
// const product3 = new Product(52.69, "description3", "name3", "1111111111113");
// const item3 = new CartItem(product3, 3);
// const product4 = new Product(10.79, "description4", "name4", "1111111111114");
// const item4 = new CartItem(product4, 4);
// const cart = new Cart([item1, item2, item3]);
// cart.printItems();
// cart.addItem(item4);
// cart.printItems();
// cart.removeItem(item3);
// cart.printItems();
import { InMemoryProductRepository } from "./infra/InMemoryProductRepository.js";
import { ListProducts } from "./app/ListProducts.js";
async function main() {
    const repo = new InMemoryProductRepository();
    const listProducts = new ListProducts(repo);
    const products = await listProducts.execute();
    console.log(products);
}
main();
//# sourceMappingURL=index.js.map