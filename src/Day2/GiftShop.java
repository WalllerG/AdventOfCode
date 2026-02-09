package Day2;

public class GiftShop {


    public static int sumInvalidId (String[] input) {
        int sum = 0;
        for (String s : input) {
            sum += findInvalidId(s);
        }
        return sum;
    }

    public static int findInvalidId (String ranges) {
        String start = getStart(ranges);
        String end = getEnd(ranges);
        if (isEven(start)) {
            int firstHalfOfStart = Integer.parseInt(start.substring(0, start.length()/2));
            //int secondHalfOfStart = Integer.parseInt(start.substring(start.length()/2));
            int firstHalfOfEnd = Integer.parseInt(end.substring(0,end.length()/2));
            int secondHalfOfEnd= Integer.parseInt(end.substring(end.length()/2));
            int diff1 = firstHalfOfEnd - firstHalfOfStart;
            //int diff2 = secondHalfOfEnd - secondHalfOfStart;
            if (diff1 > 0 && secondHalfOfEnd < firstHalfOfEnd) {
                int result = 0;
                for (int i = 0; i < diff1; i++) {
                    int digits = (int) Math.log10(firstHalfOfStart + i) + 1; // Finds that 8143 has 4 digits
                    result += (firstHalfOfStart + i) * (int) Math.pow(10, digits) + (firstHalfOfStart + i);
                }
                return result;
            }
            else if (diff1 > 0 && secondHalfOfEnd > firstHalfOfEnd) {
                int result = 0;
                for (int i = 0; i < diff1+1; i++) {
                    int digits = (int) Math.log10(firstHalfOfStart + i) + 1; // Finds that 8143 has 4 digits
                    result += (firstHalfOfStart + i) * (int) Math.pow(10, digits) + (firstHalfOfStart + i);
                }
                return result;
            }
            else if (diff1 == 0 && secondHalfOfEnd < firstHalfOfEnd) {
                return 0;
            }
            else {
                int digits = (int) Math.log10(firstHalfOfStart) + 1;
                return (firstHalfOfStart) * (int) Math.pow(10, digits) + (firstHalfOfStart);
            }
        }
        return 0;
    }


    public static boolean isEven (String ranges) {
        int length = ranges.length();
        return length % 2 == 0;
    }

    public static String getStart (String ranges) {
       String[] firstHalf = ranges.split("-");
       return firstHalf[0];
    }

    public static String getEnd (String ranges) {
        String[] secondHalf = ranges.split("-");
        return secondHalf[1];
    }

    static void main (String[] args) {
        String[] ranges = new String[]{"10","20","30"};
    }
}
