import { Product } from "./oop/Product.js";
import { Cart } from "./oop/Cart.js";
import { InMemoryProductRepository } from "./domain/InMemoryProductRepository.js";
import { ListProducts } from "./app/ListProducts.js";
async function main() {
    const repo = new InMemoryProductRepository();
    const listProducts = new ListProducts(repo);
    const products = await listProducts.execute();
    console.log(products);
}
main();
try {
    const laptop = new Product("EAN1", "Laptop Pro", 5000);
    const mouse = new Product("EAN2", "Mouse", 100);
    const myCart = new Cart();
    myCart.addProduct(laptop, 1);
    myCart.addProduct(laptop, 1);
    myCart.addProduct(mouse, 5);
    console.log("Koszyk:");
    myCart.items.forEach(item => {
        console.log(`${item.product.name} | Ilość: ${item.quantity} | Suma: ${item.product.price * item.quantity} PLN`);
    });
    console.log(`Do zapłaty: ${myCart.getTotalPrice()} PLN`);
}
catch (error) {
    if (error instanceof Error) {
        console.error("Błąd:", error.message);
    }
}
//# sourceMappingURL=index.js.map