import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class Main {

    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int t = Integer.parseInt(br.readLine());
        
        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < t; i++) {
            String str = br.readLine();
            boolean result = true;
            for(int j = 0; j < str.length(); j++) {
                char c = str.charAt(j);
                
                if(c == '(') {
                    stack.push(c);
                } else if(c == ')') {
                    if(!stack.isEmpty()) {
                        stack.pop();
                    } else {
                        result = false;
                        break;
                    }
                }
            }
            
            if(result) result = stack.isEmpty();
            System.out.println(result ? "YES" : "NO");
            stack.clear();
        }

        br.close();
        bw.flush();
        bw.close();
    }

}
