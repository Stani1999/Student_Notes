import { Order } from "./Order.js";

export interface IOrderRepository {
  save(order: Order): Promise<void>;
}