import { Cart } from "./Cart.js";
import { Product } from "./Product.js";
import { Money } from "./domain/Money.js";
import { CartItem } from "./CartItem.js";

const cart = new Cart<Product>();

const p1 = new Product("1", "Chleb", new Money(5, "PLN"));
const p2 = new Product("2", "Mleko", new Money(4, "PLN"));

cart.addItem(p1);
cart.addItem(p1); 
cart.addItem(p2);

console.log("Po dodaniu przedmiotów koszyk zawiera:", cart.getItems().length, "pozycje.");

cart.changeQuantity("1", 5);
console.log("Ilość produktu '1' po zmianie:", cart.getItems()[0].quantity);

try {
  cart.changeQuantity("1", -1);
} catch (e) {
  if (e instanceof Error) {
    console.log("Walidacja działa poprawnie:", e.message);
  }
}

const productList = cart.getItems().map((i: CartItem<Product>) => i.item);
const filtered = Cart.getFeatusers(productList, "name", "Chleb");
console.log("Wynik getFeatusers (szukanie 'Chleb'):", filtered.length, "element(y)");

cart.removeItem("2");
console.log("Liczba pozycji po usunięciu produktu '2':", cart.getItems().length);

cart.clean();
console.log("Liczba pozycji po wyczyszczeniu koszyka:", cart.getItems().length);