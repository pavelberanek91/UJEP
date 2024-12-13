
using System.Text;
using System.Threading;

namespace Memento
{

    public class TextEditor //Originator
    {
        public string textovyObsah;
        public DateTime posledniUlozeni {get; private set;}
        string autor;

        public TextEditor(string autor)
        {
            this.autor = autor;
            this.textovyObsah = "";
            this.posledniUlozeni = DateTime.Now;
        }

        public Memento VratUktualniStav() //Originator::Save
        {
            posledniUlozeni = DateTime.Now;
            return new Memento(autor, textovyObsah, posledniUlozeni);
        }

        public void NactiStav(Memento predchoziStav) //Originator::Restore
        {
            autor = predchoziStav.autor;
            textovyObsah = predchoziStav.textovyObsah;
            posledniUlozeni = predchoziStav.posledniUlozeni;
        }

        public class Memento //Nested Memento
        {
            public string textovyObsah {get; private set;}
            public DateTime posledniUlozeni {get; private set;}
            public string autor {get; private set;}

            public Memento(string autor, string textovyObsah, DateTime posledniUlozeni)
            {
                this.autor = autor;
                this.textovyObsah = textovyObsah;
                this.posledniUlozeni = posledniUlozeni;
            }
        }
    }

    public class SaveLoadSystem //Caretaker
    {
        TextEditor textEditor;
        Stack<TextEditor.Memento> historie;

        public SaveLoadSystem(TextEditor textEditor)
        {
            this.textEditor = textEditor;
            this.historie = new Stack<TextEditor.Memento>();
        }

        public void UlozStavEditor() //Caretaker::DoSomething
        {
            historie.Push(textEditor.VratUktualniStav());
        }

        public void VratPredchoziStavEditoru() //Caretaker::Undo
        {
            textEditor.NactiStav(historie.Pop());
        }
    }

    
    class Program
    {
        static void Main(string[] args)
        {
            TextEditor codeEditor = new TextEditor("Pavel Beránek");
            SaveLoadSystem saveLoadSystem = new SaveLoadSystem(codeEditor);

            // První stav: prázdný text
            Console.WriteLine("Prvotní stav:");
            saveLoadSystem.UlozStavEditor();
            Console.WriteLine($"Obsah editoru: {codeEditor.textovyObsah}");
            Console.WriteLine($"Načteno: {codeEditor.posledniUlozeni}");
            Thread.Sleep(2000);

            // Úprava obsahu editoru
            Console.WriteLine("\nÚprava obsahu:");
            codeEditor.textovyObsah = "print('Hello world)";
            saveLoadSystem.UlozStavEditor();
            Console.WriteLine($"Obsah editoru: {codeEditor.textovyObsah}");
            Console.WriteLine($"Načteno: {codeEditor.posledniUlozeni}");
            Thread.Sleep(2000);

            // Další úprava obsahu
            Console.WriteLine("\nÚprava obsahu:");
            codeEditor.textovyObsah = "input('Zadej dve cisla: ')";
            Console.WriteLine($"Obsah editoru: {codeEditor.textovyObsah}");
            Console.WriteLine($"Načteno: {codeEditor.posledniUlozeni}");
            Thread.Sleep(2000);

            // Návrat k předchozímu stavu
            Console.WriteLine("\nNávrat k předchozímu stavu:");
            saveLoadSystem.VratPredchoziStavEditoru();
            Console.WriteLine($"Obsah editoru: {codeEditor.textovyObsah}");
            Console.WriteLine($"Načteno: {codeEditor.posledniUlozeni}");
            Thread.Sleep(2000);

            // Návrat k předchozímu stavu
            Console.WriteLine("\nNávrat k původnímu stavu:");
            saveLoadSystem.VratPredchoziStavEditoru();
            Console.WriteLine($"Obsah editoru: {codeEditor.textovyObsah}");
            Console.WriteLine($"Načteno: {codeEditor.posledniUlozeni}");
            Thread.Sleep(2000);

            /* Výstup v terminálu
            Prvotní stav:
            Obsah editoru: 
            Načteno: 13.12.2024 16:59:17

            Úprava obsahu:
            Obsah editoru: print('Hello world)
            Načteno: 13.12.2024 16:59:19

            Úprava obsahu:
            Obsah editoru: input('Zadej dve cisla: ')
            Načteno: 13.12.2024 16:59:19

            Návrat k předchozímu stavu:
            Obsah editoru: print('Hello world)
            Načteno: 13.12.2024 16:59:19

            Návrat k původnímu stavu:
            Obsah editoru: 
            Načteno: 13.12.2024 16:59:17
            */
        }
    }
}
