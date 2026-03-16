"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class Person {
    name;
    constructor(name) {
        this.name = name;
    }
    greet() {
        return `Hellow, ${this.name}`;
    }
}
const p = new Person("Jan");
console.log(p.greet());
//# sourceMappingURL=index.js.map