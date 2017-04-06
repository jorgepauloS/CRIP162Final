using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Cript162.Cifras
{
    //Gerador de Congruências Lineares (LCG)
    class LCG
    {
        private int _state;
        public bool Microsoft { get; set; }
        public bool BSD
        {
            get
            {
                return !Microsoft;
            }
            set
            {
                Microsoft = !value;
            }
        }
        public LCG(bool microsoft = true)
        {
            _state = (int)DateTime.Now.Ticks;
            Microsoft = microsoft;
        }
        public LCG(int n, bool microsoft = true)
        {
            _state = n;
            Microsoft = microsoft;
        }
        public int Next(int arg)
        {
            return (_state = arg * _state);
        }
        public IEnumerable<int> Seq(int arg)
        {
            while (true)
            {
                yield return Next(arg);
            }
        }
        public static List<int> Sortear(int arg)
        {
            LCG bsd = new LCG((int)DateTime.Now.Ticks, false);
            List<int> lsd = bsd.Seq(arg).Take(4).ToList();
            
            return lsd;
        }
        public static string Congru(List<int> arg, int mod)
        {
            string retorno="";

            for (int i = 0; i < arg.Count(); i++)
            {
                retorno += (arg[i].ToString() + " mod " + mod.ToString()  + "=");
                retorno += (arg[i]%mod).ToString() + " ";
                retorno += ("//");
            }


            return retorno;
        }
    }
}
