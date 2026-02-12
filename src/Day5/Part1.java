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
        String[][] freshIds = isFreshId(part1);
        System.out.println(Arrays.deepToString(freshIds));
        int count = 0;
        outer:
        for  (String id : part2) {
           for (String[] ranges : freshIds) {
               if (Long.parseLong(ranges[0]) <= Long.parseLong(id) &&  Long.parseLong(ranges[1]) >= Long.parseLong(id)) {
                   count++;
                   continue outer;
               }
           }
        }
        System.out.println(count);
    }
    public static String[][] isFreshId(List<String> lines) {
        String[][] freshIds = new String[lines.size()][2];
        int i = 0;
        while (i  < lines.size()) {
            String[] ranges = lines.get(i).split("-");
            for (int j = 0; j < freshIds[i].length; j++) {
                freshIds[i][0] = String.valueOf(ranges[0]);
                freshIds[i][1] = String.valueOf(ranges[1]);
            }
            i++;
        }
        return freshIds;
    }
}
