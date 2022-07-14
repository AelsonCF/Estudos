
// Aula sobre entrada de dados e constantes

package Java.Aula03;
import java.util.Scanner;

public class aula03 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);

        String nome;
        double nota1;
        double nota2;
        double res;
        final int MEDIA = 7;

        System.out.println("Digite o nome do aluno");
        nome = scan.nextLine();
        System.out.println("Digite a primeira nota do aluno");
        nota1 = scan.nextDouble();
        System.out.println("Digite a segunda nota do aluno");
        nota2 = scan.nextDouble();
        res = (nota1 + nota2)/2;

        if(res >= MEDIA){
            System.out.printf("O aluno %S teve a media de %2f então esta aprovado", nome, res);
        }
        scan.close();

    }
    
}
