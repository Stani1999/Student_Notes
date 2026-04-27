import { Feature } from "./Feature.js";
import { ShippingFeature } from "./ShippingFeature.js";
import { ok, fail } from "./shared/Result.js";
import type { Result } from "./shared/Result.js";

type ProductError =
    | "INVALID_NAME"
    | "INVALID_PRICE"
    | "INVALID_DESCRIPTION"
    | "INVALID_EAN";

export class Product {
    private features: Feature[] = [];

    private constructor(
        private price: number,
        private description: string,
        private name: string,
        private ean: string
    ) {}

    public static isProduct(obj: unknown): obj is Product {
        return obj instanceof Product;
    }

    public static create(
        price: number,
        description: string,
        name: string,
        ean: string,
        features: Feature[] = []
    ): Result<Product, ProductError> {
        if (name.length === 0) return fail("INVALID_NAME");
        if (price <= 0) return fail("INVALID_PRICE");
        if (description.length === 0) return fail("INVALID_DESCRIPTION");

        if (ean.length !== 13 || !/^\d+$/.test(ean)) {
            return fail("INVALID_EAN");
        }

        const product = new Product(price, description, name, ean);

        try {
            features.forEach(f => product.addFeature(f));
        } catch (e) {
            throw e;
        }

        return ok(product);
    }

    public getPrice() { return this.price; }
    public getDescription() { return this.description; }
    public getName() { return this.name; }
    public getEan() { return this.ean; }

    public setPrice(price: number): Result<void, "INVALID_PRICE"> {
        if (price <= 0) return fail("INVALID_PRICE");
        this.price = price;
        return ok(undefined);
    }

    public setDescription(description: string): Result<void, "INVALID_DESCRIPTION"> {
        if (description.length === 0) return fail("INVALID_DESCRIPTION");
        this.description = description;
        return ok(undefined);
    }

    public setName(name: string): Result<void, "INVALID_NAME"> {
        if (name.length === 0) return fail("INVALID_NAME");
        this.name = name;
        return ok(undefined);
    }

    public setEan(ean: string): Result<void, "INVALID_EAN"> {
        if (ean.length !== 13 || !/^\d+$/.test(ean)) {
            return fail("INVALID_EAN");
        }
        this.ean = ean;
        return ok(undefined);
    }

    public getFeatures<T extends Feature>(type: new (...args: any[]) => T): T[] {
        return this.features.filter((f): f is T => f instanceof type);
    }

    public addFeature(feature: Feature): void {
        if (feature instanceof ShippingFeature) {
            const hasShipping = this.features.some(f => f instanceof ShippingFeature);
            if (hasShipping) {
                throw new Error("Product cannot have more than one ShippingFeature!");
            }
        }
        this.features.push(feature);
    }
}