import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from interfaz import Ui_MainWindow

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Boton.clicked.connect(self.analizar_texto)

    def analizar_texto(self):
        nombre_archivo = self.ui.Nombre_Arch.text()
        texto = self.ui.Texto_Escribir.text()
        num_lineas = int(self.ui.Num_Lin_Arch.text())

        # Crear el archivo
        with open(nombre_archivo, 'w') as f:
            for _ in range(num_lineas):
                f.write(texto + '\n')

        # Leer y analizar el contenido
        with open(nombre_archivo, 'r') as f:
            contenido = f.read()

        # Contar vocales y consonantes
        vocales = sum(1 for c in contenido.lower() if c in 'aeiouáéíóú')
        consonantes = sum(1 for c in contenido.lower() if c.isalpha() and c not in 'aeiouáéíóú')

        # Mostrar resultados
        self.ui.Num_Vocales.setText(str(vocales))
        self.ui.Num_Conson.setText(str(consonantes))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
