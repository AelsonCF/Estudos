﻿using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("#######################");
        Console.WriteLine("Bem vindo a calculadora");
        Console.WriteLine("#######################\n\n");
        bool ligado = true;


        Console.WriteLine("Digite um numero");
        float n1 = float.Parse(Console.ReadLine());
        float n2;
        float res;
        float arm = n1;

        while (ligado)
        {
            if (ligado)
            {
                Console.WriteLine("Escolha a operação: \n[+] Soma\n[-] Subtração\n[*] Multiplicação\n[/] Divisão");
                string escolha = Console.ReadLine();

                switch (escolha)
                {
                    case "+":
                        Console.WriteLine("Digite outro numero:");
                        n2 = float.Parse(Console.ReadLine());
                        res = arm + n2;
                        Console.WriteLine("A soma entre {0} e {1} é {2}", arm, n2, res);
                        arm = res;
                        break;
                    case "-":
                        Console.WriteLine("Digite outro numero:");
                        n2 = float.Parse(Console.ReadLine());
                        res = arm - n2;
                        Console.WriteLine("A subtração entre {0} e {1} é {2}", arm, n2, res);
                        arm = res;
                        break;
                    case "*":
                        Console.WriteLine("Digite outro numero:");
                        n2 = float.Parse(Console.ReadLine());
                        res = arm * n2;
                        Console.WriteLine("A subtração entre {0} e {1} é {2}", arm, n2, res);
                        arm = res;
                        break;
                    case "/":
                        Console.WriteLine("Digite outro numero:");
                        n2 = float.Parse(Console.ReadLine());
                        res = arm / n2;
                        Console.WriteLine("A subtração entre {0} e {1} é {2}", arm, n2, res);
                        arm = res;
                        break;
                    default:
                        Console.WriteLine("Operação invalida");
                        break;
                }
            }
        }
    }
}