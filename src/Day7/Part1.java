package Day7;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Part1 {
    static void main() throws Exception{
        List<String > lines = advent.util.Util.readInput(false,7);
        List<List<String>> simplify = new ArrayList<>();
        for (String line : lines){
            List<String> row = Arrays.asList(line.split(" "));
            if (row.contains("^")) {
                simplify.add(row);
            }
        }
        System.out.println(simplify);
    }
}
