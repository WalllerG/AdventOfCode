package Day8;

import advent.util.Util;
import java.io.IOException;
import java.util.*;

import static Day8.Part1.getConnectedGroups;

public class Part2 {
    static void main() throws IOException {
        List<String > lines = Util.readInput(true,8);
        HashMap<Integer, List<Integer>> junctionBoxes = Part1.getJunctionBoxes(lines);
        List<Map.Entry<Integer,List<Integer>>> sortedList = sort(junctionBoxes);
        Set<Integer> allKeys = new HashSet<>();
        for (int i = 0; i < 1000; i++) {
            allKeys.add(i);
        }
        List<List<Integer>> circuits;
        int end = 6000;
        int start = 1000;
        int startBefore = 1000;
        circuits = getConnectedGroups(Part1.findClosestKeys(sortedList,start),allKeys);
        while (end - start > 1) {
            if (circuits.size() > 1) {
                startBefore = start;
                start = start + (end - start) / 2;
            }
            else {
                end = start;
                start = startBefore;
            }
            circuits = getConnectedGroups(Part1.findClosestKeys(sortedList,start),allKeys);
        }
        List<int[]> pair = Part1.findClosestKeys(sortedList,start);
        long result = (long) junctionBoxes.get(pair.getLast()[0]).getFirst() * junctionBoxes.get(pair.getLast()[1]).getFirst();
        System.out.println(result);

    }

    public static List<Map.Entry<Integer, List<Integer>>> sort (HashMap<Integer, List<Integer>> junctionBoxes) {
        return new ArrayList<>(junctionBoxes.entrySet());
    }


}
