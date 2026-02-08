package Day1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class Dial {

    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("src/Day1/operationList.txt"))) {
            String line;
            int count = 0;
            int starPoint = 50;
            // Read line by line until the end of the file
            while ((line = br.readLine()) != null) {

                line = line.trim(); // Remove hidden spaces or newline characters
                int val = Integer.parseInt(line.substring(1)) % 100;
                char dir = line.charAt(0);
                // Execute your logic
                starPoint = password(dir,val,starPoint);
                if (starPoint == 0) {
                    count++;
                }
            }
            System.out.println(count);
        } catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
        }

    }

    public static int password(char direction, int val, int startPoint) {
        if (direction == 'L' && val <= startPoint) {
            startPoint = startPoint - val;
        }
        else if (direction == 'L' && val > startPoint) {
            startPoint = convertLeft(val - startPoint);
        }
        else if (direction == 'R' && val <= 100 - startPoint) {
            startPoint = startPoint + val;
            if (startPoint == 100) {
                startPoint = 0;
            }
        } else if (direction == 'R' && val > 100 - startPoint) {
            startPoint = startPoint + val - 100;
        }
        return startPoint;
    }

    public static int convertLeft (int a){
        int reversePoint = 100;
        return reversePoint - a;
    }

}
