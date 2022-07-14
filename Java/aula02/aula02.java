// Comandos de decisões: if, if/else, ?, switch case. 
package Java.aula02;

public class aula02 {
    public static void main(String[] args){
        
        double nota1 = 8.6;
        double nota2 = 5.3;
        double media = (nota1 + nota2);

        // if ... else = se ... senão
        // if ... else if ... else = se ... senão se ... senão
        if(media >= 7){
            System.out.print("Aluno aprovado");
        } else if ( media >= 5){
            System.out.println("Aluno de recuperação");
        } else {
            System.out.println("Aluno reprovado");
        }

        // Condicional ternario

        String res = (media >= 7 ? "Aprovado" : "Reprovado");
        System.out.println("O aluno está " + res);

        // Switch case
        int pos = 1;

        switch(pos){
            case 1:
                System.out.println("Esta em primeiro lugar");
                break;
            case 2:
                System.out.println("Está em segundo lugar");
                break;
            case 3:
                System.out.println("Está em terceiro lugar");
                break;
            default:
                System.out.println("Não ganhou");
                break;
        }

        System.out.println("Fim do programa");

    }
}
