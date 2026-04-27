type Unit = "MB" | "KG" | "g";

export class Size {
    private _quantity: number;
    private _unit: Unit;

    constructor(quantity: number, unit: Unit) {
        this.validateQuantity(quantity);
        this._quantity = quantity;
        this._unit = unit;
    }

    private validateQuantity(quantity: number) {
        if (quantity < 0) throw new Error("Size cannot be negative");
    }

    public getQuantity(): number {
        return this._quantity;
    }

    public getUnit(): Unit {
        return this._unit;
    }

    public setQuantity(quantity: number): void {
        this.validateQuantity(quantity);
        this._quantity = quantity;
    }

    public setUnit(unit: Unit): void {
        this._unit = unit;
    }

    public toString(): string {
        return `${this._quantity}${this._unit}`;
    }
}