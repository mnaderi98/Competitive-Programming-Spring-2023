import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        scanner.nextLine(); // Consume the remaining newline character

        while (t-- > 0) {
            String s = scanner.nextLine();
            String res = s;
            char check = '0';

            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '?') {
                    res = res.substring(0, i) + check + res.substring(i + 1);
                } else {
                    check = s.charAt(i);
                }
            }

            System.out.println(res);
        }

        scanner.close();
    }
}
