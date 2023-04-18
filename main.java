///usr/bin/env jbang "$0" "$@" ; exit $?
//DEPS io.quarkus.platform:quarkus-bom:2.16.6.Final@pom
//DEPS io.quarkus.platform:quarkus-arc:2.16.6.Final
//DEPS io.quarkus.platform:quarkus-picocli:2.16.6.Final

import io.quarkus.runtime.Quarkus;
import io.quarkus.runtime.annotations.QuarkusMain;
import up.Up;

@QuarkusMain
public class Main {
    public static void main(String[] args) {
        Quarkus.run(Up.class, args);
    }
}
