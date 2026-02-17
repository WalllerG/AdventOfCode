package Day10;

import java.util.ArrayList;
import java.util.List;

public class LightDiagram {
    List<Light> diagram;
    List<Light> goal;
    LightDiagram(int length, List<Light> goal) {
        List<Light> lights = new ArrayList<>();
        for (int i = 0; i < length; i++){
            lights.add(new Light());
        }
        this.diagram = lights;
        this.goal = goal;
    }

    LightDiagram(LightDiagram diagram){
        List<Light> lights = new ArrayList<>();
        for (int i = 0; i < diagram.diagram.size(); i++){
            lights.add(new Light());
        }
        this.diagram = lights;
        this.goal = diagram.goal;
    }

    public boolean check () {
        for (int i = 0; i < goal.size(); i++) {
            if (goal.get(i).on != diagram.get(i).on) {
                return false;
            }
        }
        return true;
    }
    public String toString(){
        return diagram.toString();
    }
}
