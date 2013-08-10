import java.io.PrintWriter;
import java.util.*;

public class Program {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        new Program().solve(in, out);
        
        out.flush();
    }

    int gcd(int x, int y) {
        if (y == 0) {
            return x;
        }
        return gcd(y, x % y);
    }

    void solve(Scanner in, PrintWriter out) {
        long maxX = in.nextLong();
        long maxY = in.nextInt();
        long x = in.nextInt();
        long y = in.nextInt();

        int a = in.nextInt();
        int b = in.nextInt();

        int d = gcd(a, b);
        a /= d;
        b /= d;
        long t = Math.min(maxX / a, maxY / b);

        long width = a * t;
        long height = b * t;

        long x2 = Math.min(maxX, x + width / 2);
        long x1 = Math.max(0, x2 - width);
        x2 = x1 + width;

        long y2 = Math.min(maxY, y + height / 2);
        long y1 = Math.max(0, y2 - height);
        y2 = y1 + height;

        out.printf("%d %d %d %d", x1, y1, x2, y2);
    }
}
