package Day9;

import advent.util.Util;

import java.util.*;

public class Part1 {
    static void main() throws Exception{
        List<String> lines = Util.readInput(true,9);
        List<int[]> coors = new ArrayList<>();
        for (String line : lines) {
            String[] coor = line.split(",");
            coors.add(new int[]{Integer.parseInt(coor[0]), Integer.parseInt(coor[1])});
        }
        System.out.println(Arrays.deepToString(coors.toArray()));
        PriorityQueue<Long> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0 ; i < coors.size()-1; i++) {
            for (int j = 0 ; j < coors.size()-1; j++) {
                if (coors.get(i) != coors.get(j)) {
                    long area = getArea(coors.get(i), coors.get(j));
                    pq.add(area);
                }
            }
        }
        System.out.println(pq.poll());
    }

    public static long getArea (int[] point1, int[] point2) {
        long length = Math.abs(point2[0] - point1[0]) + 1;
        long width = Math.abs(point2[1] - point1[1]) + 1;
        return length * width;
    }

}
