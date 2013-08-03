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
    int[][] black = new int[100][101];
    int[][] white = new int[100][101];

    void readInput(Scanner in) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                black[i][j + 1] = black[i][j];
                white[i][j + 1] = white[i][j];
                if (in.nextInt() == 1) {
                    black[i][j + 1]++;
                } else {
                    white[i][j + 1]++;
                }
            }
        }
    }

    int whiteWidth(int row, int col, int width) {
        int blackAmount = black[row][col + width] - black[row][col];
        int whiteAmount = width - blackAmount;
        if (blackAmount % 2 != 0) {
            return 0;
        }


        int whiteStart = col + blackAmount / 2;
        int middleWhite = white[row][whiteStart + whiteAmount] - white[row][whiteStart];
        return whiteAmount == middleWhite ? whiteAmount : 0;
    }

    boolean test(int row, int col, int side) {
        for (int w = 1; w <= side; w += 2) {
            if (whiteWidth(row++, col, side) != w) return false;
        }

        for (int w = side - 2; w >= 1; w -= 2) {
            if (whiteWidth(row++, col, side) != w) return false;
        }

        return true;
    }

    boolean testCase(Scanner in, PrintWriter out) {
        n = in.nextInt();
        if (n == 0) return false;
        readInput(in);

        int biggestPossibleSize = n;
        if (biggestPossibleSize % 2 == 0) {
            biggestPossibleSize--;
        }

        for (int side = biggestPossibleSize; side >= 3; side -= 2) {
            int maxCoord = n - side;

            for (int row = 0; row <= maxCoord; row++) {
                for (int col = 0; col <= maxCoord; col++) {

                    if (test(row, col, side)) {
                        out.println(side);
                        return true;
                    }

                }
            }
        }

        out.println("No solution");
        return true;
    }

    void solve(Scanner in, PrintWriter out) {
        while (testCase(in, out)) {
        }
    }
}
