package Day11;

import java.util.List;

public class Device {
    String name;
    List<Device> outputs;
    public Device(String name, List<Device> outputs) {
        this.name = name;
        this.outputs = outputs;
    }

    public String toString(){
        return this.name + ": " +  this.outputs;
    }
}
