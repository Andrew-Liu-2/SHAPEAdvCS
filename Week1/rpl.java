import java.util.*;

public class rpl {
    public static void main(String args[]) {
        System.out.println(rpl("2 3 4 * +"));
    }

    public static Object rpl(String rplStr){
        Object [] rplArr = rplStr.split(" ");
        Stack <Integer> stack = new Stack<>();
        for (int i = 0; i < rplArr.length; i++){
            if (rplArr[i].equals("+") || rplArr[i].equals("-") || rplArr[i].equals("*") || rplArr[i].equals("/") ){
                Object operator = rplArr[i];
                int operand2 = stack.pop();
                int operand1 =  stack.pop();
                System.out.println(operand2);
                System.out.println(operand1);
                if (operator.equals("+")){
                    stack.push( (Integer) operand2+ (Integer)operand1);
                }
                else if (operator.equals("-")){
                    stack.push( (Integer)operand1 - (Integer)operand2);
                }
                else if (operator.equals("/")){
                    stack.push( (Integer)operand1 / (Integer)operand2);
                }
                else if (operator.equals("*")){
                    stack.push((Integer)operand1 * (Integer) operand2);
                }
            }
            else {
                stack.push((Integer) rplArr[i]);
            }
            System.out.println(stack);
        }
        return stack.pop();
    }
    
}