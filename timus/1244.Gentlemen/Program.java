import java.io.PrintWriter;
import java.util.*;

public class Program {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		
		int packWeight = in.nextInt();
		int n = in.nextInt();
		int[] weights = new int[n];
		for (int i = 0; i < n; i++) {
			weights[i] = in.nextInt();
		}
		
		int[][] solution_count = new int[packWeight + 1][n + 1];
		boolean[][] included = new boolean[packWeight + 1][n + 1];
		for (int i = 0; i < n; i++) {
			solution_count[0][i] = 1;
		}

		for (int weight = 1; weight <= packWeight; weight++) {
			for (int i = 0; i < n; i++) {
				int cardWeight = weights[i];
				int with_me = cardWeight <= weight 
						? solution_count[weight - cardWeight][i]
						: 0;
				int without_me = solution_count[weight][i];
				int sol_count = without_me + with_me;
				solution_count[weight][i + 1] = sol_count;
				included[weight][i + 1] = sol_count == 1 && with_me == 1;
			}
		}

		int sol_count = solution_count[packWeight][n];
		if (sol_count == 0) {
			out.println(0);
		} else if (sol_count > 1) {
			out.println(-1);
		} else {
			int count = 0;
			int[] excluded = new int[n];
			int weight = packWeight;
			for (int i = n - 1; i >= 0; i--) {
				if (included[weight][i + 1]) {
					weight -= weights[i];
				} else {
					excluded[count++] = i;
				}
			}

			while (count > 0) {
				out.print(excluded[--count] + 1);
				out.print(' ');
			}
		}
		
		out.flush();
	}
}
