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
        int horses = in.nextInt();
        int stables = in.nextInt();
        int[] black = new int[horses + 1];
        for (int i = 1; i <= horses; i++) {
            black[i] = black[i - 1];
            if (in.nextInt() == 0) {
                black[i]++;                
            }
        }

        long uh[][] = new long[horses + 1][stables + 1];

        for (int n = 1; n <= horses; n++) {
            for (int s = 1; s <= Math.min(stables, n); s++) {
                uh[n][s] = Integer.MAX_VALUE;
                int minHorses = s == 1 ? n : 1;
                int maxHorses = n - s + 1;
                assert minHorses <= maxHorses;
                for (int m = minHorses; m <= maxHorses; m++) {
                    long blacks = black[n] - black[n - m];
                    long whites = m - blacks;
                    long unhappiness = uh[n - m][s - 1] + blacks * whites;
                    uh[n][s] = Math.min(unhappiness, uh[n][s]);
                }
            }
        }

        out.println(uh[horses][stables]);
    }
}
