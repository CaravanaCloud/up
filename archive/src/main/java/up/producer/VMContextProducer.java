package up.producer;

import org.graalvm.polyglot.Context;

import javax.enterprise.inject.Produces;

public class VMContextProducer {
    @Produces
    public Context produce(){
        return Context.create();
    }
}

