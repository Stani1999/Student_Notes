import { Feature } from "./Feature.js";

export class ReturnPolicyFeature extends Feature {
    constructor(
        private days: number,
        private isFree: boolean
    ) {
        super();
        if (days < 0) throw new Error("Return days cannot be negative");
    }

    public getType(): string {
        return "ReturnPolicy";
    }

    public getDays(): number {
        return this.days;
    }

    public isFreeReturn(): boolean {
        return this.isFree;
    }
}