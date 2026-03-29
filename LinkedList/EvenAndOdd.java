import java.util.*;

public class EvenAndOdd {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        LinkedList<Integer> pares = new LinkedList<>();
        LinkedList<Integer> impares = new LinkedList<>();

        // Leitura e separação
        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();

            if (num % 2 == 0) {
                pares.add(num);
            } else {
                impares.add(num);
            }
        }

        // Ordenação
        Collections.sort(pares); // crescente
        Collections.sort(impares, Collections.reverseOrder()); // decrescente

        // Impressão
        for (int num : pares) {
            System.out.println(num);
        }

        for (int num : impares) {
            System.out.println(num);
        }

        sc.close();
    }
}