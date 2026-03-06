package Day9;

import javax.swing.*;
import java.awt.*;
import java.awt.geom.Path2D;
import java.awt.geom.Rectangle2D;
import java.io.IOException;
import java.util.List;
import advent.util.Util;

public class PathVisualizer extends JPanel {
    private final Path2D path;

    public PathVisualizer(Path2D path) {
        this.path = path;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        if (path != null) {
            Rectangle2D bounds = path.getBounds2D();

            double scaleX = (getWidth() - 100) / bounds.getWidth();
            double scaleY = (getHeight() - 100) / bounds.getHeight();
            double scale = Math.min(scaleX, scaleY);

            g2.translate(50, 50);
            g2.scale(scale, scale);
            g2.translate(-bounds.getX(), -bounds.getY());

            g2.setStroke(new BasicStroke((float)(3 / scale)));
            g2.setColor(Color.YELLOW);
            g2.draw(path);

            g2.setColor(new Color(100, 150, 255, 100));
            g2.fill(path);
        }
    }

    static void main() throws IOException {
        List<String> lines = Util.readInput(false, 9);
        Path2D path = new Path2D.Double();
        boolean start = true;

        for (String line : lines) {
            String[] coor = line.split(",");
            int x = Integer.parseInt(coor[0].trim());
            int y = Integer.parseInt(coor[1].trim());

            if (start) {
                path.moveTo(x, y);
                start = false;
            } else {
                path.lineTo(x, y);
            }
        }
        path.closePath();


        JFrame frame = new JFrame("Path2D Visualizer");

        PathVisualizer panel = new PathVisualizer(path);

        frame.add(panel);
        frame.setSize(500, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}