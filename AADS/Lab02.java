//***********************
//Name : Poon King Fung
//SID: 2011 8523
//***********************

import java.util.*;

public class Lab02 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Stack<Character> stack = new Stack<Character>();
        int i;

		System.out.print("\nPlease input a word: ");
		String word = input.nextLine();
		word = word.toUpperCase();
        
        for ( i = 0; i < word.length(); i++) {
            stack.push(word.charAt(i));
        }

        boolean palindrome = true;
        for ( i = 0; i < word.length(); i++){
            if (word.charAt(i) != stack.pop()) {
                palindrome = false;
            }
        }

		if (palindrome) {
			System.out.println("This is a Palindrome!");			
		}
		else {
			System.out.println("This isn't a Palindrome");
		}

        input.close();
    }
}