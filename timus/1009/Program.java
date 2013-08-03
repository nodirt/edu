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
        int k = in.nextInt();

        int withZero = 1;
        int withoutZero = 0;
        for (int m = 1; m <= n; m++) {
            int wt = withoutZero;
            int wo = (withZero  + withoutZero) * (k - 1);
            withZero = wt;
            withoutZero = wo;
        }

        out.println(withZero + withoutZero);
    }
}
