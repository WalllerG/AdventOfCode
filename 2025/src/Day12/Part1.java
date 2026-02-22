package Day12;

import advent.util.Util;
import java.awt.*;
import java.util.ArrayList;
import java.util.List;


public class Part1 {
    public static void main() throws Exception {
        List<String> lines = Util.readInput(true, 12);
        List<List<Point>> points = getShapes(lines);
        int result = 0;
        result = getResult(lines, points, result);
        System.out.println(result);
    }

    private static int getResult(List<String> lines, List<List<Point>> points, int result) {
        for (int i = 30; i < lines.size(); i++) {
            String[] input = lines.get(i).split(" ");
            String[] board = input[0].split("x");
            Region region = new Region(Integer.parseInt(board[0]), Integer.parseInt(board[1].replace(":","")));
            boolean fit;
            List<ShapeType> shapes = new ArrayList<>();
            for  (int j = 1; j < input.length; j++) {
                int index = Integer.parseInt(input[j]);
                if (index != 0) {
                    ShapeType shape = new ShapeType(points.get(j-1),index);
                    shapes.add(shape);
                }
            }
            int boardArea = region.region.length * region.region[0].length;
            int totalShapeArea = computeTotalShapeArea(shapes);

            if (totalShapeArea > boardArea){
                continue;
            }
            shapes.sort((a, b) -> Integer.compare(b.area(), a.area()));
            fit = dfs(region.region,  shapes);
            if (fit) {
                result++;
            }
        }
        return result;
    }

    public static  List<List<Point>> getRotations(List<Point> point) {
        List<List<Point>> rotation = new ArrayList<>();
        rotation.add(point);
        rotation.add(rotate90(point));
        rotation.add(rotate180(point));
        rotation.add(rotate270(point));
        return rotation;
    }

    public static List<List<Point>> getShapes(List<String> lines) {
        List<List<Point>> points = new ArrayList<>();
        for (int i = 0; i < 26; i += 5) {
            List<Point> shape = new ArrayList<>();
            for  (int k = 1; k < 4; k++) {
                String row = lines.get(i+k);
                for (int j = 0; j < 3; j++) {
                    if (row.charAt(j) == '#') {
                        Point p = new Point(k-1, j);
                        shape.add(p);
                    }
                }
            }
            points.add(shape);
        }
        return points;
    }


    static boolean canPlace(boolean[][] board, List<Point> shape, int r, int c) {

        for (Point p : shape) {
            int nr = r + p.x;
            int nc = c + p.y;

            if (nr < 0 || nr >= board.length || nc < 0 || nc >= board[0].length)
                return false;

            if (board[nr][nc]) // already occupied
                return false;
        }

        return true;
    }

    static void place(boolean[][] board, List<Point> shape, int r, int c, boolean value) {

        for (Point p : shape) {
            board[r + p.x][c + p.y] = value;
        }

    }

    static boolean allPiecesUsed(List<ShapeType> shapes) {
        for (ShapeType s : shapes)
            if (s.remaining > 0)
                return false;
        return true;
    }

    static Point firstEmpty(boolean[][] board) {

        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {

                if (!board[r][c]) {
                    return new Point(r, c);
                }
            }
        }

        return null; // no empty cells
    }

    static int computeTotalShapeArea(List<ShapeType> shapes) {
        int total = 0;

        for (ShapeType type : shapes) {
            int area = type.rotations.getFirst().size();
            total += area * type.remaining;
        }

        return total;
    }

    static boolean dfs(boolean[][] board, List<ShapeType> shapes) {

        if (allPiecesUsed(shapes)) return true;

        Point p = firstEmpty(board);
        if (p == null) return false; // board full but pieces remain

        for (ShapeType type : shapes) {

            if (type.remaining == 0) continue;

            for (List<Point> shape : type.rotations) {

                if (canPlace(board, shape, p.x, p.y)) {

                    place(board, shape, p.x, p.y, true);
                    type.remaining--;

                    if (dfs(board, shapes))
                        return true;

                    type.remaining++;
                    place(board, shape, p.x, p.y, false);
                }
            }
        }

        // Also allow this cell to remain empty
        board[p.x][p.y] = true;

        if (dfs(board, shapes))
            return true;

        board[p.x][p.y] = false;

        return false;
    }


    public static List<Point> rotate90 (List<Point> points) {
        List<Point> result = new ArrayList<>();
        for (Point point : points) {
            if (point.x == 0) {
                Point p = new Point(point.y,2);
                result.add(p);
            }
            if (point.x == 1) {
                Point p = new Point(point.y,1);
                result.add(p);
            }
            if (point.x == 2) {
                Point p = new Point(point.y,0);
                result.add(p);
            }
        }
        return result;
    }

    public static List<Point> rotate180 (List<Point> points) {
        return rotate90(rotate90(points));
    }

    public static List<Point> rotate270 (List<Point> points) {
        return rotate90(rotate90(rotate90(points)));
    }
}
