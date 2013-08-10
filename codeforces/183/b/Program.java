import java.io.PrintWriter;
import java.util.*;

public class Program {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);

        new Program().solve(in, out);
        
        out.flush();
    }

    int[] months = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

    class Date {
        int year;
        int month;
        int day;

        int compareTo(Date other) {
            if (other.year != this.year) {
                return this.year - other.year;
            }
            if (other.month != this.month) {
                return this.month - other.month;
            }
            return this.day - other.day;
        }
    }

    Date parseDate(String text) {
        String[] parts = text.split(":");
        Date date = new Date();
        date.year = Integer.parseInt(parts[0]);
        date.month = Integer.parseInt(parts[1]);
        date.day = Integer.parseInt(parts[2]);
        return date;
    }

    boolean isLeapYear(int year) {
        if (year % 400 == 0) {
            return true;
        }
        if (year % 100 == 0) {
            return false;
        }

        if (year % 4 == 0) {
            return true;
        }

        return false;
    }

    long daysInMonth(int year, int month) {
        long days = months[month];
        if (month == 2 && isLeapYear(year)) {
            days++;
        }
        return days;
    }


    long daysBetween(int startYear, int endYear) {
        long count = 365 * (endYear - startYear);
        for (int y = startYear; y < endYear; y++) {
            if (isLeapYear(y)) {
                count++;
            }
        }

        return count;
    }

    long daysFromYearStart(Date date) {
        long days = 0;
        for (int m = 1; m < date.month; m++) {
            days += daysInMonth(date.year, m);
        }
        days += date.day;
        return days;
    }

    void solve(Scanner in, PrintWriter out) {
        Date start = parseDate(in.nextLine());
        Date end = parseDate(in.nextLine());
        if (start.compareTo(end) > 0) {
            Date tmp = start;
            start = end;
            end = tmp;
        }

        long days = daysBetween(start.year, end.year) - daysFromYearStart(start) + daysFromYearStart(end);
        out.println(days);
    }
}
