package Day11;

import advent.util.Util;

import java.util.*;

public class Part2 {
    public static void main()  throws Exception {
        List<String> lines = Util.readInput(true, 11);
        getResult(lines,"svr");
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
        Device you =  devices.get(target);
        Map<String, Long> memo = new HashMap<>();
        System.out.println(getPath(you,false,false,memo));
    }


    public static long getPath(Device you, boolean fft, boolean dac, Map<String, Long> memo) {
        if (you.name.equals("fft")) {
            fft = true;
        }
        if (you.name.equals("dac")) {
            dac = true;
        }

        if (you.name.equals("out")) {
            return (fft && dac) ? 1 : 0;
        }

        String stateKey = you.name + "-" + fft + "-" + dac;
        if (memo.containsKey(stateKey)) {
            return memo.get(stateKey);
        }

        long count = 0;
        for (Device device : you.outputs) {
            count += getPath(device,fft,dac,memo);
        }
        memo.put(stateKey, count);
        return count;
    }

}
