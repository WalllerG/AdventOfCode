package Day3;

import advent.util.Util;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;

public class Part1 {
    static void main() throws IOException{
        List<String> lines = Util.readInput(true, 3);

        int sum = 0;
        for(String line : lines){
            sum += getVoltage(line);
        }
        System.out.println(sum);
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
