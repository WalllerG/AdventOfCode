package Day4;

import advent.util.Util;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Part2 {
    static void main(String[] args) throws IOException {
        List<String> lines = Util.readInput(true,4);
        List<String[]> input = new ArrayList<>();
        for  (String line : lines) {
            String[] split = line.split("");
            input.add(split);
        }
        System.out.println(check(input));
    }

    public static int check( List<String[]> input) {
        int result = 0;
        List<int[]> toRemove = new ArrayList<>();
        for (int i = 0; i < input.size(); i++) {
            for  (int j = 0; j < input.get(i).length; j++) {
                int count = 0;
                if (input.get(i)[j].equals("@") && i != 0 && j != 0 && i != input.size()-1 && j != input.get(i).length-1) { // middle
                    if (input.get(i)[j+1].equals("@")) {
                        count++;
                    }
                    if (input.get(i)[j-1].equals("@")) {
                        count++;
                    }
                    if (input.get(i-1)[j+1].equals("@")) {
                        count++;
                    }
                    if (input.get(i-1)[j-1].equals("@")) {
                        count++;
                    }
                    if (input.get(i+1)[j+1].equals("@")) {
                        count++;
                    }
                    if (input.get(i+1)[j-1].equals("@")) {
                        count++;
                    }
                    if (input.get(i+1)[j].equals("@")) {
                        count++;
                    }
                    if (input.get(i-1)[j].equals("@")) {
                        count++;
                    }
                    if (count < 4) {
                        result++;
                        int[] index = new int[2];
                        index[0] = i;
                        index[1] = j;
                        toRemove.add(index);
                    }
                }

                else if (input.get(i)[j].equals("@") && i == 0 && j != input.get(i).length-1 && j != 0) { // first line without head and tail
                    if (input.get(i)[j+1].equals("@")) {
                        count++;
                    }
                    if (input.get(i)[j-1].equals("@")) {
                        count++;
                    }
                    if (input.get(i+1)[j+1].equals("@")) {
                        count++;
                    }
                    if (input.get(i+1)[j-1].equals("@")) {
                        count++;
                    }
                    if (input.get(i+1)[j].equals("@")) {
                        count++;
                    }
                    if (count < 4) {
                        result++;
                        int[] index = new int[2];
                        index[0] = i;
                        index[1] = j;
                        toRemove.add(index);
                    }
                }

                else if (input.get(i)[j].equals("@") && i != input.size()-1 && i != 0 && j == 0) { // first column without head and tail
                    if (input.get(i+1)[j].equals("@")) {
                        count++;
                    }
                    if (input.get(i-1)[j].equals("@")) {
                        count++;
                    }
                    if (input.get(i+1)[j+1].equals("@")) {
                        count++;
                    }
                    if (input.get(i-1)[j+1].equals("@")) {
                        count++;
                    }
                    if (input.get(i)[j+1].equals("@")) {
                        count++;
                    }
                    if (count < 4) {
                        result++;
                        int[] index = new int[2];
                        index[0] = i;
                        index[1] = j;
                        toRemove.add(index);
                    }
                }

                else if (input.get(i)[j].equals("@") && i == 0 && j == 0) { // left top coner
                    result++;
                    int[] index = new int[2];
                    index[0] = i;
                    index[1] = j;
                    toRemove.add(index);
                }

                else if (input.get(i)[j].equals("@") && i == input.size()-1 && j == 0) { // left bottom coner
                    result++;
                    int[] index = new int[2];
                    index[0] = i;
                    index[1] = j;
                    toRemove.add(index);

                }

                else if (input.get(i)[j].equals("@") && i == input.size()-1 && j != 0 && j != input.get(i).length-1) { // last line without head and tail
                    if (input.get(i)[j+1].equals("@")) {
                        count++;
                    }
                    if (input.get(i)[j-1].equals("@")) {
                        count++;
                    }
                    if (input.get(i-1)[j+1].equals("@")) {
                        count++;
                    }
                    if (input.get(i-1)[j-1].equals("@")) {
                        count++;
                    }
                    if (input.get(i-1)[j].equals("@")) {
                        count++;
                    }
                    if (count < 4) {
                        result++;
                        int[] index = new int[2];
                        index[0] = i;
                        index[1] = j;
                        toRemove.add(index);

                    }
                }

                else if (input.get(i)[j].equals("@") && i == input.size()-1 && j == input.get(i).length-1) { // right bottom coner
                    result++;
                    int[] index = new int[2];
                    index[0] = i;
                    index[1] = j;
                    toRemove.add(index);

                }

                else if (input.get(i)[j].equals("@") && i != 0 && i != input.size()-1 && j == input.get(i).length-1) { // right column without head and tail
                    if (input.get(i+1)[j].equals("@")) {
                        count++;
                    }
                    if (input.get(i-1)[j].equals("@")) {
                        count++;
                    }
                    if (input.get(i+1)[j-1].equals("@")) {
                        count++;
                    }
                    if (input.get(i-1)[j-1].equals("@")) {
                        count++;
                    }
                    if (input.get(i)[j-1].equals("@")) {
                        count++;
                    }
                    if (count < 4) {
                        result++;
                        int[] index = new int[2];
                        index[0] = i;
                        index[1] = j;
                        toRemove.add(index);
                    }
                }
                else if (input.get(i)[j].equals("@") && i == 0 && j == input.get(i).length-1) { // right top coner
                    result++;
                    int[] index = new int[2];
                    index[0] = i;
                    index[1] = j;
                    toRemove.add(index);
                }
            }
        }
        if (result == 0) {
            return 0;
        }
        for  (int i = 0; i < toRemove.size(); i++) {
            int[] a =  toRemove.get(i);
            input.get(a[0])[a[1]] = "X";
        }
        return result + check(input);
    }
}
