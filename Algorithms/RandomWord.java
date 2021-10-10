import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        String chmapion = "";
        String temp = "";
        for (double i = 1; !StdIn.isEmpty(); i++) {
            temp = StdIn.readString();
            if (StdRandom.bernoulli(1 / i)) {
                chmapion = temp;
            }
        }

        StdOut.println(chmapion);
    }

}
