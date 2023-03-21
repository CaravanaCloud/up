package up.parser;

import up.doclet.Doclet;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import javax.enterprise.context.ApplicationScoped;

@ApplicationScoped
public class Parser {
    private static final String[] COMMENT_DELIMITERS = {"//", "#", "/*", "*/", "<!--", "-->"};
    private static final String[] DOCLET_DELIMITERS = {":", " :"};

    public List<Doclet> parse(String content) {
        var lines = content.split("\n");
        var doclets = Arrays.stream(lines)
                .map(this::parseCommentLine)
                .filter(Optional::isPresent)
                .map(Optional::get)
                .toList();
        return doclets;
    }

    private Optional<Doclet> parseCommentLine(String line) {
        var trimmedLine = line.trim();
        if (!isComment(trimmedLine)) {
            return Optional.empty();
        }
        var comment = trimmedLine;
        for (var delimiter : COMMENT_DELIMITERS) {
            comment = comment.replace(delimiter, "");
        }
        comment = comment.trim();
        for (var delimiter : DOCLET_DELIMITERS) {
            var index = comment.indexOf(delimiter);
            if (index != -1) {
                var key = comment.substring(0, index).trim();
                var value = comment.substring(index + delimiter.length()).trim();
                return Optional.of(new Doclet(key, value));
            }
        }
        return Optional.empty();
    }

    private boolean isComment(String line) {
        for (var delimiter : COMMENT_DELIMITERS) {
            if (line.startsWith(delimiter)) {
                return true;
            }
        }
        return false;
    }

    public static String fileToString(File file) throws IOException {
        Path filePath = file.toPath();
        byte[] fileBytes = Files.readAllBytes(filePath);
        return new String(fileBytes, StandardCharsets.UTF_8);
    }
    public List<Doclet> parse(File file) throws IOException {
        var content = Parser.fileToString(file);
        var result = parse(content);
        return result;
    }
}
