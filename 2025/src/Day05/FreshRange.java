package Day5;

public class FreshRange {
    public long start;
    public long end;

    public FreshRange(String input) {
        String[] str = input.split("-");
        this.start = Long.parseLong(str[0]);
        this.end = Long.parseLong(str[1]);
    }

    public boolean inRange (long val) {
        if (val > end || val < start) {
            return false;
        }
        return true;
    }

    public boolean isOverLap (String input) {
        String[] str = input.split("-");
        long newStart = Long.parseLong(str[0]);
        long newEnd = Long.parseLong(str[1]);
        if (inRange(newStart) || inRange(newEnd)) {
            if (newStart < start) {
                this.start = newStart;
            }
            if (newEnd > end) {
                this.end = newEnd;
            }
            return true;
        }
        return false;
    }

    public boolean isOverLap (FreshRange input) {
        long newStart = input.start;
        long newEnd = input.end;
        if (inRange(newStart) || inRange(newEnd)) {
            if (newStart < start) {
                this.start = newStart;
            }
            if (newEnd > end) {
                this.end = newEnd;
            }
            return true;
        }
        return false;
    }

    public long getSize() {
        return end - start + 1;
    }

}
