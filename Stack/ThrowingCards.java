public class ThrowingCards {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            int n = sc.nextInt();
            if (n == 0) break;

            Stack<Integer> stack = new Stack<>();

            for (int i = n; i >= 1; i--) {
                stack.push(i);
            }

            List<Integer> descartadas = new ArrayList<>();

            while (stack.size() > 1) {
                descartadas.add(stack.pop());

                int proxima = stack.pop();

                Stack<Integer> aux = new Stack<>();

                while (!stack.isEmpty()) {
                    aux.push(stack.pop());
                }

                stack.push(proxima);

                while (!aux.isEmpty()) {
                    stack.push(aux.pop());
                }
            }

            System.out.print("Cartas descartada:");
            for (int i = 0; i < descartadas.size(); i++) {
                if (i == 0) System.out.print(" ");
                System.out.print(descartadas.get(i));
                if (i < descartadas.size() - 1) {
                    System.out.print(", ");
                }
            }
            System.out.println();

            System.out.println("Cartas restantes: " + stack.peek());
        }

        sc.close();
    }
}
