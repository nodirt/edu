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
        if (n % 2 == 0) {
            out.println(-1);
            return;
        }

        for (int j = 0; j < 2; j++) {
            for (int i = 0; i < n; i++) {
                out.print(i);
                out.print(' ');
            }
            out.println();
        }

        for (int i = 0, j = 0; i < n; i++, j += 2) {
            out.print(j % n);
            out.print(' ');
        }
        out.println();
    }
}
