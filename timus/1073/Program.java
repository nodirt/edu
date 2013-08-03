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

        int[] q = new int[n];
        int qc = 0;
        while (true) {
            int xx = (qc + 1) * (qc + 1);
            if (xx > n) break;
            q[qc++] = xx;
        }

        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {

            dp[i] = Integer.MAX_VALUE;

            for (int x : q) {
                if (x > i) break;
                dp[i] = Math.min(dp[i], dp[i - x]);
            }
            dp[i]++;
        }

        out.println(dp[n]);
    }
}
