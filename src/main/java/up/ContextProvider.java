package up;

import org.graalvm.polyglot.Context;

import javax.enterprise.inject.Produces;

public class ContextProvider {
    @Produces
    public Context produce(){
        return Context.create();
    }
}

