package Day8;

import advent.util.Util;
import com.sun.source.tree.Tree;

import java.io.IOException;
import java.util.*;

public class Part1 {
    public static void main() throws IOException {
        List<String > lines = Util.readInput(true,8);
        HashMap<Integer, List<Integer>> junctionBoxes = getJunctionBoxes(lines);
        List<Map.Entry<Integer,List<Integer>>> sortedList = sort(junctionBoxes);
        List<int[]> pair = findClosestKeys(sortedList,1000);
        Set<Integer> allKeys = new HashSet<>();
        for (int i = 0; i < 1000; i++) {
            allKeys.add(i);
        }
        List<List<Integer>> circuits = getConnectedGroups(pair,allKeys);
        circuits.sort(Comparator.comparingInt(List::size));
        int result = 1;
        for (int i = circuits.size() - 1; i >= circuits.size()-3; i--) {
            result *= circuits.get(i).size();
        }
        System.out.println(result);
    }

    public static List<List<Integer>> getConnectedGroups(List<int[]> pairs, Set<Integer> allKeys) {
        // 1. Initialize Union-Find structure
        Map<Integer, Integer> parent = new HashMap<>();
        for (Integer key : allKeys) {
            parent.put(key, key);
        }

        // 2. Union the pairs
        for (int[] pair : pairs) {
            union(parent, pair[0], pair[1]);
        }

        // 3. Group keys by their ultimate root
        Map<Integer, List<Integer>> groupsMap = new HashMap<>();
        for (Integer key : allKeys) {
            int root = find(parent, key);
            // If the group doesn't exist yet, create a new list
            groupsMap.computeIfAbsent(root, k -> new ArrayList<>()).add(key);
        }

        // 4. Return as a List of Lists
        return new ArrayList<>(groupsMap.values());
    }

    private static int find(Map<Integer, Integer> parent, int i) {
        if (parent.get(i) == i) return i;
        // Path compression for efficiency
        int root = find(parent, parent.get(i));
        parent.put(i, root);
        return root;
    }

    private static void union(Map<Integer, Integer> parent, int i, int j) {
        int rootI = find(parent, i);
        int rootJ = find(parent, j);
        if (rootI != rootJ) {
            parent.put(rootI, rootJ);
        }
    }


    public static HashMap<Integer, List<Integer>> getJunctionBoxes(List<String> lines) {
        HashMap<Integer, List<Integer>> junctionBoxes = new HashMap<>();
        int i = 0;
        for (String line : lines) {
            String[] coordinates = line.split(",");
            List<Integer> xyz = new ArrayList<>();
            for (String coordinate : coordinates) {
                xyz.add(Integer.parseInt(coordinate));
            }
            junctionBoxes.put(i, xyz);
            i++;
        }
        return junctionBoxes;
    }


    public static List<Map.Entry<Integer, List<Integer>>> sort (HashMap<Integer, List<Integer>> junctionBoxes) {
        List<HashMap.Entry<Integer, List<Integer>>> sortedList = new ArrayList<>(junctionBoxes.entrySet());
        sortedList.sort((entry1, entry2) -> {
            Integer val1 = entry1.getValue().getFirst();
            Integer val2 = entry2.getValue().getFirst();
            return val1.compareTo(val2);
        });
        return sortedList;
    }

    public static  List<int[]> findClosestKeys(List<Map.Entry<Integer, List<Integer>>> entries, int k) {
        // 1. Sort by X-coordinate initially (index 0 of the List value)

        PriorityQueue<Result> pq = new PriorityQueue<>(Comparator.comparingDouble(p -> p.distance));
        for (int i = 0; i < entries.size(); i++) {
            for (int j = i + 1; j < entries.size(); j++) {
                double d = calculateDist(entries.get(i), entries.get(j));
                pq.add(new Result(d, entries.get(i).getKey(), entries.get(j).getKey()));
            }
        }
        List<int[]> result = new ArrayList<>();
        for (int i = 0; i < k && !pq.isEmpty(); i++) {
            Result closest = pq.poll();
            result.add(new int[]{closest.key1, closest.key2});
        }

        return result;
    }

    private static double calculateDist(Map.Entry<Integer, List<Integer>> e1, Map.Entry<Integer, List<Integer>> e2) {
        List<Integer> p1 = e1.getValue();
        List<Integer> p2 = e2.getValue();
        return Math.sqrt(Math.pow(p1.get(0) - p2.get(0), 2) +
                Math.pow(p1.get(1) - p2.get(1), 2) +
                Math.pow(p1.get(2) - p2.get(2), 2));
    }
}
