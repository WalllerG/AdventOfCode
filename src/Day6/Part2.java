package Day6;

import advent.util.Util;

import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class Part2 {
    static void main() throws IOException {

        List<String> lines = Util.readInput(true, 6);
        List<String[]> list = lines.stream().map(line -> line.split("")).collect(Collectors.toList());
        int max = 0;
        for (String[] strings : list) {
            if (strings.length > max) {
                max = strings.length;
            }
        }

        for (int i = 0; i < list.size(); i++) {
            String[] current = list.get(i);
            if (current.length < max) {
                String[] padded = Arrays.copyOf(current, max);

                for (int j = current.length; j < max; j++) {
                    padded[j] = " ";
                }
                list.set(i, padded);
            }
        }

        List<Long> numList = new ArrayList<>();
        List<List<Long>> finalList = new ArrayList<>();
        outer:
        for (int j = 0; j < max; j++) {
            String newNum = "";
            for (int i = 0; i < list.size() - 1; i++) {
                if (list.get(0)[j].equals(" ") && list.get(1)[j].equals(" ") && list.get(2)[j].equals(" ") && list.get(3)[j].equals(" ")) {
                    finalList.add(numList);
                    numList = new ArrayList<>();
                    continue outer;
                }
                if (list.get(i)[j].equals(" ") || list.get(i)[j] == null) {
                    newNum += "";
                } else {
                    newNum += list.get(i)[j];
                }
            }
            long newLong = Long.parseLong(newNum);
            numList.add(newLong);
            if (j == max - 1) {
                finalList.add(numList);
            }
        }

        String[] signs = lines.getLast().split(" ");
        List<String> signList = new ArrayList<>();
        for (String sign : signs) {
            if (sign.contains("*")) {
                signList.add("*");
            } else if (sign.contains("+")) {
                signList.add("+");
            }
        }

        long finalResult = 0;
        for  (int i = 0; i < signList.size(); i++) {
            if  (signList.get(i).equals("*")) {
                long time = 1;
                for (Long l : finalList.get(i)) {
                    time *= l;
                }
                finalResult += time;
            }
            else if(signList.get(i).equals("+")) {
                long add = 0;
                for (Long l : finalList.get(i)) {
                    add += l;
                }
                finalResult += add;
            }
        }
        System.out.println(finalResult);
    }
}
