package Day3;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Part2 {
    static void main() {
        try (BufferedReader br = new BufferedReader(new FileReader("src/Day3/input.txt"))) {
            String line;
            long result = 0;
            while ((line = br.readLine()) != null) {
                result += Long.parseLong(getVoltage(line, 12,100));
            }
            System.out.println(result);
        } catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
        }

    }
    public static String getVoltage (String input, int numsNeeded, int numsLeft) {
        if  (numsNeeded == 0) {
            return "";
        }
        String result;
        int largest = 0;
        int index = 0;
        int limit = numsLeft - numsNeeded + 1;
        for  (int i = 0; i < limit; i++) {
            String s = input.substring(i, i+1);
            if (Integer.parseInt(s) > largest) {
                largest = Integer.parseInt(s);
                index = i;
            }
        }
        result = String.valueOf(largest);
        return  result + getVoltage(input.substring(index + 1), numsNeeded-1, numsLeft-(index+1));
    }
}
