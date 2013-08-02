import java.io.PrintWriter;
import java.util.*;

public class Program {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        new Program().solve(in, out);
        
        out.flush();
    }


    int latinLimit, nonLatinLimit;
    String line;

    int[] cache;
    int[] len;
    int[] latin;
    int tokenCount;

    int minSms(int last) {
        if (last < 0) return 0;

        if (cache[last] != -1) {
            return cache[last];
        }

        int min = minSms(last - nonLatinLimit);

        int latinCount = latin[last + 1];
        // for (int i = 0; i < latinCount; i++) {
        //     assert isLatin(line.charAt(last - i));
        // }

        if (latinCount > 0) {
            min = Math.min(min, minSms(last - Math.min(latinCount, latinLimit)));
        }

        min++;
        cache[last] = min;
        return min;
    }

    boolean isLatin(char c) {
        return c == ' ' || Character.isLetter(c);
    }

    void solve(Scanner in, PrintWriter out) {
        nonLatinLimit = in.nextInt();
        latinLimit = in.nextInt();

        in.nextLine();
        line = in.nextLine();
        latin = new int[line.length() + 1];
        for (int i = 0; i < line.length(); i++) {
            if (isLatin(line.charAt(i))) {
                latin[i + 1] = latin[i] + 1;
            }
        }

        int n = line.length();
        cache = new int[n];
        for (int i = 0; i < n; i++) {
            cache[i] = -1;
        }

        out.println(minSms(n - 1));
    }
}
