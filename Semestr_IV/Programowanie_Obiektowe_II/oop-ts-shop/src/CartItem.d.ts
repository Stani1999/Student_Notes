import { Identifiable } from "./Identifiable.js";
export declare class CartItem<T extends Identifiable> {
    readonly item: T;
    quantity: number;
    constructor(item: T, quantity: number);
    changeQuantity(newQuantity: number): void;
}
//# sourceMappingURL=CartItem.d.ts.map