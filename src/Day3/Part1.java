package Day3;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Part1 {
    static void main() {
        try (BufferedReader br = new BufferedReader(new FileReader("src/Day3/input.txt"))) {
            String line;
            int result = 0;
            while ((line = br.readLine()) != null) {
                result += getVoltage(line);
            }
            System.out.println(result);
        } catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
        }
        String a = "123456";
    }

    public static int getVoltage (String input) {
        int length = input.length();
        int largest = 0;
        int secondLargest = 0;
        int index = 0;
        for  (int i = 0; i < length-1; i++) {
            String s = input.substring(i, i+1);
            if (Integer.parseInt(s) > largest) {
                largest = Integer.parseInt(s);
                index = i;
            }
        }
        for (int i = index+1; i < length; i++) {
            String s = input.substring(i, i+1);
            if (Integer.parseInt(s) > secondLargest) {
                secondLargest = Integer.parseInt(s);
            }
        }
        return  largest * 10 + secondLargest;
    }
}
