package Day10;

import advent.util.Util;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Part2 {
    public static void main() throws Exception{
        List<String> lines = Util.readInput(true,10);
        getResult(lines);
    }

    private static void getResult(List<String> lines) {
        int result = 0;
        for (String line : lines){
            List<List<Integer>> buttons = getButtons(line);
            List<Integer> target = getJoltage(line);
            result += getPresses(target, buttons);
        }
        System.out.println(result);
    }

    private static int getPresses(List<Integer> target, List<List<Integer>> buttons) {

        Queue<List<Integer>> queue = new LinkedList<>();
        Map<List<Integer>, Integer> visited = new HashMap<>();

        List<Integer> initial = new ArrayList<>(Collections.nCopies(target.size(), 0));
        queue.add(initial);
        visited.put(initial, 0);

        while (!queue.isEmpty()) {
            List<Integer> currentState = queue.poll();
            int presses = visited.get(currentState);

            if (currentState.equals(target)) {
                return presses;
            }

            for (List<Integer> button : buttons) {
                List<Integer> nextState = press(currentState, button, target);

                if (nextState != null && !visited.containsKey(nextState)) {
                    visited.put(nextState, presses + 1);
                    queue.add(nextState);
                }
            }
        }
        return -1;
    }

    private static List<Integer> press(List<Integer> current, List<Integer> button, List<Integer> target) {
        List<Integer> next = new ArrayList<>(current);
        for (int index : button) {
            int newVal = next.get(index) + 1;
            if (newVal > target.get(index)) {
                return null;
            }
            next.set(index, newVal);
        }
        return next;
    }


    public static  List<Integer> getJoltage(String line) {
        String sign = "";
        Pattern p = Pattern.compile("([{])([^}]*)([}])");
        Matcher m = p.matcher(line);

        if (m.find()) {
            sign = m.group(2);
        }
        String[] lines = sign.split(",");
        List<Integer> joltage = new ArrayList<>();
        for (String a: lines) {
            joltage.add(Integer.parseInt(a));
        }
        return joltage;
    }

    public static List<List<Integer>> getButtons(String line) {
        return Part1.getButtons(line);
    }
}
