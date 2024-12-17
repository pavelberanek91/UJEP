using System;
using System.Collections.Generic;
using QRCoder;

namespace AbstractFactory
{   
    interface ITicketFactory //AbstractFactory
    {
        public QRTicket CreateQRTicket(string ownerName, string destination);
        public SMSTicket CreateSMSTicket(string ownerName, string destination);

    }  
    
    class TrainTicketFactory: ITicketFactory //ConcreteFactory1
    {
        private static int currentTrainTicketID = 0;
        public string CompanyName {get; private set;}

        public TrainTicketFactory(string companyName)
        {
            CompanyName = companyName;
        }

        public QRTicket CreateQRTicket(string ownerName, string destination)
        {
            return new TrainQRTicket(CompanyName, currentTrainTicketID++, ownerName, destination);
        }

        public SMSTicket CreateSMSTicket(string ownerName, string destination)
        {
            return new TrainSMSTicket(CompanyName, currentTrainTicketID++.ToString(), ownerName, DateTime.Now, 
                                      DateTime.Now.AddHours(1), destination);
        }

    }

    class BusTicketFactory: ITicketFactory //ConcreteFactory2
    {
        private static int currentBusTicketID = 0;
        public string CompanyName {get; private set;}

        public BusTicketFactory(string companyName)
        {
            CompanyName = companyName;
        }

        public QRTicket CreateQRTicket(string ownerName, string destination)
        {
            return new BusQRTicket(CompanyName, currentBusTicketID++.ToString(), ownerName, DateTime.Now, DateTime.Now.AddHours(1), destination);

        }

        public SMSTicket CreateSMSTicket(string ownerName, string destination)
        {
            return new BusSMSTicket(CompanyName, currentBusTicketID++.ToString(), ownerName, DateTime.Now, 
                                    DateTime.Now.AddHours(1), destination);
        }
    }

    abstract class QRTicket //AbstractProductA
    {
        public string CompanyName {get; private set;}
        public string TicketID {get; private set;}
        public string OwnerName {get; private set;}
        public DateTime ValidFrom {get; private set;}
        public DateTime ValidTo {get; private set;}
        public string Destination {get; private set;}

        public QRTicket(string companyName, string ticketID, string ownerName, DateTime validFrom, DateTime validTo, string destination)
        {
            CompanyName = companyName;
            TicketID = ticketID;
            OwnerName = ownerName;
            ValidFrom = validFrom;
            ValidTo = validTo;
            Destination = destination;
        }

        public abstract string GenerateQRCode();

        protected string GenerateAsciiQRCode(QRCodeData qrCodeData)
        {
            string asciiQRCode = "";
            for (int y = 0; y < qrCodeData.ModuleMatrix.Count; y++)
            {
                for (int x = 0; x < qrCodeData.ModuleMatrix[y].Count; x++)
                {
                    asciiQRCode += qrCodeData.ModuleMatrix[y][x] ? "██" : "  "; // Černé bloky pro "1", mezera pro "0"
                }
                asciiQRCode += "\n";
            }
            return asciiQRCode;
        }
    }

    abstract class SMSTicket //AbstractProductB
    {
        public string CompanyName {get; private set;}
        public string TicketID {get; private set;}
        public string OwnerName {get; private set;}
        public DateTime ValidFrom {get; private set;}
        public DateTime ValidTo {get; private set;}
        public string Destination {get; private set;}

        public SMSTicket(string companyName, string ticketID, string ownerName, DateTime validFrom, DateTime validTo, string destination)
        {
            CompanyName = companyName;
            TicketID = ticketID;
            OwnerName = ownerName;
            ValidFrom = validFrom;
            ValidTo = validTo;
            Destination = destination;
        }

        public abstract string PrintInfo();

        public virtual bool ValidateTicket()
        {
            return ValidFrom <= DateTime.Now && DateTime.Now <= ValidTo;
        }
    }

    class TrainQRTicket: QRTicket //ConcreteProductA1
    {
        public TrainQRTicket(string companyName, int ticketID, string ownerName, string destination) : base(companyName, ticketID.ToString(), ownerName, DateTime.Now, DateTime.Now.AddHours(1), destination) {}

        public override string GenerateQRCode()
        {
            string qrData = $"Train Ticket ({CompanyName})\nID: {TicketID}\nOwner: {OwnerName}\nFrom: {ValidFrom}\nTo: {ValidTo}\nDestination: {Destination}";

            using (QRCodeGenerator qrGenerator = new QRCodeGenerator())
            {
                QRCodeData qrCodeData = qrGenerator.CreateQrCode(qrData, QRCodeGenerator.ECCLevel.Q);
                return GenerateAsciiQRCode(qrCodeData);
            }
        }
    }

    class TrainSMSTicket: SMSTicket //ConcreteProductB1
    {
        public TrainSMSTicket(string companyName, string ticketID, string ownerName, DateTime validFrom, DateTime validTo, string destination): base(companyName, ticketID, ownerName, validFrom, validTo, destination) {}


        public override string PrintInfo()
        {
            string smsData = $"Train Ticket ({CompanyName})ID: {TicketID}\nOwner: {OwnerName}\nFrom: {ValidFrom}\nTo: {ValidTo}\nDestination: {Destination}";

            return smsData;
        }
    }

    class BusQRTicket: QRTicket //ConcreteProductA2
    {
        public BusQRTicket(string companyName, string ticketID, string ownerName, DateTime validFrom, DateTime validTo, string destination): base(companyName, ticketID, ownerName, validFrom, validTo, destination) {}

        public override string GenerateQRCode()
        {
            string qrData = $"Bus Ticket ({CompanyName})\nID: {TicketID}\nOwner: {OwnerName}\nFrom: {ValidFrom}\nTo: {ValidTo}\nDestination: {Destination}";

            using (QRCodeGenerator qrGenerator = new QRCodeGenerator())
            {
                QRCodeData qrCodeData = qrGenerator.CreateQrCode(qrData, QRCodeGenerator.ECCLevel.Q);
                return GenerateAsciiQRCode(qrCodeData);
            }
        }
    }

    class BusSMSTicket: SMSTicket //ConcreteProductB2
    {
        public BusSMSTicket(string companyName, string ticketID, string ownerName, DateTime validFrom, DateTime validTo, string destination): base(companyName, ticketID, ownerName, validFrom, validTo, destination) {}


        public override string PrintInfo()
        {
            string smsData = $"Bus Ticket ({CompanyName})ID: {TicketID}\nOwner: {OwnerName}\nFrom: {ValidFrom}\nTo: {ValidTo}\nDestination: {Destination}";

            return smsData;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {

            /* Factories/Product Matrix
            |            | BusTicketFactory | TrainTickerFactory | - Factories
            |------------|------------------|--------------------|
            | QR Ticket  | BusQRTicket      | TrainQRTicket      |
            | SMS Ticket | BusSMSTicket     | BusSMSTicket       |
            |
            Products
            */

            //instalace nuget balíčku pro QR kódy: terminál -> dotnet add package QRCoder
            //vypsání nainstalovaných balíčků: terminál -> dotnet list package
            //smazání balíčku: terminál -> dotnet remove package QRCoder

            List<QRTicket> jizdenkyQRApp = new List<QRTicket>();
            List<SMSTicket> jizdenkySMS = new List<SMSTicket>();

            ITicketFactory ticketFactory = new BusTicketFactory("Dopravní podnik města Ústí nad Labem");
            QRTicket qrTicket = ticketFactory.CreateQRTicket("Jan Novák", "Praha");
            jizdenkyQRApp.Add(qrTicket);
            SMSTicket smsTicket = ticketFactory.CreateSMSTicket("Jan Novák", "Brno");
            jizdenkySMS.Add(smsTicket);

            ticketFactory = new TrainTicketFactory("České dráhy");

            qrTicket = ticketFactory.CreateQRTicket("Petr Svoboda", "Olomouc");
            jizdenkyQRApp.Add(qrTicket);
            smsTicket = ticketFactory.CreateSMSTicket("Petr Svoboda", "Plzeň");
            jizdenkySMS.Add(smsTicket);

            foreach (var ticket in jizdenkyQRApp)
            {
                Console.WriteLine(ticket.GenerateQRCode());
            }

            foreach (var ticket in jizdenkySMS)
            {
                Console.WriteLine(ticket.PrintInfo());
            }

        }
    }
}
