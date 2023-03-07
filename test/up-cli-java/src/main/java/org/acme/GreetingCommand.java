package org.acme;

import picocli.CommandLine;
import picocli.CommandLine.Command;
import picocli.CommandLine.Parameters;
import upcli.*;

@Command(name = "greeting", mixinStandardHelpOptions = true)
public class GreetingCommand implements Runnable {

    @Parameters(paramLabel = "<name>", defaultValue = "picocli",
        description = "Your name.")
    String name;

    @Override
    public void run() {
        System.out.printf("Hello %s, go go commando! %d \n", name, System.currentTimeMillis());
        var name = "noixxx";
        var greeter = Greeter.Builder.create()
            .greetee(name)
            .build();
        var greeting = greeter.greet();
        System.out.println(greeting);
    }

}
