package up;

import io.quarkus.runtime.QuarkusApplication;

public class Up implements QuarkusApplication {
    
    @Override
    public int run(String... args){

        System.out.println("Starting up cli, thank you for running!");
        return 0;
    
    }

}