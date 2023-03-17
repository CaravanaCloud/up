package up;

import io.quarkus.test.junit.QuarkusTest;
import org.junit.jupiter.api.Test;

import javax.inject.Inject;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@QuarkusTest
public class ParserTest {

    @Inject
    private Parser parser;

    @Test
    void testBashStyleComment() {
        String content = "# assertion: This is a bash-style comment";
        List<Doclet> doclets = parser.parse(content);
        assertEquals(1, doclets.size());
        assertEquals("assertion", doclets.get(0).type());
        assertEquals("This is a bash-style comment", doclets.get(0).value());
    }

    @Test
    void testJavaStyleComment() {
        String content = "// wait: This is a Java-style comment";
        List<Doclet> doclets = parser.parse(content);
        assertEquals(1, doclets.size());
        assertEquals("wait", doclets.get(0).type());
        assertEquals("This is a Java-style comment", doclets.get(0).value());
    }

    @Test
    void testJavaBlockComment() {
        String content = "/* assertion: This is a Java-style comment */";
        List<Doclet> doclets = parser.parse(content);
        assertEquals(1, doclets.size());
        assertEquals("This is a Java-style comment", doclets.get(0).value());
    }

    @Test
    void testXmlStyleComment() {
        String content = "<!-- assertion: This is an XML-style comment -->";
        List<Doclet> doclets = parser.parse(content);
        assertEquals(1, doclets.size());
        assertEquals("This is an XML-style comment", doclets.get(0).value());
    }

    @Test
    void testNoKeywordInComment() {
        String content = "// This comment does not have a keyword";
        List<Doclet> doclets = parser.parse(content);
        assertEquals(0, doclets.size());
    }

    @Test
    void testMultipleDoclets() {
        String content = "/* waiter: This is a multi-line comment */\n"
                + "/* variable: Another comment */\n"
                + "// assertion: This is a Java-style comment\n"
                + "<!-- before: This is an XML-style comment -->\n"
                + "// This comment does not have a keyword";
        List<Doclet> doclets = parser.parse(content);
        assertEquals(4, doclets.size());

        assertEquals("This is a multi-line comment", doclets.get(0).value());
        assertEquals("Another comment", doclets.get(1).value());
        assertEquals("This is a Java-style comment", doclets.get(2).value());
        assertEquals("This is an XML-style comment", doclets.get(3).value());
    }
}
