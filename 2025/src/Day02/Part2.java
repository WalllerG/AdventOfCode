package Day2;

import advent.util.Util;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Part2 {
    public static void main(String[] args) throws IOException {
        List<String> lines = Util.readInput(true, 2);

        for(String line : lines){
            String[] input = line.split(",");
            System.out.println(sumUp(input));
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
        String start = Part1.getStart(input);
        String end = Part1.getEnd(input);
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
