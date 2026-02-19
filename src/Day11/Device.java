package Day11;

import java.util.HashSet;

public class Device {
    String name;
    HashSet<Device> outputs;
    public Device(String name, HashSet<Device> outputs) {
        this.name = name;
        this.outputs = outputs;
    }

    public String toString(){
        return this.name + ": " +  this.outputs;
    }
}
