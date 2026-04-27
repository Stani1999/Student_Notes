import { Feature } from "./Feature.js";
import { Size } from "./Size.js";

export class ShippingFeature extends Feature {
    constructor(
        private size: Size,
        private weight: number
    ) {
        super();
        if (weight < 0) throw new Error("Weight cannot be negative");
    }

    public getType(): string {
        return "Shipping";
    }

    public getSize(): Size {
        return this.size;
    }

    public getWeight(): number {
        return this.weight;
    }
}