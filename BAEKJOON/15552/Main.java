// https://www.acmicpc.net/problem/15552

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
 
public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        run();
    }
 
    public static void run() throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        String[] temp = new String[2];
        
        for(int i = 0; i < t; ++i) {
            temp = br.readLine().split(" ");
            bw.write(Integer.parseInt(temp[0]) + Integer.parseInt(temp[1]) + "\n");
        }
        
        bw.flush();
    }
}
