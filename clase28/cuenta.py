
class CuentaBancaria:

    def __init__(self, contraseña) -> None:
        self.contra = contraseña

    def __retirar (self, saldo, monto, contraseña):
        if contraseña == self.contra and saldo >= monto:
            saldo -= monto
        else:
            return f"INGRESO INVALIDO. Vuelva a intentarlo."

    def __depositar (self, saldo, monto, contraseña):
        if contraseña == self.contra:
            saldo+= monto
        else:
            return "INGRESO INVALIDO."

class CuentaDebito (CuentaBancaria):
    RECARGO = 10
    
    def __init__(self) -> None:
        super().__init__(self)
        self.saldo = 0
        self.recargo = 10

    def retirar (self, monto, contraseña):
        super().__retirar(self.saldo, monto, contraseña)
        self.saldo -= CuentaDebito.RECARGO
    
    def depositar (self, monto, contraseña):
        super().__depositar(self.saldo, monto, contraseña)



class CuentaCredito (CuentaBancaria):
    
    LIMITE = 1000

    def __init__(self) -> None:
        super().__init__()
        self.saldo = 10000

    def retirar (self, monto, contraseña):
        if monto <= CuentaCredito.LIMITE:
            super().__retirar(self.saldo, monto, contraseña)
        else:
            return "LIMITE EXCEDIDO"
    
    def depositar (self, monto, contraseña):
        super().__depositar(self.saldo, monto, contraseña)
