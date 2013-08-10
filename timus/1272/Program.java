import java.io.PrintWriter;
import java.util.*;

public class Program {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        new Program().solve(in, out);
        
        out.flush();
    }

    class Island {
        ArrayList<Island> tunnels = new ArrayList<Island>();
        ArrayList<Island> bridges = new ArrayList<Island>();
        boolean visited;

        ArrayList<Island> getList(boolean bridges) {
            return bridges ? this.bridges : this.tunnels;
        }
    }

    Island[] islands;

    void readEdges(Scanner in, int count, boolean bridges) {
        for (int i = 0; i < count; i++) {
            Island land1 = islands[in.nextInt() - 1];
            Island land2 = islands[in.nextInt() - 1];
            land1.getList(bridges).add(land2);
            land2.getList(bridges).add(land1);
        }
    }

    void solve(Scanner in, PrintWriter out) {
        int n = in.nextInt();
        int k = in.nextInt();
        int m = in.nextInt();

        islands = new Island[n];
        for (int i = 0; i < n; i++) {
            islands[i] = new Island();
        }

        readEdges(in, k, false);
        readEdges(in, m, true);

        int bridgesUsed = 0;
        Queue<Island> bfs = new LinkedList<Island>();
        Queue<Island> candidates = new LinkedList<Island>();
        Island nextRoot = islands[0];
        while (nextRoot != null) {
            bfs.add(nextRoot);
            nextRoot = null;

            while (!bfs.isEmpty()) {
                Island land = bfs.remove();
                land.visited = true;
                
                for (Island other : land.tunnels) {
                    if (!other.visited) {
                        bfs.add(other);
                    }
                }

                for (Island other : land.bridges) {
                    if (!other.visited) {
                        candidates.add(other);
                    }
                }
            }

            while (!candidates.isEmpty()) {
                Island land = candidates.remove();
                if (!land.visited) {
                    nextRoot = land;
                    bridgesUsed++;
                    break;
                }
            }
        }

        out.println(bridgesUsed);
    }
}
