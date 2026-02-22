package Day1;

import advent.util.Util;


import java.io.IOException;
import java.util.List;


public class Part1 {

    static void main() throws IOException{
        int a = 123456;
        String b = String.valueOf(a);
        String c = b.substring(5,6);
        int d = Integer.parseInt(b);
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
