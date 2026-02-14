package Day7;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import advent.util.Util;

public class Part2 {
    static void main() throws IOException {
       List<String> lines = Util.readInput(true, 7);
       List<List<String>> simplify = Part1.simplify(lines);
       List<String> lastLine = new ArrayList<>();
       for  (String _ : simplify.getFirst())
       {
           lastLine.add(".");
       }
       simplify.add(lastLine);
       int getStartIndex = Part1.getStartIndex(simplify.getFirst());
       Long[][] memo = new Long[simplify.size()][simplify.getFirst().size()];
       System.out.println(backTracking(simplify,0,getStartIndex,memo));
   }
   public static long backTracking (List<List<String>> tree, int height, int startIndex, Long[][] memo) {
       if (memo[height][startIndex] != null) {
           return memo[height][startIndex];
       }
       if (height == tree.size()-1) {
           return 1;
       }
       long result = 0;
       if (tree.get(height+1).get(startIndex).equals("^")) {
           result = backTracking(tree, height+1, startIndex-1,memo) + backTracking(tree, height+1, startIndex+1,memo);
       }
       if (tree.get(height+1).get(startIndex).equals(".")) {
           result = backTracking(tree, height+1, startIndex,memo);
       }
       memo[height][startIndex] = result;
       return result;
   }
}
