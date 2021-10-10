import java.util.Scanner;

public class palindromecheck {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Please input a word:");
        String word = input.nextLine();
        String reverse = "";
        for (int i = word.length() - 1; i >= 0; i--) {
            reverse += word.charAt(i);
        }
        if (word.equals(reverse)) {
            System.out.println("Is palindrome.");
        } else {
            System.out.println("Not Is palindrome.");
        }
        input.close();
    }
}
