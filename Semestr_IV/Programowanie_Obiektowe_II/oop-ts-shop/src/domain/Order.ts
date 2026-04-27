import { Money } from "./Money";

export class Order {
  constructor(
    public readonly id: string,
    public readonly total: Money,
    public readonly status: "PENDING" | "PAID" = "PENDING"
  ) {}
}