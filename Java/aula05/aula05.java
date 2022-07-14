package Java.aula05;

public class aula05 {
    public static void main(String[] args){
        int[] array = new int[5];

        array[0] = 10;
        array[1] = 20;
        array[2] = 30;
        array[3] = 40;
        array[4] = 50;

        System.out.printf("%d\n", array[3]);

        // array iniciado ja com valores

        int[] numeros = {10, 20, 30, 40, 50};

        for (int i=0; i< numeros.length; i++){
            System.out.printf("%d\n", numeros[i]);
        }

        for (int n:numeros){
            System.out.printf("%d\n", n);
        }

    }
}
