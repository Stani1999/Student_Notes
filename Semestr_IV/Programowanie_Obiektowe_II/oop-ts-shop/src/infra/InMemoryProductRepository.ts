import type { IOrderRepository } from "../domain/IOrderRepository.js";
import { Order } from "../domain/Order.js";

export class InMemoryOrderRepository implements IOrderRepository {
  private orders: Order[] = [];

  async save(order: Order): Promise<void> {
    this.orders.push(order);
    console.log(`Zapisano zamówienie: ${order.id}, kwota: ${order.total.toString()}`);
  }
}