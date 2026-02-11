package Day3;

import advent.util.Util;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;

public class Part2 {
    static void main() throws IOException{
        List<String> lines = Util.readInput(true, 3);

        long result = 0;
        for(String line : lines){
            result += Long.parseLong(getVoltage(line, 12, 100));
        }
        System.out.println(result);
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
