import { CartItem } from "./CartItem.js";
import { Identifiable } from "./Identifiable.js";
export declare class Cart<T extends Identifiable> {
    private items;
    getItems(): CartItem<T>[];
    addItem(item: T): void;
    removeItem(itemId: string): void;
    changeQuantity(itemId: string, newQuantity: number): void;
    clean(): void;
    static getFeatusers<T>(list: T[], key: keyof T, value: T[keyof T]): T[];
}
//# sourceMappingURL=Cart.d.ts.map