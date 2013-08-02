import java.io.PrintWriter;
import java.util.*;

public class Program {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        new Program().solve(in, out);
        
        out.flush();
    }


    void solve(Scanner in, PrintWriter out) {
        int n = in.nextInt();

        long[] white = new long[n + 1];
        white[0] = 1;

        for (int m = 1; m <= n; m++) {
            white[m] = white[m - 1];
            if (m - 2 > 0) {
                white[m] += white[m - 2];
            }
        }

        out.println(white[n] * 2);
    }
}
