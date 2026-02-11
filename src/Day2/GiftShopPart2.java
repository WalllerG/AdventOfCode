package Day2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class GiftShopPart2 {
    public static void main(String[] args) {

        try (BufferedReader br = new BufferedReader(new FileReader("src/Day2/input.txt"))) {
            String line = br.readLine(); // Grabs the one long line
            if (line != null) {
                // Split the entire line into an array of range strings
                String[] allRanges = line.split(",");
                System.out.println(sumUp(allRanges));
            }
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
    public static long sumUp(String[] ranges) {
        long sum = 0;
        for (String range : ranges) {
            sum += findInvalidIdPro(range);
        }
        return sum;
    }

    public static long findInvalidIdPro(String input) {
        String start = GiftShopPart1.getStart(input);
        String end = GiftShopPart1.getEnd(input);
        long startNum = Long.parseLong(start);
        long endNum = Long.parseLong(end);
        long result = 0;
        for (long i = startNum; i <= endNum; i++) {
            if (isInvalidId(i)) {
                result += i;
            }
        }
        return result;
    }

    public static boolean isInvalidId(long num) {
        String s = String.valueOf(num);
        ArrayList<Integer> list = new ArrayList<>();
        boolean flag = true;
        for  (int i = 1; i < s.length(); i++) {
            if (s.length() % i == 0) {
                list.add(i);
            }
        }
        for  (int i = 0; i < list.size(); i++) {
            String comb = s.substring(0, list.get(i));
            int times = s.length() / list.get(i);
            for (int j = 1; j < times; j++) {
                String s1 = s.substring(list.get(i) * j, list.get(i) * j + list.get(i));
                if  (!s1.equals(comb)) {
                    flag = false;
                    break;
                }
                flag = true;
            }
            if  (flag) {
                return true;
            }
        }
        return false;
    }
}
