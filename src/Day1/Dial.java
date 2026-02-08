package Day1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;


public class Dial {

    public static void main(String[] args) {
        int[][] operation = {{0,68},{0,30}, {1,48},{0,5},{1,60},{0,55},{0,1},{0,99},{1,14},{0,82}};
        System.out.println(password(operation));
    }
    public static int password(int[][] operation) {
        ArrayList<int[]> list = new ArrayList<> (Arrays.asList(operation));
        int startPoint = 50;
        int count = 0;
        for (int i = 0; i<list.size();i++) {
            int num = list.get(i)[1] % 100;
            if (list.get(i)[0] == 0 && list.get(i)[1] % 100 <= startPoint) {
                startPoint = startPoint - num;
                if (startPoint == 0) {
                    count++;
                }
            }
            else if (list.get(i)[0] == 0 && list.get(i)[1] % 100 > startPoint) {
                startPoint = convertLeft(num - startPoint);
                if (startPoint == 0) {
                    count++;
                }
            }
            else if (list.get(i)[0] == 1 && list.get(i)[1] % 100 <= 100 - startPoint) {
                startPoint = startPoint + num;
                if (startPoint == 100) {
                    count++;
                    startPoint = 0;
                }
            }
            else if (list.get(i)[0] == 1 && list.get(i)[1] % 100 > 100 - startPoint) {
                startPoint = startPoint + num - 100;
            }
        }
        return count;
    }

    public static int convertLeft (int a){
        int reversePoint = 100;
        return reversePoint - a;
    }

}
