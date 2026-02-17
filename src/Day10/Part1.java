package Day10;

import advent.util.Util;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Part1 {
    public static void main(String[] args) throws Exception{
        List<String> lines = Util.readInput(false,10);
        List<LightDiagram> machines = new ArrayList<>();
        List<List<Button>> buttons = new ArrayList<>();
        getMachines(lines, buttons, machines);
        System.out.println(Arrays.toString(machines.toArray()));
        System.out.println(Arrays.toString(buttons.toArray()));
        buttons.getFirst().get(4).click();
        buttons.getFirst().get(5).click();
        System.out.println(machines.getFirst().check());
    }






    private static void getMachines(List<String> lines, List<List<Button>> buttons, List<LightDiagram> machines) {
        for (String line : lines){
            List<String> signs = new ArrayList<>();
            List<List<Integer>> ButtonSets = new ArrayList<>();
            Pattern p = Pattern.compile("([\\[\\(])([^\\)\\]]*)[\\]\\)]");
            Matcher m = p.matcher(line);
            while (m.find()) {
                String bracketType = m.group(1);
                String content = m.group(2);

                if (bracketType.equals("[")) {
                    signs.addAll(Arrays.asList(content.split("")));

                } else if (bracketType.equals("(")) {
                    List<Integer> nums = new ArrayList<>();
                    for (String s : content.split(",")) {
                        if (!s.trim().isEmpty()) {
                            nums.add(Integer.parseInt(s.trim()));
                        }
                    }
                    ButtonSets.add(nums);
                }
            }
            List<Light> lights = new ArrayList<>();
            for (String sign : signs){
                if (sign.equals(".")) {
                    lights.add(new Light(false));
                }
                else if (sign.equals("#")) {
                    lights.add(new Light(true));
                }
            }
            LightDiagram diagram = new LightDiagram(signs.size(),lights);
            List<Button> button = new ArrayList<>();
            for (List<Integer> buttonSet : ButtonSets) {
               button.add(new Button(buttonSet, diagram));
            }
            buttons.add(button);
            machines.add(diagram);
        }
    }
}
