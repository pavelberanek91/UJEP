using System;

abstract class Iterator
{
    public int actualIndex;
    public int actualNumber;
    public abstract int GetNext();
    public abstract bool HasMore();
}

interface IterableCollection
{
    Iterator CreateIterator(string type);
}

class ListCollection: IterableCollection
{
    public int[] data;

    public ListCollection(int[] data)
    {
        this.data = data;
    }

    public Iterator CreateIterator(string type)
    {
        if (type == "RL")
        {
            return new RightLeftListIterator(this);
        }
        else
        {
            return new LeftRightListIterator(this);
        }
    }
}

class LeftRightListIterator: Iterator
{
    public ListCollection collection;

    public LeftRightListIterator(ListCollection collection)
    {
        this.collection = collection;
        this.actualIndex = 0;
    }

    public override int GetNext()
    {
        if (HasMore())
        {
            actualNumber = collection.data[actualIndex];
            Console.WriteLine($"Index: {actualIndex}, Value: {actualNumber} ");
            actualIndex++;
        }
        else
        {
            Console.WriteLine("Nelze dále iterovat. Došli jsme na konec!");
        }
        return actualNumber;
    }

    public override bool HasMore()
    {
        return actualIndex < collection.data.Length;
    }
}

class RightLeftListIterator: Iterator
{
    public ListCollection collection;

    public RightLeftListIterator(ListCollection collection)
    {
        this.collection = collection;
        this.actualIndex = collection.data.Length - 1;
    }

    public override int GetNext()
    {
        if (HasMore())
        {
            actualNumber = collection.data[actualIndex];
            Console.WriteLine($"Index: {actualIndex}, Value: {actualNumber} ");
            actualIndex--;
        }
        else
        {
            Console.WriteLine("Nelze dále iterovat. Došli jsme na konec!");
        }
        return actualNumber;
    }

    public override bool HasMore()
    {
        return actualIndex >= 0;
    }
}

class TestClass
{
    static void Main(string[] args)
    {
        ListCollection collection = new ListCollection(new int[] {1, 2, 3, 4, 5});
        
        Console.WriteLine("Iterace zleva doprava:");
        Iterator iterator = collection.CreateIterator("LR");
        while (iterator.HasMore())
        {
            iterator.GetNext();
        }

        Console.WriteLine("\nIterace zprava doleva:");
        iterator = collection.CreateIterator("RL");
        while (iterator.HasMore())
        {
            iterator.GetNext();
        }
    }
}
