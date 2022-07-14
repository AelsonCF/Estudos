package Java;
import java.util.Scanner;


public class calculadora {

    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        boolean ligado = true;
        // variaveis utilizadas
        System.out.println("Digite o primeiro numero");
        float n1 = scan.nextFloat();

        
        float res;
        float arma = n1;

        while(ligado){
            if(arma > 0){
                System.out.println("Digite uma operação: [+] Soma, [-] Subtração, [/] Divisão, [*] Multiplicação");
                String operacao = scan.nextLine();
                
                if(operacao.equals("+")){
                    System.out.println("Digite outro numero:");
                    float n2 = scan.nextFloat();
                    res = arma + n2;
                    System.out.printf("O valor da soma entre %f e %f é %f\n", arma, n2, res);
                    arma = res;
                }
                else if(operacao.equals("-")){
                    System.out.println("Digite outro numero:");
                    float n2 = scan.nextFloat();
                    res = arma - n2;
                    System.out.printf("O valor da soma entre %f e %f é %f\n", arma, n2, res);
                    arma = res;
                }
                else if(operacao.equals("/")){
                    System.out.println("Digite outro numero:");
                    float n2 = scan.nextFloat();
                    res = arma / n2;
                    System.out.printf("O valor da soma entre %f e %f é %f\n", arma, n2, res);
                    arma = res;
                }
                else if(operacao.equals("*")){
                    System.out.println("Digite outro numero:");
                    float n2 = scan.nextFloat();
                    res = arma * n2;
                    System.out.printf("O valor da soma entre %f e %f é %f\n", arma, n2, res);
                    arma = res;
                }
                else{
                    System.out.println("Operação inválida !!");
                }
            }
        }
        scan.close();
    }
}
