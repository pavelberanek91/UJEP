using System;

namespace Prototype
{    
    interface IPrototype<T> //IPrototype
    {
        T Clone(); //IPrototype::Clone()
    }

    class Database: IPrototype<Database> //ConcretePrototype
    {
        public string Name { get; private set; }
        private Dictionary<string, List<string>> authorizationTable;

        private List<string> rows;

        public Database(string name, Dictionary<string, List<string>> authorizationTable, List<string> rows)
        {
            Name = name;
            this.authorizationTable = authorizationTable;
            this.rows = rows;
        }

        public string QueryDatabase(string user, string query)
        {
            if (query == "read" && authorizationTable[query].Contains(user))
            {
                return string.Join("\n", rows);
            }
            else if (query == "delete" && authorizationTable[query].Contains(user))
            {
                rows.Clear();
                return "Database was deleted!";
            }
            else
            {
                return "You don't have permission to do this action!";
            }
        }

        public Database Clone() //ConcretePrototype::Clonse()
        {
            Dictionary<string, List<string>> clonedAuthTable = new Dictionary<string, List<string>>();
            foreach (string key in authorizationTable.Keys)
            {
                clonedAuthTable[key] = new List<string>(authorizationTable[key]);
            }

            List<string> clonedRows = new List<string>(rows);

            return new Database(Name, clonedAuthTable, clonedRows);
        }
    }
    
    
    class Program
    {
        static void Main(string[] args)
        {
            Database database = new Database("database", new Dictionary<string, List<string>>
                {
                    {"read", new List<string>{"admin"}}, 
                    {"delete", new List<string>{"admin"}}
                }, 
                new List<string>
                {
                    "Marek Novak, 34, marek@gmail.com", 
                    "Alena Novakova, 54, alena@email.cz", 
                    "Pepa Jirchar, 23, pepa@seznam.cz"
                }
            );
            Console.WriteLine("Original Database -> Read():");
            Console.WriteLine(database.QueryDatabase("admin", "read"));

            Database databaseCopy = database.Clone();

            Console.WriteLine("\nOriginal Database -> Read after Delete():");
            database.QueryDatabase("admin", "delete");
            Console.WriteLine(database.QueryDatabase("admin", "read"));

            Console.WriteLine("\nCopy of Database -> Read():");
            Console.WriteLine(databaseCopy.QueryDatabase("admin", "read"));

            /* Výstup v terminálu
                Original Database -> Read():
                Marek Novak, 34, marek@gmail.com
                Alena Novakova, 54, alena@email.cz
                Pepa Jirchar, 23, pepa@seznam.cz

                Original Database -> Read after Delete():


                Copy of Database -> Read():
                Marek Novak, 34, marek@gmail.com
                Alena Novakova, 54, alena@email.cz
                Pepa Jirchar, 23, pepa@seznam.cz
            */
        }
    }
}
