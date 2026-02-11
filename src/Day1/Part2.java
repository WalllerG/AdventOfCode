package Day1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Part2 {
    static void main() {

    }

    public static int password(char direction, int val, int startPoint) {
        if (direction == 'L' && val <= startPoint) {
            startPoint = startPoint - val;
        }
        else if (direction == 'R' && val <= 100 - startPoint) {
            startPoint = startPoint + val;
            if (startPoint == 100) {
                startPoint = 0;
            }
        } else if (direction == 'R' && val > 100 - startPoint) {
            startPoint = startPoint + val - 100;
        }
        else {
            startPoint = convertLeft(val - startPoint);
        }
        return startPoint;
    }

    public static int convertLeft (int a){
        int reversePoint = 100;
        return reversePoint - a;
    }
}
