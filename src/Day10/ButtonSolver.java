package Day10;

import java.util.*;

public class ButtonSolver {

    private int best = Integer.MAX_VALUE;
    private int[][] effects;
    private int m, n;

    public int minPresses(List<Integer> target, List<List<Integer>> buttons) {

        n = target.size();
        m = buttons.size();

        // Convert target to array
        int[] remaining = new int[n];
        for (int i = 0; i < n; i++) {
            remaining[i] = target.get(i);
        }

        // Convert buttons to matrix form
        effects = new int[m][n];
        for (int j = 0; j < m; j++) {
            for (int idx : buttons.get(j)) {
                effects[j][idx] = 1;
            }
        }

        dfs(0, remaining, 0);

        return best == Integer.MAX_VALUE ? -1 : best;
    }

    private void dfs(int buttonIndex, int[] remaining, int presses) {

        // Prune if already worse than best solution
        if (presses >= best) return;

        // Check if done
        boolean done = true;
        for (int x : remaining) {
            if (x != 0) {
                done = false;
                break;
            }
        }
        if (done) {
            best = presses;
            return;
        }

        // No more buttons
        if (buttonIndex == m) return;

        // Compute max usable times for this button
        int maxUse = Integer.MAX_VALUE;
        boolean useful = false;

        for (int i = 0; i < n; i++) {
            if (effects[buttonIndex][i] == 1) {
                useful = true;
                maxUse = Math.min(maxUse, remaining[i]);
            }
        }

        // If button does nothing helpful, skip it
        if (!useful) {
            dfs(buttonIndex + 1, remaining, presses);
            return;
        }

        // Try k presses (largest first for better pruning)
        for (int k = maxUse; k >= 0; k--) {

            // Apply k presses
            for (int i = 0; i < n; i++) {
                remaining[i] -= k * effects[buttonIndex][i];
            }

            dfs(buttonIndex + 1, remaining, presses + k);

            // Undo (backtrack)
            for (int i = 0; i < n; i++) {
                remaining[i] += k * effects[buttonIndex][i];
            }
        }
    }

}
