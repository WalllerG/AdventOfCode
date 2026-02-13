package Day6;

import advent.util.Util;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Part2 {
    static void main() throws IOException {

        List<String> lines = Util.readInput(false,6);
        List<List<String>> rows = new ArrayList<>();
        for (String line : lines) {
            rows.add(Part1.getRow(line));
        }
        List<List<String>> cols = getColumn(rows);
        System.out.println(Arrays.deepToString(cols.toArray()));
    }

    public static List<List<String>> getColumn (List<List<String>> input) {
        List<List<String>> result = new ArrayList<>();
        for (int i = 0; i < input.getFirst().size(); i++) {
            List<String> list = new ArrayList<>();
            for (List<String> strings : input) {
                list.add(strings.get(i));
            }
            result.add(list);
        }
        return result;
    }
}
