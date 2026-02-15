package Day8;

import advent.util.Util;
import java.io.IOException;
import java.util.*;

public class Part2 {
    static void main() throws IOException {
        List<String > lines = Util.readInput(true,8);
        HashMap<Integer, List<Integer>> junctionBoxes = Part1.getJunctionBoxes(lines);
        List<Map.Entry<Integer,List<Integer>>> sortedList = sort(junctionBoxes);
        List<int[]> pair = Part1.findClosestKeys(sortedList,5471);
        long result;
        result = (long) junctionBoxes.get(362).getFirst() * junctionBoxes.get(954).getFirst();
        System.out.println(result);
    }

    public static List<Map.Entry<Integer, List<Integer>>> sort (HashMap<Integer, List<Integer>> junctionBoxes) {
        return new ArrayList<>(junctionBoxes.entrySet());
    }


}
