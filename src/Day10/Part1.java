package Day10;

import advent.util.Util;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Part1 {
    public static void main() throws Exception{
        List<String> lines = Util.readInput(true,10);
        getResult(lines);
    }

    private static void getResult(List<String> lines) {
        int result = 0;
        for (String line : lines){
            List<List<Integer>> buttons = getButtons(line);
            String target = getSign(line);
            result += getPresses(target, buttons);
        }
        System.out.println(result);
    }

    private static int getPresses(String target, List<List<Integer>> buttons) {

        Queue<String> queue = new LinkedList<>();

        Map<String, Integer> map = new HashMap<>();

        String initial = ".".repeat(target.length());

        queue.add(initial);
        map.put(initial,0);

        while (!queue.isEmpty()){
            String currentState = queue.poll();
            int pressed = map.get(currentState);

            if (currentState.equals(target)) {
                return pressed;
            }
            for (List<Integer> button : buttons) {
                String nextState = toggle(currentState, button);
                if  (!map.containsKey(nextState)) {
                    map.put(nextState,pressed+1);
                    queue.add(nextState);
                }
            }
        }
        System.out.println("No solution found.");
        return 0;
    }

    public static String toggle (String currentState, List<Integer> button) {
        char[] chars = currentState.toCharArray();
        for (int index : button) {
            chars[index] = (chars[index] == '.') ? '#' : '.';
        }
        return new String(chars);
    }


    public static String getSign(String line) {
            String sign = "";
            Pattern p = Pattern.compile("([\\[(])([^)\\]]*)[])]");
            Matcher m = p.matcher(line);
            while (m.find()) {
                String bracketType = m.group(1);
                String content = m.group(2);
                if (bracketType.equals("[")) {
                    sign = String.format("%s", content);

                }
            }
            return sign;
    }

    public static List<List<Integer>> getButtons(String line) {
        List<List<Integer>> ButtonSets = new ArrayList<>();
        Pattern p = Pattern.compile("([\\[(])([^)\\]]*)[])]");
        Matcher m = p.matcher(line);
        while (m.find()) {
            String bracketType = m.group(1);
            String content = m.group(2);
            if (bracketType.equals("(")) {
                List<Integer> nums = new ArrayList<>();
                for (String s : content.split(",")) {
                    if (!s.trim().isEmpty()) {
                        nums.add(Integer.parseInt(s.trim()));
                    }
                }
                ButtonSets.add(nums);
            }
        }
        return ButtonSets;
    }
}
