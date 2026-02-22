package Day11;

import advent.util.Util;

import java.util.*;

public class Part1 {
    public static void main()  throws Exception {
        List<String> lines = Util.readInput(true, 11);
        getResult(lines,"you");
    }

    public static void getResult(List<String> lines, String target) {
        HashMap<String, Device> devices = new HashMap<>();
        for (String line : lines) {
            String[] parts = line.split(" ");
            String name = parts[0].substring(0,3);
            Device head;
            if (devices.containsKey(name)) {
                head = devices.get(name);
            }
            else {
                head = new Device(name, new HashSet<>());
                devices.put(name, head);
            }
            for  (int i = 1; i < parts.length; i++) {
                if (devices.containsKey(parts[i])) {
                    head.outputs.add(devices.get(parts[i]));
                }
                else {
                    Device device = new Device(parts[i], new HashSet<>());
                    head.outputs.add(device);
                    devices.put(parts[i], device);
                }
            }
        }
        Device out = devices.get("out");
        Device you = devices.get(target);
        System.out.println(getPath(you,out));
    }

    public static int getPath(Device you, Device out) {
        int count = 0;
        for (Device device : you.outputs) {
            if (device.outputs.contains(out)) {
                count++;
            }
            else {
               count += getPath(device,out);
            }
        }
        return count;
    }

}

