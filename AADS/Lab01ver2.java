//***********************
//Name : Poon King Fung
//SID: 2011 8523
//***********************

import java.util.Scanner;

public class Lab01ver2 { 
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("\nPlease input a word: ");
		String word = input.nextLine();
		word = word.toUpperCase();
		String reverse = "";
		
		for (int i = word.length() - 1; i>=0 ;i--) {
			reverse += word.charAt(i);
            System.out.println(reverse);		
		}
		
        boolean palindrome = true;
        for (int i = 0;  i < word.length(); i++) {
            if (word.charAt(i) != reverse.charAt(i)) {
                palindrome = false;
            }
        }

		if (palindrome) {
			System.out.println("This is a Palindrome!");			
		}
		else {
			System.out.println("This isn't a Palindrome");
		}
	}
}