import java.util.Stack;

public class Evaluate {
    public static void main(String[] args) {
        Stack<String> ops = new Stack<>();
        Stack<Double> vals = new Stack<>();
        boolean test = StdIn.isEmpty();
        while (!StdIn.isEmpty()) {
            String s = StdIn.readString();
            if (s.equals("(")) {
            } else if (s.equals("+")) {
                ops.push(s);
            } else if (s.equals("-")) {
                ops.push(s);
            } else if (s.equals("*")) {
                ops.push(s);
            } else if (s.equals("/")) {
                ops.push(s);
            } else if (s.equals("sqrt")) {
                ops.push(s);
            } else if (s.equals(")")) {
                String op = ops.pop();
                double val2 = vals.pop();
                if (op.equals("+")) {
                    vals.push(vals.pop() + val2);
                } else if (op.equals("-")) {
                    vals.push(vals.pop() - val2);
                } else if (op.equals("*")) {
                    vals.push(vals.pop() * val2);
                } else if (op.equals("/")) {
                    vals.push(vals.pop() / val2);
                } else if (op.equals("sqrt")) {
                    vals.push(Math.sqrt(val2));
                }
//                } else if (op.equals("(")){
//                    break;
//                }
            } else {
                vals.push(Double.parseDouble(s));

            }
        }
        System.out.print(vals.pop());
    }
}
