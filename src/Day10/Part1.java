package Day10;

import advent.util.Util;
import java.util.List;

public class Part1 {
    public static void main(String[] args) throws Exception{
        List<String> lines = Util.readInput(false,9);
        LightDiagram diagram = new LightDiagram(4);
        System.out.println(diagram);

        for (int i = 0; i < diagram.length; i++) {
            diagram.diagram[i].click();
        }
        System.out.println(diagram);
    }
}
