using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Cript162.Cifras
{
    class Rho
    {
        static int gcd(int a, int b)
        {
            int remainder;
            while (b != 0)
            {
                remainder = a % b;
                a = b;
                b = remainder;
            }
            return a;
        }

        public static string GetFactorCount(int numberToCheck)
        {
            int x_fixed = 2, cycle_size = 2, x = 2, factor = 1;
            while (factor == 1)
            {
                for (int count = 1; count <= cycle_size && factor <= 1; count++)
                {
                    x = (x * x + 1) % numberToCheck;
                    factor = gcd(x - x_fixed, numberToCheck);
                }

                cycle_size *= 2;
                x_fixed = x;
            }
            return "O fator é: " + factor.ToString() ;
        }
    }
}
