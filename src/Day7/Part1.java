package Day7;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class Part1 {
    static void main() throws Exception {
        List<String> lines = advent.util.Util.readInput(true, 7);
        List<List<String>> simplify = new ArrayList<>();
        for (String line : lines) {
            List<String> row = Arrays.asList(line.split(""));
            if (row.contains("^") || row.contains("S")) {
                simplify.add(row);
            }
        }
        HashSet<Integer> SIndex = new HashSet<>();
        int Start = getStartIndex(simplify.getFirst());
        SIndex.add(Start);
        int count = 0;
        for (int i = 0; i < simplify.size() - 1; i++) {
            HashSet<Integer> copy = deepCopy(SIndex);
            for (Integer index : copy) {
                if (simplify.get(i + 1).get(index).equals("^")) {
                    SIndex.remove(index);
                    SIndex.add(index + 1);
                    SIndex.add(index - 1);
                    count++;
                }
            }
        }
        System.out.println(count);
    }


    public static HashSet<Integer> deepCopy(HashSet<Integer> SIndex) {
        return new HashSet<>(SIndex);
    }

    public static int getStartIndex(List<String> lines) {
        for (int i = 1; i < lines.size(); i++) {
            if (lines.get(i).equals("S")) {
                return i;
            }
        }
        return -1;
    }
}
