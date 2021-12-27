import java.util.List;
import java.util.ArrayList;
 
public class Solution {
    public static void main(String args[]) {
        System.out.print(run());
    }
    
    public static String run() {
        int remainder;
        int max = -1, ans = 2;
        
        
        for(int d = 2; d <= 1000; d++) {
            List<Integer> list = new ArrayList<Integer>(0);
            remainder = 1;
            
            int diff = 0;
            do {
                remainder = (remainder * 10) % d;
                list.add(remainder);
            } while((diff = list.lastIndexOf(remainder) - list.indexOf(remainder)) == 0);
            
            if(max < diff) {
                max = diff;
                ans = d;
            }
        }
        
        return Integer.toString(ans);
    }
}
