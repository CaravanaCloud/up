export interface GreeterProps {
    readonly greetee: string;
}

export class Greeter {
    private readonly greetee: string;

    public constructor(props: GreeterProps) {
        this.greetee = props.greetee;
    }

    public greet(): string {
        return `Hello, ${this.greetee}!`
    }
}