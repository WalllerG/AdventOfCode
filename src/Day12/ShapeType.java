package Day12;

import java.awt.*;
import java.util.List;
import static Day12.Part1.getRotations;

public class ShapeType {
    List<List<Point>> rotations;
    int remaining;
    public ShapeType(List<Point> shape, int remaining) {
        this.rotations = getRotations(shape);
        this.remaining = remaining;
    }
    int area() {
        return rotations.getFirst().size();
    }
}
