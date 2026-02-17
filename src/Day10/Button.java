package Day10;

import java.util.List;

public class Button {
    List<Integer> inputs;
    LightDiagram diagram;
    public Button(List<Integer> inputs,  LightDiagram diagram) {
        this.inputs = inputs;
        this.diagram = diagram;
    }
    public void click() {
        for (Integer i : inputs) {
            diagram.diagram.get(i).click();
        }
    }
    public String toString() {
        return inputs.toString();
    }
}
