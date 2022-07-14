// Aula de comandos de saidas e variaveis

package Java.aula01;

public class aula01 {
    public static void main(String[] args){
        // Para declarar uma variavel temos que colocar o tipo e o nome. Se não tiver nenhum valor automaticamente é atribuido 0 a variavel.
        int n1 = 10;
        int n2 = 20;
        int n3 = 30;
        int res = n1+n2+n3;

        System.out.print("Olá Mundo"); // Não quebra a linha
        System.out.print("Olá Mundo\n"); // Quebra de linha com /n
        System.out.println("saidas no terminal"); // println quebra a linha assim que é impresso
        System.out.printf("O resultado da soma entre n1 + n2 + n3 é %d", res); // printf permite formatar textos e colocar valores da variaveis dentro dele sem ter que ficar concatenando.
    }
}
