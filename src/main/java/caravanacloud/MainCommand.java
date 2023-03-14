package caravanacloud;

import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import picocli.CommandLine.Command;
import picocli.CommandLine.Parameters;

import javax.inject.Inject;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

@Command(name = "main", mixinStandardHelpOptions = true)
public class MainCommand implements Runnable {
    @Inject
    Context context;

    Logger log = LoggerFactory.getLogger(MainCommand.class);

    @Parameters(index = "0")
    String subject;

    @Override
    public void run() {
        System.out.println("Up!");
        log.info("^ {}", subject);
        try {
            execute(subject);            
        }catch (Exception ex){
            System.out.println("Failed to run script: " + ex.getMessage());
        }
    }

    private void tryExecute(String dir, String fileName) throws IOException{
        var file = new File(dir, fileName);
        if (file.exists()){
            execute(file);
        }else {
            log.trace("File does not exist ", fileName);
        }
    }

    private void execute(String subject) throws IOException {
        var dir = "./scripts/"+subject; //TODO: possible parameter dir
        //TODO: try only found files 
        tryExecute(dir, "main.py");
        tryExecute(dir, "main.js");
        tryExecute(dir, "main.sh");
    }
    
    private void execute(String dir, String fileName) throws IOException {
        var file = new File(dir, fileName);
        execute(file);
    }
    private void execute(File file) throws IOException {
        var lang = Source.findLanguage(file);
        log.info("Found language {} for script {}", lang, file.getName());
        if (lang == null){
            if (file.getName().endsWith(".sh")){
                execShell(file.getAbsolutePath());
            }else {
                throw new RuntimeException("Unsupported language: " + lang);
            }
        }
        else switch (lang){
            case "js", "python" -> executeGraalVM(lang, file);            
            default -> throw new RuntimeException("Unsupported language: " + lang);
        }
    }

    private void executeGraalVM(String lang, File file) throws IOException {
        var src = Source.newBuilder(lang, file).build();
        context.eval(src);
    }


    public static void execShell(String scriptPath) {
        try {
            // Create the process builder with the script path and any arguments
            ProcessBuilder builder = new ProcessBuilder(scriptPath);

            // Start the process and read its output
            Process process = builder.start();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // Wait for the process to complete
            int exitCode = process.waitFor();
            System.out.println("Process exited with code " + exitCode);

        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

}
