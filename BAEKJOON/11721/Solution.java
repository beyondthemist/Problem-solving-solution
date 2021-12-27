public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String input = sc.nextLine();
    int i;
    
    for(i = 0; i <= (input.length() / 10 - 1) * 10; i += 10) {
        System.out.println(input.substring(i, i + 10));
    }
    System.out.println(input.substring(i));        
}
