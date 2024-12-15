using System;
using System.Collections.Generic;
using System.Text;

namespace Builder
{    

    interface IProgrammer //IBuilder
    {
        string CreateClass(string className); //IBuilder::BuildStepA()
        string CreateMethod(string methodName, string returnType, string[] parameters); //IBuilder::BuildStepB()
        string CreateProperty(string propertyName, string propertyType); //IBuilder::BuildStepC()
    }

    class CSharpProgrammer: IProgrammer //ConcreteBuilder1
    {
        public string CreateClass(string className) //ConcreteBuilder1::BuildStepA()
        {
            return $"class {className}{{}}\n";
        }

        public string CreateMethod(string methodName, string returnType, string[] parameters) //ConcreteBuilder1::BuildStepB()
        {
            string parametersString = string.Join(", ", parameters);
            return $"public {returnType} {methodName}({parametersString}){{}}\n";
        }

        public string CreateProperty(string propertyName, string propertyType) //ConcreteBuilder1::BuildStepC()
        {
            return $"{propertyType} {propertyName} {{ get; set; }}\n";
        }
    }

    class PythonProgrammer: IProgrammer //ConcreteBuilder2
    {
        public string CreateClass(string className) //ConcreteBuilder2::BuildStepA()
        {
            return $"class {className}:\n";
        }

        public string CreateMethod(string methodName, string returnType, string[] parameters) //ConcreteBuilder2::BuildStepB()
        {
            string parametersString = string.Join(", ", parameters);
            return $"def {methodName.ToLower()}(self, {parametersString}):\n\t...\n";
        }

        public string CreateProperty(string propertyName, string propertyType) //ConcreteBuilder2::BuildStepC()
        {
            return $"@property\n{propertyName.ToLower()}(self):\n\treturn self.{propertyName.ToLower()}\n";
        }
    }

    class ProjectManager //Director
    {
        private IProgrammer _programmer; //-IBuilder builder

        public ProjectManager(IProgrammer programmer) //Director(IBuilder builder)
        {
            _programmer = programmer;
        }

        public string CreateApp(List<string> requirementsSpecification) //Director::make(type)
        {
            StringBuilder sourceCode = new StringBuilder();
            foreach (string requirement in requirementsSpecification)
            {
                if (requirement == "registration")
                {
                    sourceCode.Append(_programmer.CreateClass("RegistrationForm"));
                    sourceCode.Append(_programmer.CreateProperty("Username", "string"));
                    sourceCode.Append(_programmer.CreateProperty("Password", "string"));
                    sourceCode.Append(_programmer.CreateMethod("Register", "void", new string[] { "string username", "string password" }));
                }
                else if (requirement == "order system")
                {
                    sourceCode.Append(_programmer.CreateClass("Order"));
                    sourceCode.Append(_programmer.CreateProperty("OrderNumber", "int"));
                    sourceCode.Append(_programmer.CreateProperty("OrderDate", "DateTime"));
                    sourceCode.Append(_programmer.CreateMethod("CreateOrder", "Order", new string[] { "int orderNumber", "DateTime orderDate" }));
                }
                else if (requirement == "payment system")
                {
                    sourceCode.Append(_programmer.CreateClass("Payment"));
                    sourceCode.Append(_programmer.CreateProperty("Amount", "decimal"));
                    sourceCode.Append(_programmer.CreateProperty("Currency", "string"));
                    sourceCode.Append(_programmer.CreateMethod("Pay", "void", new string[] { "decimal amount", "string currency" }));
                }
                else 
                {
                    throw new Exception("Unknown requirement");   
                }
            }
            return sourceCode.ToString();
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            ProjectManager projectManager = new ProjectManager(new CSharpProgrammer());
            List<string> requirementsSpecification = new List<string> { "registration", "order system", "payment system" };
            
            Console.WriteLine("C#");
            string sourceCode = projectManager.CreateApp(requirementsSpecification);
            Console.WriteLine(sourceCode);

            Console.WriteLine("\nPython");
            projectManager = new ProjectManager(new PythonProgrammer());
            sourceCode = projectManager.CreateApp(requirementsSpecification);
            Console.WriteLine(sourceCode);

            /* Výstup v terminálu
            C#
            class RegistrationForm{}
            string Username { get; set; }
            string Password { get; set; }
            public void Register(string username, string password){}
            class Order{}
            int OrderNumber { get; set; }
            DateTime OrderDate { get; set; }
            public Order CreateOrder(int orderNumber, DateTime orderDate){}
            class Payment{}
            decimal Amount { get; set; }
            string Currency { get; set; }
            public void Pay(decimal amount, string currency){}


            Python
            class RegistrationForm:
            @property
            username(self):
                    return self.username
            @property
            password(self):
                    return self.password
            def register(self, string username, string password):
                    ...
            class Order:
            @property
            ordernumber(self):
                    return self.ordernumber
            @property
            orderdate(self):
                    return self.orderdate
            def createorder(self, int orderNumber, DateTime orderDate):
                    ...
            class Payment:
            @property
            amount(self):
                    return self.amount
            @property
            currency(self):
                    return self.currency
            def pay(self, decimal amount, string currency):
                    ...
            */
        }
    }
}
