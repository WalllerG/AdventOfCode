package Day12;

import java.util.Arrays;

public class Region {
    boolean[][] region;
    public Region(int  col, int row) {
        this.region = new boolean[row][col];;
    }
    public void printRegion () {
        for (boolean[] booleans : this.region) {
            System.out.println(Arrays.toString(booleans));
        }
    }
}
