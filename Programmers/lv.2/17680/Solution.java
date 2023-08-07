import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        if(cacheSize == 0) { return cities.length * 5; }

        for(int i = 0; i < cities.length; ++i) {
            cities[i] = cities[i].toLowerCase();
        }

        int answer = 0;
        List<String> cache = new LinkedList<>();
        for(int i = 0; i < cities.length; ++i) {
            String city = cities[i];
            
            if(cache.contains(city)) {
                cache.remove(city);
                cache.add(city);
                answer += 1;
            } else {
                cache.add(city);
                if(cache.size() > cacheSize) {
                    cache.remove(0);
                }

                answer += 5;
              }
        }

        return answer;
    }
}
