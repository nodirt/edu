import java.io.PrintWriter;
import java.util.*;

public class Program {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        new Program().solve(in, out);
        
        out.flush();
    }



    boolean find(int[] array, int x, int start) {
        int lo = start;
        int hi = array.length - 1;

        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (array[mid] == x) {
                return true;
            } else if (x < array[mid]) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }

        return array[lo] == x;
    }
    void solve(Scanner in, PrintWriter out) {
        int n = in.nextInt();
        int[] squares = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            squares[i] = i * i;
        }

        int count = 0;
        for (int a = 1; a <= n; a++) {
            for (int b = a + 1; b <= n; b++) {
                int c = squares[a] + squares[b];
                if (c > squares[squares.length - 1]) {
                    break;
                }

                int c2 = (int) Math.sqrt(c);
                if (c2 * c2 == c) {
                    count++;
                }
            }
        }

        out.println(count);
    }
}
