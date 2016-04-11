import java.util.*;
import java.io.*;

class ex {

  public static void main( String args[] )
  {
      //
      //  Print the required CGI header.
      //
      System.out.println("Content-type: text/html\n\n");

      //
      // Create the Top of the returned HTML page
      //
	  String Top = "<html>\n";
	  Top+= "<head>\n";
	  Top+= "<title>\n";
	  Top+= "Hello world from java";
	  Top+= "\n";
	  Top+= "</title>\n";
	  Top+= "</head>\n";
	  Top+= "<body>\n";
	  System.out.println(Top);
	  System.out.println("Hello World from Java @"+ new Date());

      //
      // Create the Bottom of the returned HTML page to close it cleanly.
      //
      System.out.println("</body>\n</html>\n");

  }

}

