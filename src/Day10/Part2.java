package Day10;

import advent.util.Util;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Part2 {
    public static void main() throws Exception{
        List<String> lines = Util.readInput(true,10);
        //getResult(lines);
        int result = 0;
        for (String line : lines){
            List<Integer> target = getJoltage(lines.get(2));
            List<List<Integer>> buttons = getButtons(lines.get(2));
            int presses = getEvenPress(target, buttons);
            List<Integer> newTarget =getEvenState(target, buttons);
            result += recursion(newTarget,buttons,presses);
        }
        System.out.println(result);
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

    public static boolean checkEven (List<Integer> target) {
      for (Integer i : target){
          if (i % 2 != 0){
              return false;
          }
      }
      return true;
    }

    public static int recursion (List<Integer> target, List<List<Integer>> buttons, int presses){
        if (!checkEven(target)){
            List<Integer> newTarget = getEvenState(target, buttons);
            int newPresses;
            if (newTarget == null) {
                return getPresses(target, buttons);
            }
            else {
                newPresses = getEvenPress(newTarget, buttons);
                return recursion(newTarget,buttons,newPresses);
            }

        }
        else {
            for (int i = 0; i < target.size(); i++) {
                target.set(i, target.get(i) / 2);
            }
            return recursion(target, buttons, presses) * 2 + presses;
        }
    }

    public static List<Integer> getEvenState(List<Integer> target, List<List<Integer>> buttons) {

        Queue<List<Integer>> queue = new LinkedList<>();

        Map<List<Integer>, Integer> visited = new HashMap<>();

        List<Integer> initial = new ArrayList<>(target);

        queue.add(initial);

        visited.put(initial, 0);

        while (!queue.isEmpty()) {
            List<Integer> currentState = queue.poll();

            int presses = visited.get(currentState);

            if (checkEven(currentState)) {
                return currentState;
            }

            for (List<Integer> button : buttons) {
                List<Integer> nextState = press1(button, currentState);

                if (nextState != null && !visited.containsKey(nextState)) {
                    visited.put(nextState, presses+1);
                    visited.remove(currentState, presses);
                    queue.add(nextState);
                }
            }
        }
        return null;

    }


    public static int getEvenPress(List<Integer> target, List<List<Integer>> buttons) {

        Queue<List<Integer>> queue = new LinkedList<>();

        Map<List<Integer>, Integer> visited = new HashMap<>();

        List<Integer> initial = new ArrayList<>(target);

        queue.add(initial);

        visited.put(initial, 0);

        while (!queue.isEmpty()) {
            List<Integer> currentState = queue.poll();

            int presses = visited.get(currentState);

            if (checkEven(currentState)) {
                return presses;
            }

            for (List<Integer> button : buttons) {
                List<Integer> nextState = press1(button, currentState);

                if (nextState != null && !visited.containsKey(nextState)) {
                    visited.put(nextState, presses+1);
                    visited.remove(currentState, presses);
                    queue.add(nextState);
                }
            }
        }
        return -1;
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
                    visited.put(nextState, presses+1);
                    visited.remove(currentState, presses);
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

    private static List<Integer> press1(List<Integer> button, List<Integer> target) {
        List<Integer> next = new ArrayList<>(target);
        for (int index : button) {
            int newVal = next.get(index) - 1;
            if (newVal <= 0) {
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
