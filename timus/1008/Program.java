import java.io.PrintWriter;
import java.util.*;

public class Program {
    Scanner in = new Scanner(System.in);
    PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) {
        new Program().run();
    }

    void run() {
        solve();
        out.flush();
    }

    static final int LEFT = 0;
    static final int TOP = 1;
    static final int RIGHT = 2;
    static final int BOTTOM = 3;

    static final String[] dirName = { "R", "T", "L", "B" };
    static final int[][] dirDelta = { {1, 0}, {0, 1}, {-1, 0}, {0, -1} };

    class Node {
        int x;
        int y;
        boolean visited;

        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }

        Node[] nodes = new Node[4];

        @Override
        public String toString() {
            return x + " " + y;
        }
    }

    Node readCoords() {
        return new Node(in.nextInt(), in.nextInt());
    }

    Node[][] nodes = new Node[12][12];

    void coordsToDirs(int n) {
        Node root = null;
        for (int i = 0; i < n; i++) {
            Node node = readCoords();
            if (root == null) {
                root = node;
            }

            nodes[node.x][node.y] = node;
        }

        out.println(root.toString());

        Queue<Node> bfs = new LinkedList<Node>();
        bfs.add(root);
        while (!bfs.isEmpty()) {
            Node node = bfs.remove();
            node.visited = true;

            for (int dir = 0; dir < 4; dir++) {
                int[] delta = dirDelta[dir];
                Node other = nodes[node.x + delta[0]][node.y + delta[1]];
                if (other == null || other.visited) continue;
                other.visited = true;
                bfs.add(other);
                out.print(dirName[dir]);
            }
            out.println(bfs.isEmpty() ? ". " : ",");
        }
    }

    void dirsToCoords(Node root) {
        nodes[root.x][root.y] = root;
        Queue<Node> bfs = new LinkedList<Node>();
        bfs.add(root);

        int count = 0;

        while (!bfs.isEmpty()) {
            Node node = bfs.remove();
            count++;

            String line = in.nextLine();

            for (int i = 0; i < line.length() - 1; i++) {
                char c = line.charAt(i);

                int d = 0;
                while (dirName[d].charAt(0) != c) {
                    d++;
                }

                Node other = new Node(node.x + dirDelta[d][0], node.y + dirDelta[d][1]);
                assert nodes[other.x][other.y] == null;
                nodes[other.x][other.y] = other;
                bfs.add(other);
            }

        }

        out.println(count);

        for (int x = root.x; x <= 10; x++) {
            for (int y = 1; y <= 10; y++) {
                if (nodes[x][y] != null) {
                    out.printf("%d %d\n", x, y);
                }
            }
        }
    }

    void solve() {
        String line = in.nextLine();
        String[] parts = line.split(" ");

        if (parts.length == 2) {
            dirsToCoords(new Node(Integer.parseInt(parts[0]), Integer.parseInt(parts[1])));
        } else {
            assert parts.length == 2;
            int n = Integer.parseInt(parts[0]);
            coordsToDirs(n);
        }
    }
}
