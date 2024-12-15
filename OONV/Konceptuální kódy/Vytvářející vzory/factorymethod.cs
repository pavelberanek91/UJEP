using System;
using QRCoder;

namespace FactoryMethod
{        
    abstract class DigitalTicket //Product
    {
        public string TicketID {get; private set;}
        public string OwnerName {get; private set;}
        public DateTime ValidFrom {get; private set;}
        public DateTime ValidTo {get; private set;}
        public string Destination {get; private set;}

        public DigitalTicket(string ticketID, string ownerName, DateTime validFrom, DateTime validTo, string destination)
        {
            TicketID = ticketID;
            OwnerName = ownerName;
            ValidFrom = validFrom;
            ValidTo = validTo;
            Destination = destination;
        }

        public abstract string GenerateTicketDetails(); //Product: DoStuff()

        public virtual bool ValidateTicket() //Product: DoStuff()
        {
            return ValidFrom <= DateTime.Now && DateTime.Now <= ValidTo;
        }
    }

    class TrainTicket : DigitalTicket //ConcreteProductA
    {
        public TrainTicket(string ticketID, string ownerName, DateTime validFrom, DateTime validTo, string destination)
        : base(ticketID, ownerName, validFrom, validTo, destination){}
        
        public override string GenerateTicketDetails()
        {
            return $"Train Ticket:\nID: {TicketID}\nOwner: {OwnerName}\nValid From: {ValidFrom}\nValid To: {ValidTo}\nDestination: {Destination}";
        }
    }

    class BusTicket : DigitalTicket  //ConcreteProductB
    {
        public BusTicket(string ticketID, string ownerName, DateTime validFrom, DateTime validTo, string destination)
        : base(ticketID, ownerName, validFrom, validTo, destination){}
        
        public override string GenerateTicketDetails()
        {
            string qrData = $"ID: {TicketID}\nOwner: {OwnerName}\nFrom: {ValidFrom}\nTo: {ValidTo}\nDestination: {Destination}";

            using (QRCodeGenerator qrGenerator = new QRCodeGenerator())
            {
                QRCodeData qrCodeData = qrGenerator.CreateQrCode(qrData, QRCodeGenerator.ECCLevel.Q);
                return GenerateAsciiQRCode(qrCodeData);
            }
        }

        private string GenerateAsciiQRCode(QRCodeData qrCodeData)
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

     class TicketFactory //Creator
    {
        private static int currentBusTicketID = 0; //stejné jako Creator::SomeOperation() -> Business logika je vyčleněna z ConcreteProducts (zde počítání správného ID)
        private static int currentTrainTicketID = 0;

        public static DigitalTicket CreateTicket(string type, string destination, string ownername) //Creator::CreateProduct()
        {
            switch (type)
            {
                case "Train":
                    return new TrainTicket(
                        ticketID: "T" + currentTrainTicketID++,
                        ownerName: ownername,
                        validFrom: DateTime.Now,
                        validTo: DateTime.Now.AddHours(2),
                        destination: destination
                    );
                case "Bus":
                    return new BusTicket(
                        ticketID: "B" + currentBusTicketID++,
                        ownerName: ownername,
                        validFrom: DateTime.Now,
                        validTo: DateTime.Now.AddHours(1),
                        destination: destination
                    );
                default:
                    throw new ArgumentException("Invalid ticket type.");
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            //instalace nuget balíčku pro QR kódy: terminál -> dotnet add package QRCoder
            //vypsání nainstalovaných balíčků: terminál -> dotnet list package
            //smazání balíčku: terminál -> dotnet remove package QRCoder
            
            Console.WriteLine("Train Ticket:\n");
            DigitalTicket trainTicket = TicketFactory.CreateTicket("Train", "Prague", "Pepa Novák");
            Console.WriteLine(trainTicket.GenerateTicketDetails());
            Console.WriteLine($"Is ticket valid? {trainTicket.ValidateTicket()}");   

            Console.WriteLine("Bus Ticket:\n");
            DigitalTicket busTicket = TicketFactory.CreateTicket("Bus", "Brno", "Pepa Novák");
            Console.WriteLine(busTicket.GenerateTicketDetails());
            Console.WriteLine($"Is ticket valid? {busTicket.ValidateTicket()}");
            /* Výstup v terminálu
                Train Ticket:
                ID: T0
                Owner: Pepa Novák
                Valid From: 15.12.2024 14:22:29
                Valid To: 15.12.2024 16:22:29
                Destination: Prague
                Is ticket valid? True
                
                Bus Ticket:                                                                                                      
                                                                                       
                                                                                                                  
        ██████████████    ██████  ██    ██    ████  ██  ████  ██    ██      ████████    ██  ██████████████        
        ██          ██  ████          ██  ██  ██  ██  ██  ██████████        ██  ██████████  ██          ██        
        ██  ██████  ██      ████    ██  ██████████    ████      ██  ██████████  ████  ████  ██  ██████  ██        
        ██  ██████  ██  ██        ████████            ████    ██    ██  ██████  ██    ██    ██  ██████  ██        
        ██  ██████  ██  ██    ██    ██  ████        ██████████  ██████    ██  ██████        ██  ██████  ██        
        ██          ██    ██████      ████      ██████      ████        ████    ██████      ██          ██        
        ██████████████  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ██████████████        
                        ████████████████  ████████████      ██    ██████████████  ████                            
          ██  ████████  ██    ██████  ██    ██    ████████████████████  ██    ██████████  ████  ████  ██          
            ██  ████  ██    ██████████████  ██  ██  ██  ██    ████  ██      ██      ██  ██  ██    ██  ██          
                    ████    ██    ██    ██  ██████      ██████  ████  ██    ████████  ████      ██████████        
        ████  ██████    ██  ██  ████████      ████  ██████  ██  ████        ██            ████  ██  ██  ██        
                ██  ██  ████████        ██      ██  ████  ██      ██  ██████  ████  ████  ██    ██    ████        
        ██    ██  ██  ██      ██    ██  ████          ██  ██  ██  ████  ██        ██████    ██      ██  ██        
                  ████    ██    ██    ██  ████    ██    ██    ████  ██████      ██  ██  ████    ██  ██████        
            ██    ██  ██  ████  ██  ██    ████  ██  ██          ██  ████    ██    ██      ████    ████            
        ██████    ████████        ████  ██████      ██  ██          ██  ██████  ██    ██████████████████          
        ████  ██      ██  ████    ████████████  ██      ██    ██████████  ████████    ████  ██  ██  ██████        
        ██  ██      ██████  ██    ██████████    ████████  ████      ████████    ██        ██      ██    ██        
              ██      ██  ████████    ████  ██      ██████    ██    ██      ████  ████████  ████  ██              
          ██  ████  ████        ██  ██    ██  ████  ██      ████    ████  ██    ██  ██      ████                  
        ████              ████████  ██      ██  ██████████  ██  ██████    ████    ████  ████████  ██    ██        
          ████  ██████████████  ████    ██████  ██████████████    ████  ████          ████████████  ██  ██        
          ████████      ██  ██  ██    ████  ██████  ██      ██  ██  ██  ██  ██          ██      ██████            
          ██  ████  ██  ████████████  ██  ████    ████  ██  ██    ██    ██  ██  ██████████  ██  ██      ██        
          ██  ████      ██    ██    ██    ██████    ██      ██  ████  ██      ████  ██  ██      ████              
          ██  ████████████████    ██████  ████████  ██████████          ████  ████      ████████████  ████        
            ██    ██            ████    ████  ██    ██████    ██    ████    ████    ██████████  ██████  ██        
        ██    ██  ██████████████  ██████  ████  ████    ██████    ██    ██████  ████████    ████    ██  ██        
          ████    ██    ████  ██  ██  ██  ██████    ██  ████  ██  ████      ██  ██    ████  ████  ██████          
          ██████  ████    ██  ██████  ████████████    ████  ██████      ████    ██      ██  ██  ██████████        
        ████████████      ██████  ██  ████████  ██  ██      ████  ██  ████  ██  ████  ██  ██  ████                
        ██████      ██████████          ██  ████    ████████  ████    ██  ██  ████    ██████    ██      ██        
          ██████████    ██    ████    ████████      ████    ██████  ████    ██  ██  ██████████  ██  ████          
          ████████  ████████  ██  ██████████  ██████    ████████      ██  ████████  ██  ██████  ██████████        
        ██████    ██        ██    ████    ████      ████  ██  ██    ██████        ██  ████          ██████        
        ██████    ████        ██      ██  ██  ██    ██████      ████████████  ████  ██████████        ████        
        ██      ████  ██████  ██████  ██████████    ██    ██████  ██████          ██████      ████████  ██        
          ██      ████████      ██████  ████    ██    ██████    ██    ██            ██████  ████████    ██        
          ██████        ████████  ██  ████  ██    ██          ██  ██  ██  ██  ████    ██  ██      ██████          
        ██████      ██    ██          ██████        ████████████  ██    ██████  ██    ██████████████████          
                        ██      ████████    ████  ████      ██████        ██████        ██      ██████████        
        ██████████████          ████████  ██████    ██  ██  ████████████████  ██  ██  ████  ██  ██  ██████        
        ██          ██  ██████████    ████████    ████      ██  ██  ██      ██    ██  ████      ████    ██        
        ██  ██████  ██  ██████  ████  ██    ████    ██████████████    ██    ██  ██  ██████████████      ██        
        ██  ██████  ██  ████        ████  ██  ██      ██    ██  ██  ██    ████████████    ████    ████            
        ██  ██████  ██        ████    ██    ████    ████  ████        ██  ██    ██        ████████  ██  ██        
        ██          ██  ████  ██      ████          ██  ██████    ████      ████      ████████  ██████████        
        ██████████████        ████████      ██    ██  ██████    ██  ██  ██████  ████████  ██  ██████    ██        
                                                                                                                  
                                                                                                                  
            Is ticket valid? True
            */
        }
    }
}
