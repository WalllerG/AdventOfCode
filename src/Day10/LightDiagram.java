package Day10;

import java.util.Arrays;

public class LightDiagram {
    Light[] diagram;
    int length;
    LightDiagram(int length){
        Light[] diagram = new Light[length];
        for (int i = 0; i < length; i++){
            diagram[i] = new Light();
        }
        this.length = length;
        this.diagram = diagram;
    }
    public String toString(){
        return Arrays.toString(diagram);
    }
}
