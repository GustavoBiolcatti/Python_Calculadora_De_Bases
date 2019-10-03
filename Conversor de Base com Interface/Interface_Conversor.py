from tkinter import *
import tkinter.ttk as ttk
from Conversor import operacoes


class Application:
    def __init__(self, master=None):
        self.fonteTitulo = ("Google Sans", "12", "bold")
        self.fonteBtn = ("Google Sans", "10", "bold")
        self.fonte = ("Google Sans", "10")
        self.widthLabel = 15
        self.widthEntry = 30
        self.padxContainer = 30
        self.padyContainer = 5
        self.pady = 10

        self.tituloContainer = Frame(master)
        self.tituloContainer["pady"] = self.pady
        self.tituloContainer.pack()

        # INSERIR
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = self.padxContainer
        self.primeiroContainer["pady"] = self.padyContainer
        self.primeiroContainer.pack()

        self.numContainer = Frame(self.primeiroContainer)
        self.numContainer.pack(side=LEFT)

        self.baseContainer = Frame(self.primeiroContainer)
        self.baseContainer.pack()

        # CONVERSÃO
        self.inContainer = Frame(master)
        self.inContainer["padx"] = self.padxContainer
        self.inContainer["pady"] = self.padyContainer+10
        self.inContainer.pack()

        self.segundoContainer = Frame(self.inContainer)
        self.segundoContainer["pady"] = self.padyContainer
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(self.inContainer)
        self.terceiroContainer["pady"] = self.padyContainer
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(self.inContainer)
        self.quartoContainer["pady"] = self.padyContainer
        self.quartoContainer.pack()

        self.quintoContainer = Frame(self.inContainer)
        self.quintoContainer["pady"] = self.padyContainer
        self.quintoContainer.pack()

        # RODAPÉ
        self.rodapeContainer = Frame(master)
        self.rodapeContainer["padx"] = self.padxContainer
        self.rodapeContainer["pady"] = self.padyContainer
        self.rodapeContainer.pack()

        # ========================================================= #
        # TÍTULO
        self.labelTitulo = Label(self.tituloContainer, text="CONVERSOR DE BASE")
        self.labelTitulo["font"] = self.fonteTitulo
        self.labelTitulo.pack()

        # INSERIR DADOS
        self.labelNum = Label(self.numContainer, text="Valor: ")
        self.labelNum["font"] = self.fonte
        self.labelNum.pack(side=LEFT)

        self.entryNum = Entry(self.numContainer)
        self.entryNum["width"] = self.widthEntry-10
        self.entryNum["font"] = self.fonte
        self.entryNum.pack()

        self.labelBase = Label(self.baseContainer, text="                     Base: ")
        self.labelBase["font"] = self.fonte
        self.labelBase.pack(side=LEFT)

        self.comboBase = ttk.Combobox(self.baseContainer, values=[2, 8, 10, 16])
        self.comboBase["width"] = 5
        self.comboBase["font"] = self.fonte
        self.comboBase.pack()

        # DECIMAL
        self.labelDec = Label(self.segundoContainer, text="Decimal: ")
        self.labelDec["width"] = self.widthLabel
        self.labelDec["font"] = self.fonte
        self.labelDec.pack(side=LEFT)

        self.entryDec = Entry(self.segundoContainer)
        self.entryDec["width"] = self.widthEntry
        self.entryDec["font"] = self.fonte
        self.entryDec.pack(side=RIGHT)

        # BINÁRIO
        self.labelBin = Label(self.terceiroContainer, text="Binário: ")
        self.labelBin["width"] = self.widthLabel
        self.labelBin["font"] = self.fonte
        self.labelBin.pack(side=LEFT)

        self.entryBin = Entry(self.terceiroContainer)
        self.entryBin["width"] = self.widthEntry
        self.entryBin["font"] = self.fonte
        self.entryBin.pack(side=RIGHT)

        # OCTAL
        self.labelOct = Label(self.quartoContainer, text="Octal: ")
        self.labelOct["width"] = self.widthLabel
        self.labelOct["font"] = self.fonte
        self.labelOct.pack(side=LEFT)

        self.entryOct = Entry(self.quartoContainer)
        self.entryOct["width"] = self.widthEntry
        self.entryOct["font"] = self.fonte
        self.entryOct.pack(side=RIGHT)

        # HEXADECIMAL
        self.labelHex = Label(self.quintoContainer, text="Hexadecimal: ")
        self.labelHex["width"] = self.widthLabel
        self.labelHex["font"] = self.fonte
        self.labelHex.pack(side=LEFT)

        self.entryHex = Entry(self.quintoContainer)
        self.entryHex["width"] = self.widthEntry
        self.entryHex["font"] = self.fonte
        self.entryHex.pack(side=RIGHT)

        # --------------------------

        self.btnConverter = Button(self.rodapeContainer)
        self.btnConverter["width"] = 10
        self.btnConverter["font"] = self.fonteBtn
        self.btnConverter["text"] = "Converter"
        self.btnConverter["command"] = self.converteValor
        self.btnConverter.pack(side=LEFT)

        self.btnSair = Button(self.rodapeContainer)
        self.btnSair["padx"] = 10
        self.btnSair["width"] = 5
        self.btnSair["font"] = self.fonteBtn
        self.btnSair["text"] = "Sair"
        self.btnSair["command"] = self.btnSair.quit
        self.btnSair.pack()

        # ===================================================================

    def converteValor(self):
        if str(self.entryNum.get()).strip() == "":
            pass
        else:
            n = str(self.entryNum.get()).upper().strip().replace(",", ".")
            base = int(self.comboBase.get())

            if base not in [2, 8, 10, 16]:
                operacoes.mBox(self, "Erro de parâmetro", "A base selecionada não está entre as opções.", 1)
            else:
                if operacoes.verificaValor(self, n=n, num_base=base) != False:
                    self.entryDec.delete(0, 'end')
                    self.entryDec.insert(0, operacoes.converteBase10(self, n=n, num=n, num_base=base))

                    self.entryBin.delete(0, 'end')
                    self.entryBin.insert(0, operacoes.converteBase2(self, n=n, num=n, num_base=base))

                    self.entryOct.delete(0, 'end')
                    self.entryOct.insert(0, operacoes.converteBase8(self, num=n, num_base=base))

                    self.entryHex.delete(0, 'end')
                    self.entryHex.insert(0, operacoes.converteBase16(self, num=n, num_base=base))


root = Tk()
root.title("Conversor de Base")
root.resizable(False, False)
Application(root)
root.mainloop()
