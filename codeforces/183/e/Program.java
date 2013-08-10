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
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = in.nextInt();
        }

        int lim = 1000000;
        int[] diff = new int[lim + 1];
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                diff[Math.abs(a[i] - a[j])]++;
            }
        }
        
        boolean[] occur = new boolean[10000000];
        int primeCount = 0;

        mLoop:
        for (int m = Math.min(1, n - k);; m++) {
            for (int i = 0; i < m; i++) {
                occur[i] = false;
            }

            int same = 0;
            for (int i = 0; i < n; i++) {
                int x = a[i] % m;
                if (!occur[x]) {
                    occur[x] = true;
                } else {
                    if (++same > k) {
                        continue mLoop;
                    }
                }
            }

            out.println(m);
            break;
        }
    }
}
