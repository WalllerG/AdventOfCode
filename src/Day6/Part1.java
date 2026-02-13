package Day6;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import advent.util.Util;

public class Part1 {
    public static void main(String[] args) throws IOException {

        List<String> lines = Util.readInput(true,6);
        List<List<String>> list = new ArrayList<>();
        for (int i = 0; i < lines.size(); i++) {
            List<String> row = getRow(lines.get(i));
            list.add(row);
        }
        System.out.println(list);
        long result = 0;
        for  (int i = 0; i < list.getFirst().size(); i++) {
            String operation = list.get(list.size()-1).get(i);
            long time = 1;
            long add = 0;
            for (int j = 0; j < list.size()-1; j++) {
                if (operation.equals("+")) {
                    add +=  Long.parseLong(list.get(j).get(i));
                }
                else if (operation.equals("*")) {
                    time *= Long.parseLong(list.get(j).get(i));
                }
            }
            if (operation.equals("+")) {
                time = 0;
            }
            result += add;
            result += time;
        }
        System.out.println(result);

      }

     public static List<String> getRow (String input) {
        String[] nums = input.split(" ");
        List<String> list = new ArrayList<>();
        outer:
         for (String num : nums) {
             if (num.isEmpty()) {
                 continue outer;
             } else {
                 list.add(num);
             }
         }
        return list;
     }
}
