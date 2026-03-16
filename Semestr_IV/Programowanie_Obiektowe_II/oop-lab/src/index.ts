class Person {
        constructor(private name: string) {}

        greet(): string {
                return `Hellow, ${this.name}`;
        }
}

const p = new Person("Jan");
console.log(p.greet());
