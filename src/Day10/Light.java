package Day10;

public class Light {
    boolean on;
    public Light(boolean on) {
        this.on = on;
    }
    public Light(){
        this.on = false;
    }
    public void click () {
        on = !on;
    }
    public String toString () {
        return on ? "#" : ".";
    }
}
