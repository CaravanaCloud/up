package upcli;

import picocli.CommandLine;
import picocli.CommandLine.Command;
import picocli.CommandLine.Parameters;
import org.graalvm.polyglot.*;

import java.io.BufferedReader;
import java.io.InputStreamReader;

@Command(name = "greeting", mixinStandardHelpOptions = true)
public class GreetingCommand implements Runnable {

    @Parameters(paramLabel = "<name>", defaultValue = "world",
        description = "Your name.")
    String name;

    @Override
    public void run() {
        var input = "{}";
        try (Context context = Context.create("js")) {
            Value parse = context.eval("js", "JSON.parse");
            Value stringify = context.eval("js", "JSON.stringify");
            Value result = stringify.execute(parse.execute(input), null, 2);
            System.out.println("Hello world, from js!\n");
            System.out.println(result.asString());
        }
        System.out.println("Hello world, from java!\n");
    }

}
