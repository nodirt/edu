import java.io.PrintWriter;
import java.util.*;

public class Program {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        new Program().solve(in, out);
        
        out.flush();
    }


    int n;
    int[][] map;
    int[] maxLen;
    int[][][] path;

    boolean isValid(int coord) {
        return coord >= 0 && coord < n;
    }
    void calcPath(int x, int y, int dir, int x2, int y2) {
        int len = isValid(x2) && isValid(y2) && map[y][x] == map[y2][x2]
            ? path[y2][x2][dir] + 1 
            : 1;

        path[y][x][dir] = len;
    }

    void solve(Scanner in, PrintWriter out) {
        n = Integer.parseInt(in.nextLine());
        map = new int[2][n];
        maxLen = new int[2];
        path = new int[2][n][4];

        for (int y0 = 0, y = 0; y0 < n; y0++) {
            String line = in.nextLine();
            for (int x = 0; x < n; x++) {
                int code = line.charAt(x) == 'S' ? 0 : 1;
                map[y][x] = code;

                calcPath(x, y, 0, x - 1, y);
                calcPath(x, y, 1, x - 1, y - 1);
                calcPath(x, y, 2, x, y - 1);
                calcPath(x, y, 3, x + 1, y - 1);
                for (int len : path[y][x]) {
                    maxLen[code] = Math.max(len, maxLen[code]);
                }
            }

            assert y == 0 || y == 1;

            if (y == 1) {
                int[] tmp = map[0];
                map[0] = map[1];
                map[1] = tmp;

                int[][] tmp2 = path[0];
                path[0] = path[1];
                path[1] = tmp2;
            } else {
                y++;
            }
        }

        if (maxLen[0] == maxLen[1]) {
            out.println("?");
        } else {
            out.println(maxLen[0] > maxLen[1] ? "S" : "s");
        }

        out.println(Math.max(maxLen[0], maxLen[1]));
    }
}
