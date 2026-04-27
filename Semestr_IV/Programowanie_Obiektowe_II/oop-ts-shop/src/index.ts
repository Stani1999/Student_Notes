import { InMemoryOrderRepository } from "./infra/InMemoryOrderRepository.js";
import { InMemoryProductRepository } from "./infra/InMemoryProductRepository.js";
import { Cart } from "./Cart.js";
import { AddToCart } from "./app/AddToCart.js";
import { Checkout } from "./app/Checkout.js";
import { CourierShipping } from "./domain/shipping/CourierShipping.js";


async function main() {
  // Inicjalizacja
  const productRepo = new InMemoryProductRepository();
  const orderRepo = new InMemoryOrderRepository();
  const cart = new Cart();
  const shipping = new CourierShipping();

  const addToCart = new AddToCart(productRepo, cart);
  const checkout = new Checkout(cart, shipping, orderRepo);

  // Logika
  console.log("Dodawanie produktu...");
  const addResult = await addToCart.execute("1", 2); 

  if (addResult.isOk()) {
    console.log("Tworzenie zamówienia...");
    const checkoutResult = await checkout.execute();

    if (checkoutResult.isOk()) {
      console.log("Sukces! Wygenerowano zamówienie.");
    } else {
      console.error("Błąd checkoutu:", checkoutResult.error);
    }
  } else {
    console.error("Błąd dodawania do koszyka:", addResult.error);
  }
}

main();