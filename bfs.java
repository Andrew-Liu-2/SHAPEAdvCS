import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

class bfs{
    public static void main (String args[]){

    }
    public static void bfsAlg(HashMap <String,ArrayList<Integer>> map, String source){
        HashSet<String> discovered = new HashSet<>();
        Queue<String> queue = new LinkedList<>();
        queue.add(source);
        discovered.add(source);

        while (!queue.isEmpty()){
            String value = queue.remove();
            System.out.println(value);
        }
    }
}