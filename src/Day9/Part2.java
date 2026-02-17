package Day9;

import advent.util.Util;

import java.awt.*;
import java.awt.geom.Area;
import java.awt.geom.GeneralPath;
import java.math.BigInteger;
import java.util.*;
import java.util.List;


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
                start = false;
            }
            else {
                path.lineTo(x, y);
            }
        }

        Area area = new Area(path);

        BigInteger largestArea = BigInteger.ZERO;
        for (int i = 0; i < points.size(); i++) {
            for (int j = 0; j < points.size(); j++) {
                int width = Math.abs(points.get(i).x - points.get(j).x) + 1;
                int height = Math.abs(points.get(i).y - points.get(j).y) + 1;
                BigInteger newArea = BigInteger.valueOf(width).multiply(BigInteger.valueOf(height));
                Rectangle rect = new Rectangle(
                        Math.min(points.get(i).x, points.get(j).x),
                        Math.min(points.get(i).y, points.get(j).y),
                        width - 1,
                        height - 1
                );
                if (area.contains(rect)) {
                    if (largestArea.compareTo(newArea) == -1) {
                        largestArea = newArea;
                    }
                }
            }
        }
        System.out.println(largestArea);
    }

}
