package Day9;

import advent.util.Util;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Part1 {
    static void main() throws Exception{
        List<String> lines = Util.readInput(false,9);
        List<int[]> coors = new ArrayList<>();
        for (int i = 0 ; i < lines.size() ; i++) {
            String[] coor = lines.get(i).split(",");
            coors.add(new int[] {Integer.parseInt(coor[0]), Integer.parseInt(coor[1])});
        }
        System.out.println(Arrays.deepToString(coors.toArray()));
    }
}
