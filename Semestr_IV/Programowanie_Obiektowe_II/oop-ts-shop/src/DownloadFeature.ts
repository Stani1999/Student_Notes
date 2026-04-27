import { Feature } from "./Feature.js";
import { Size } from "./Size.js";

export class DownloadFeature extends Feature {
    constructor(
        private url: string,
        private size: Size
    ) {
        super();
        if (!url.startsWith("http")) throw new Error("Invalid URL");
    }

    public getType(): string {
        return "Download";
    }

    public getUrl(): string {
        return this.url;
    }

    public getSize(): Size {
        return this.size;
    }
}