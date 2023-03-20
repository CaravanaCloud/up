package up.doclet;

import javax.inject.Inject;
import javax.inject.Named;
import java.util.logging.Logger;

@Named("assert")
public class AssertDoclet implements DocletProcessor {
    @Inject
    Logger log;

    @Override
    public void accept(String s) {
        log.info("[doclet] assert: " + s);
    }
}
