
import java.util.Scanner;
public class InvertirArray {

    public static String[] invertirArray(String[] arreglo) {
    String[] invertido = new String[arreglo.length];
    for (int i = 0; i < arreglo.length; i++) {
        invertido[i] = arreglo[arreglo.length - 1 - i];
    }
    return invertido;


    public static void main(String[] args) {
        Scaner sc = new Scanner(System.in);


        System.out.print("Ingrese el tamaño del array: ");
        int n = sc.nextInt();
        sc.nextLine();
    }
        String[] arrayOriginal = new String[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Ingrese el elemento " + (i + 1) + ": ");
            arrayOriginal[i] = sc.nextLine();
        }

        String[] arrayInvertido = invertirArray(arrayOriginal);

        System.out.println("\nArray Original:");
        for (String elemento : arrayOriginal) {
            System.out.println(elemento + "");
        }
        System.out.println("\nArray Invertido:");
        for (String elemento : arrayInvertido) {
            System.out.println(elemento + "");
        }
        sc.close();
    }
}




