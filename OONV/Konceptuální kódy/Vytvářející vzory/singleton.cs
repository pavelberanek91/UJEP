using System;
using System.Collections.Generic;

namespace Singleton
{    
    class GameServer //Singleton
    {
        private static GameServer serverInstance; //-Singleton::instance
        private List<Player> players; //-Singleton::players

        private GameServer() //-Singleton()
        {
            players = new List<Player>();
        }

        public static GameServer GetServerInstance() //+Singleton::getInstance()
        {
            if (serverInstance == null){
                serverInstance = new GameServer();
            }
            return serverInstance;
        }

        public void AddPlayer(Player player) //+Singleton::addPlayer()
        {
            players.Add(player);
        }

        public void RemovePlayer(Player player) //+Singleton::removePlayer()
        {
            players.Remove(player);
        }

        public void GetPlayers() //+Singleton::getPlayers()
        {
            foreach (Player player in players)
            {
                Console.WriteLine(player.userName + "(X: " + player.coordinates[0] + ", Y: " + player.coordinates[1] + ")");
            }
        }
    }

    class Player
    {
        public string userName;
        public int[] coordinates;

        public Player(string userName)
        {
            this.userName = userName;
            coordinates = new int[2];
        }

        public void SetCoordinates(int x, int y)
        {
            coordinates[0] = x;
            coordinates[1] = y;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Player playerAdam = new Player("Adam");
            GameServer serverAdam = GameServer.GetServerInstance();
            serverAdam.AddPlayer(playerAdam);
            playerAdam.SetCoordinates(1, 1);
            Console.WriteLine("Adam se připojil k serveru a přesunul se na pozici (1, 1).");
            
            Player playerAlena = new Player("Alena");
            GameServer serverAlena = GameServer.GetServerInstance();
            serverAlena.AddPlayer(playerAlena);
            playerAlena.SetCoordinates(2, 2);
            Console.WriteLine("Alena se připojila k serveru a přesunula se na pozici (2, 2).");
            
            Console.WriteLine("Co vidí Adam:");
            serverAdam.GetPlayers();

            Console.WriteLine("Co vidí Alena:");
            serverAlena.GetPlayers();

            Console.WriteLine("Adam se odhlásil ze serveru:");
            serverAdam.RemovePlayer(playerAdam);

            Console.WriteLine("Co vidí Alena:");
            serverAlena.GetPlayers();

            /* Výstup v terminálu
            Adam se připojil k serveru a přesunul se na pozici (1, 1).
            Alena se připojila k serveru a přesunula se na pozici (2, 2).
            Co vidí Adam:
            Adam(X: 1, Y: 1)
            Alena(X: 2, Y: 2)
            Co vidí Alena:
            Adam(X: 1, Y: 1)
            Alena(X: 2, Y: 2)
            Adam se odhlásil ze serveru:
            Co vidí Alena:
            Alena(X: 2, Y: 2)
            */
        }
    }
}
