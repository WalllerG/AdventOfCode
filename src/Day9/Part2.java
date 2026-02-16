package Day9;

import advent.util.Util;

import java.awt.geom.GeneralPath;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;



public class Part2 {
    static void main() throws Exception {
        boolean start = true;
        List<String> lines = Util.readInput(true,9);
        GeneralPath path = new GeneralPath();
        List<Point> points = new ArrayList<>();
        for (String line : lines) {
            String[] coor = line.split(",");
            int x = Integer.parseInt(coor[0]);
            int y = Integer.parseInt(coor[1]);
            points.add(new Point(x, y));
            if (start) {
                path.moveTo(x, y);
            }
            else {
                path.lineTo(x, y);
            }
        }
        path.closePath();

    }

    public static long getMaxX (List<List<Integer>> coors) {
        long maxX = 0;
        for (List<Integer> coor : coors) {
            if (coor.getFirst() > maxX) maxX = coor.getFirst();
        }
        return maxX;
    }
    public static long getMaxY (List<List<Integer>> coors) {
        long maxY = 0;
        for (List<Integer> coor: coors) {
            if (coor.getLast() > maxY) maxY = coor.getLast();
        }
        return maxY;
    }
    public static long getMinX (List<List<Integer>> coors) {
        long minX = Integer.MAX_VALUE;
        for (List<Integer> coor : coors) {
            if (coor.getFirst() < minX) minX = coor.getFirst();
        }
        return minX;
    }
    public static long getMinY (List<List<Integer>> coors) {
        long minY = Integer.MAX_VALUE;
        for (List<Integer> coor: coors) {
            if (coor.getLast() < minY) minY = coor.getLast();
        }
        return minY;
    }

    public static long getArea (List<Integer> point1, List<Integer> point2) {
        long length = Math.abs(point2.getFirst() - point1.getFirst()) + 1;
        long width = Math.abs(point2.getLast() - point1.getLast()) + 1;
        return length * width;
    }
}
