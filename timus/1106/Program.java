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
        int[][] adj = new int[n][n + 2];

        for (int i = 0; i < n; i++) {
            int j = 0;
            do {
                adj[i][j] = in.nextInt() - 1;
                j++;
            } while (adj[i][j - 1] != -1);

            if (j == 0) {
                out.println(0);
                return;
            }
        }

        int[] team = new int[n];
        int team1 = 0;
        Queue<Integer> bfs = new ArrayDeque<Integer>(n);
        for (int i = 0; i < n; i++) {
            if (team[i] != 0) continue;

            team[i] = 1;
            bfs.add(i);
            while (!bfs.isEmpty()) {
                int node = bfs.remove();
                assert team[node] != 0;
                if (team[node] == 1) {
                    team1++;
                }

                for (int j = 0;; j++) {
                    int friend = adj[node][j];
                    if (friend == -1) break;
                    if (team[friend] != 0) continue;
                    team[friend] = -team[node];
                    bfs.add(friend);
                }
            }
        }

        out.println(team1);
        boolean firstMember = true;
        for (int i = 0; i < n; i++) {
            assert team[i] != 0;
            if (team[i] != 1) continue;
            if (!firstMember) {
                out.print(" ");
            }
            out.print(i + 1);
            firstMember = false;
        }
    }
}
