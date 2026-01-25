# Duck Typing : it is a concept where the type of an object is determined
# by its behaviour, not by its class

class InkjectPrinter:
    def PrintDocument(self,document):
        print("Inkject Printer printing:",document)

class LaserPrinter:
    def PrintDocument(self,document):
        print("Laser Printer printing:",document)

class PdfWriter:
    def PrintDocument(self,document):
        print(f"saving {document} as pdf")


def StartPrinting(device):
    device.PrintDocument("Marvellous Notes")

def  main():

    StartPrinting(InkjectPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PdfWriter())

main()