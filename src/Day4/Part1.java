package Day4;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Part1 {
    public static void main(String[] args) {
        String a = "..@@.@@@@.";
        String[] ab = a.split("");
        System.out.println(Arrays.toString(ab));
        String filePath = "src/Day4/input.txt";
        List<String[]> list = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            int count = 0;
            while ((line = br.readLine()) != null) {
                String[] lineParts = line.split("");
                list.add(lineParts);
            }
            System.out.println(check(list));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static int check( List<String[]> input) {
        int result = 0;
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
                    }
                }

                else if (input.get(i)[j].equals("@") && i == 0 && j == 0) { // left top coner
                        result++;
                }

                else if (input.get(i)[j].equals("@") && i == input.size()-1 && j == 0) { // left bottom coner
                        result++;
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
                    }
                }

                else if (input.get(i)[j].equals("@") && i == input.size()-1 && j == input.get(i).length-1) { // right bottom coner
                        result++;
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
                    }
                }
                else if (input.get(i)[j].equals("@") && i == 0 && j == input.get(i).length-1) { // right top coner
                        result++;
                }
            }
        }
        return result;
    }

}
