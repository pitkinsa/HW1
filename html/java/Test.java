import java.util.*;
import java.io.*;
public class Test{

    public static void main(String[] args) {
        // Prints "Hello, World" to the terminal window.
        
	System.out.println(cgi_lib.Header());	
	System.out.println("Content-Type: test/html;charset=utf-8\n\n\nHello, World");
        
    }

}
