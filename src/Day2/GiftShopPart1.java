package Day2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class GiftShopPart1 {


    public static long sumInvalidId (String[] input) {
        long sum = 0;
        for (String s : input) {
            sum += findInvalidId(s);
        }
        return sum;
    }

    public static long findInvalidId (String ranges) {
        String start = getStart(ranges);
        String end = getEnd(ranges);
        if (isEven(start) && isEven(end) && Long.parseLong(start) < Long.parseLong(end)) {
            long firstHalfOfStart = Long.parseLong(start.substring(0, start.length()/2));
            long secondHalfOfStart = Integer.parseInt(start.substring(start.length()/2));
            long firstHalfOfEnd =  Long.parseLong(end.substring(0,end.length()/2));
            long secondHalfOfEnd=  Long.parseLong(end.substring(end.length()/2));
            long diff1 = firstHalfOfEnd - firstHalfOfStart;
            if (diff1 > 0 && secondHalfOfEnd < firstHalfOfEnd && secondHalfOfStart < firstHalfOfStart) {
                long result = 0;
                for (long i = 0; i < diff1; i++) {
                    long digits = (long) Math.log10(firstHalfOfStart + i) + 1;
                    result += (firstHalfOfStart + i) * (long) Math.pow(10, digits) + (firstHalfOfStart + i);
                }
                return result;
            }
            else if (diff1 > 0 && secondHalfOfEnd >= firstHalfOfEnd && secondHalfOfStart < firstHalfOfStart) {
                long result = 0;
                for (long i = 0; i < diff1+1; i++) {
                    long digits = (long) Math.log10(firstHalfOfStart + i) + 1; // Finds that 8143 has 4 digits
                    result += (firstHalfOfStart + i) * (long) Math.pow(10, digits) + (firstHalfOfStart + i);
                }
                return result;
            }

            else if (diff1 > 0 && secondHalfOfEnd < firstHalfOfEnd &&  secondHalfOfStart > firstHalfOfStart) {
                long result = 0;
                for (long i = 1; i < diff1; i++) {
                    long digits = (long) Math.log10(firstHalfOfStart + i) + 1; // Finds that 8143 has 4 digits
                    result += (firstHalfOfStart + i) * (long) Math.pow(10, digits) + (firstHalfOfStart + i);
                }
                return result;
            }

            else if (diff1 > 0 && secondHalfOfEnd > firstHalfOfEnd &&  secondHalfOfStart > firstHalfOfStart) {
                long result = 0;
                for (long i = 1; i < diff1+1; i++) {
                    long digits = (long) Math.log10(firstHalfOfStart + i) + 1; // Finds that 8143 has 4 digits
                    result += (firstHalfOfStart + i) * (long) Math.pow(10, digits) + (firstHalfOfStart + i);
                }
                return result;
            }

            else if (diff1 == 0 && secondHalfOfEnd < firstHalfOfEnd) {
                return 0;
            }
            else {
                long digits = (long) Math.log10(firstHalfOfStart) + 1;
                return (firstHalfOfStart) * (long) Math.pow(10, digits) + (firstHalfOfStart);
            }
        }
        else if (isEven(end) && !isEven(start)) {
            long a = 1;
            long startInt = Integer.parseInt(start);
            while (a <= startInt) {
                a *= 10;
            }
            String newStart = String.valueOf(a);
            String newInput = newStart + "-" + end;
            return findInvalidId(newInput);
        }
        else if (isEven(start) && !isEven(end)) {
            long length = end.length();
            long newEnd = (long) Math.pow(10, length - 1) - 1;
            String newInput = start + "-" + newEnd;
            return findInvalidId(newInput);
        }
        else if (!isEven(start) && !isEven(end)) {
            long a = 1;
            long startInt = Integer.parseInt(start);
            while (a <= startInt) {
                a *= 10;
            }
            String newStart = String.valueOf(a);
            long length = end.length();
            long newEnd = (long) Math.pow(10, length - 1) - 1;
            String newInput = newStart + "-" + newEnd;
            return findInvalidId(newInput);
        }
        return 0;
    }


    public static boolean isEven (String ranges) {
        long length = ranges.length();
        return length % 2 == 0;
    }

    public static String getStart (String ranges) {
       String[] firstHalf = ranges.split("-");
       return firstHalf[0];
    }

    public static String getEnd (String ranges) {
        String[] secondHalf = ranges.split("-");
        return secondHalf[1];
    }

    static void main (String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("src/Day2/input.txt"))) {
            String line = br.readLine(); // Grabs the one long line
            if (line != null) {
                // Split the entire line into an array of range strings
                String[] allRanges = line.split(",");
                System.out.println(sumInvalidId(allRanges));
            }
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
        String test = "59-87";
        System.out.println(findInvalidId(test));
    }
}
