package Day12;

import advent.util.Util;

import java.awt.*;
import java.awt.geom.Area;
import java.awt.geom.GeneralPath;
import java.awt.geom.Rectangle2D;
import java.lang.classfile.instruction.LoadInstruction;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Part1 {
    public static void main(String[] args) throws Exception {
        List<String> lines = Util.readInput(false, 12);
        List<String[]> grid = getGrid(lines);
        List<GeneralPath> shapes = getShape(grid);
        Area grid4 = new Area(shapes.get(4));
        Rectangle rec = new Rectangle(0,0,4,4);
        Area region = new Area(rec);

    }

    public static List<String[]> getGrid(List<String> lines) {
        List<String[]> shapes = new ArrayList<>();
        for (int i = 0; i < 29; i += 5) {
            String[] grid = new String[3];
            grid[0] = lines.get(i + 1);
            grid[1] = lines.get(i + 2);
            grid[2] = lines.get(i + 3);
            shapes.add(grid);
        }
        return shapes;
    }

    public static List<GeneralPath> getShape (List<String[]> shapes) {
        List<GeneralPath> grids = new ArrayList<>();
        for (String[] shape : shapes) {
            GeneralPath path = new GeneralPath();
            boolean start = true;
            for (int row = 0; row < shape.length; row++) {
                for (int col = 0; col < shape[row].length(); col++) {
                    if (shape[row].charAt(col) == '#' && start) {
                       path.moveTo(col,row);
                       start = false;
                    }
                    else if (shape[row].charAt(col) == '#') {
                        path.lineTo(col,row);
                    }
                }
            }
            grids.add(path);
        }
        return grids;
    }

    public static List<Point> rotate90 (List<Point> shape) {
        for  (int i = 0; i < shape.size(); i++) {
        }
        return shape;
    }

    public static  List<Point> rotate180 (List<Point> shape) {
        return shape;
    }

    public static List<Point> rotate270 (List<Point> shape) {
        return shape;
    }
}
