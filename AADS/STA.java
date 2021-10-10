import java.util.*;

public class STA {
    public static void main(String args[])
    {
        String str = "GeeksForGeeks";
  
        // Creating array of string length
        char[] ch = new char[str.length()];
  
        // Copy character by character into array
        for (int i = 0; i < str.length(); i++) {
            ch[i] = str.charAt(i);
        }
  
        // Printing content of array
        for (char c : ch) {
            System.out.println(c);
        }
    }
}