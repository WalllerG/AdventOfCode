package Day9;

import advent.util.Util;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;


public class Part2 {
    static void main() throws Exception {
        List<String> lines = Util.readInput(true,9);
        List<int[]> coors = new ArrayList<>();
        for (String line : lines) {
            String[] coor = line.split(",");
            coors.add(new int[]{Integer.parseInt(coor[0]), Integer.parseInt(coor[1])});
        }
    }

}
