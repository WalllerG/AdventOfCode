package Day10;

import java.util.ArrayList;
import java.util.List;

public class Button {
    List<Integer> inputs;
    LightDiagram diagram;
    public Button(List<Integer> inputs,  LightDiagram diagram) {
        this.inputs = inputs;
        this.diagram = diagram;
    }
    Button(LightDiagram diagram, Button button) {
        this.diagram = diagram;
        this.inputs = button.inputs;
    }
    public void click() {
        for (Integer i : inputs) {
            this.diagram.diagram.get(i).click();
        }
    }
    public String toString() {
        return inputs.toString();
    }
}
