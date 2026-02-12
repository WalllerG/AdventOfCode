package Day5;

import advent.util.Util;

import java.io.File;
import java.util.*;

public class Part1 {
    static void main(String[] args) throws Exception {
        List<String> part1 = new ArrayList<>();
        List<String> part2 = new ArrayList<>();

        File file = new File("src/Day5/input.txt");
        Scanner sc = new Scanner(file);

        boolean hitEmptyLine = false;

        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            if (line.isBlank()) {
                hitEmptyLine = true;
                continue;
            }

            if (!hitEmptyLine) {
                part1.add(line);
            } else {
                part2.add(line);
            }
        }
        sc.close();
        TreeSet<Long> freshIds = isFreshId(part1);
        int count = 0;
        for  (int i = 0; i < part2.size(); i++) {
            long id = Long.parseLong(part2.get(i));
            if (freshIds.contains(id)) {
                count++;
            }
        }
        System.out.println(count);
    }
    public static TreeSet<Long> isFreshId(List<String> lines) {
        TreeSet<Long> set = new TreeSet<>();
        int i = 0;
        while (i  < lines.size()) {
            String[] ranges = lines.get(i).split("-");
            long start = Long.parseLong(ranges[0]);
            long end = Long.parseLong(ranges[1]);
            for (long j = start; j <= end; j++) {
                set.add(j);
            }
            i++;
        }
        return set;
    }
}
