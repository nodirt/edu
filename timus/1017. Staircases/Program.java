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

        long[][] dp = new long[n + 1][n + 1];
        for (int h = 0; h <= n; h++) {
            dp[0][h] = 1;
        }
        for (int m = 1; m <= n; m++) {
            for (int h = 1; h <= n; h++) {
                dp[m][h] = dp[m][h - 1];
                if (h <= m) {
                    dp[m][h] += dp[m - h][h - 1];
                }
            }
        }

        out.println(dp[n][n - 1]);
    }
}
