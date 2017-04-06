using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Cript162.Cifras
{
    class Rho
    {
        public static string GetFactorCount(int numberToCheck)
        {
            string output = "";
            int factorCount = 0;
            int sqrt = (int)Math.Ceiling(Math.Sqrt(numberToCheck));
            output += numberToCheck.ToString() + " \n ";
            // Começa de 1 se nós quisermos também feito para funcionar quando numberToCheck seja 0 ou 1.
            for (int i = numberToCheck-1; i >= 1; i--)
            {
                if (numberToCheck % i == 0)
                {
                    factorCount += 2; //  Encontrou um par de fatores
                    output += i.ToString()+" \n ";
                }
            }
            // Checa se o número é um quadrado perfeito.
            if (sqrt * sqrt == numberToCheck)
            {
                factorCount++;
            }
            output += factorCount.ToString()+" fatores.";
            return output;
        }
    }
}
