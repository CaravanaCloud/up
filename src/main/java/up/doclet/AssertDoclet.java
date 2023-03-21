package up.doclet;

import org.slf4j.Logger;

import javax.enterprise.context.Dependent;
import javax.inject.Inject;
import javax.inject.Named;

@Dependent
@Named("assert")
public class AssertDoclet implements DocletProcessor {
    @Inject
    Logger log;

    @Override
    public void accept(String s) {
        log.info("[doclet] assert: " + s);
        //TODO: Execute the command and shutdown if it fails
        //TODO: Consider return type for DocletProcessor
    }
}
