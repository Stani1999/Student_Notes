import { Cart } from "../Cart";
import { IProductRepository } from "../domain/IProductRepository";
import { Result, ok, fail } from "../shared/Result";

type AddToCartError = "PRODUCT_NOT_FOUND" | "INVALID_QUANTITY";

export class AddToCart {
  constructor(
    private readonly repo: IProductRepository,
    private readonly cart: Cart
  ) {}

  async execute(productId: string, quantity: number): Promise<Result<void, AddToCartError>> {
    if (quantity <= 0) {
      return fail("INVALID_QUANTITY");
    }

    const product = await this.repo.getById(productId);

    if (!product) {
      return fail("PRODUCT_NOT_FOUND");
    }

    this.cart.add(product, quantity);
    return ok(undefined);
  }
}