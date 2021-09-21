using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculadora___INF319___Pregunta1
{
    public partial class Form1 : Form
    {
        float term1, term2;
        string operat;

        public Form1()
        {
            InitializeComponent();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            if(textBox1.Text=="0")
                textBox1.Text = ((Button)sender).Text;
            else
                textBox1.Text += ((Button)sender).Text;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "")
            {
                term1 = float.Parse(textBox1.Text);
                operat = ((Button)sender).Text;
                textBox1.Text = "";
            }
                
        }

        private void button20_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            if (!textBox1.Text.Contains(","))
            {
                if (textBox1.Text == "")
                    textBox1.Text += "0,";
                else
                    textBox1.Text += ",";

            }
        }

        private void button13_Click_1(object sender, EventArgs e)
        {
            if(textBox1.Text!="")
            {
                term2 = float.Parse(textBox1.Text);
                float res = 0;
                bool sw = false;
                switch (operat)
                {
                    case "+":
                        res = term1 + term2;
                        break;
                    case "-":
                        res = term1 - term2;
                        break;
                    case "*":
                        res = term1 * term2;
                        break;
                    case "/":
                        res = term1 / term2;
                        break;
                    default:
                        res= float.Parse(textBox1.Text);
                        break;
                }
                textBox1.Text = res.ToString();
                operat = "";
            }
            
        }



    }
}
