package Day11;

import advent.util.Util;

import java.util.*;

public class Part1 {
    public static void main(String[] args)  throws Exception {
        List<String> lines = Util.readInput(true, 11);
        HashMap<String, Device> devices = new HashMap<>();
        for (String line : lines) {
            String[] parts = line.split(" ");
            String name = parts[0].substring(0,3);
            Device head;
            if (devices.containsKey(name)) {
                head = devices.get(name);
            }
            else {
                head = new Device(name, new ArrayList<>());
                devices.put(name, head);
            }
            for  (int i = 1; i < parts.length; i++) {
                if (devices.containsKey(parts[i])) {
                    head.outputs.add(devices.get(parts[i]));
                }
                else {
                    Device device = new Device(parts[i], new ArrayList<>());
                    head.outputs.add(device);
                    devices.put(parts[i], device);
                }
            }
        }
        Device you = devices.get("you");
        System.out.println(getPath(you));
    }

    private static int getPath(Device you) {
        int count = 0;
        for (Device device : you.outputs) {
            if (device.outputs.getFirst().name.equals("out")) {
                count++;
            }
            else {
               count += getPath(device);
            }
        }
        return count;
    }

}

