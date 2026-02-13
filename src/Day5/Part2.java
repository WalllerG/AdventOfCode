package Day5;

import advent.util.Util;
import java.util.*;
import Day5.FreshRange;

public class Part2 {
    static void main(String[] args) throws Exception {
        List<String> lines = Util.readInput(false, 5);
        List<String> part1 = new ArrayList<>();
        int i = 0;
        while (!lines.get(i).isEmpty()) {
            String line = lines.get(i);
            part1.add(line);
            i++;
        }
        List<FreshRange> ranges = new ArrayList<>();
        outer:
        for (String s : part1) {
            for (FreshRange fr : ranges) {
                if (fr.isOverLap(s)) {
                    continue outer;
                }
            }
            ranges.add(new FreshRange(s));
        }
        long result = 0;
        for  (FreshRange fr : ranges) {
            result += fr.getSize();
        }
        System.out.println(result);
    }




}
