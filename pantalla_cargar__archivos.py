from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFileDialog, QMessageBox, QFrame, QApplication
)
from PySide6.QtCore import Qt
import os
import sys

class PantallaCargarArchivos(QWidget):
    def __init__(self, volver_al_menu_callback):
        super().__init__()
        self.volver_al_menu_callback = volver_al_menu_callback
        self.setMinimumSize(1000, 700)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # Botón volver
        btn_volver = QPushButton("← Volver al Menú Principal")
        btn_volver.setStyleSheet("background-color: #2567B3; color: white; font-weight: bold; padding: 6px;")
        btn_volver.setFixedWidth(220)
        btn_volver.clicked.connect(self.volver_al_menu_callback)
        layout.addWidget(btn_volver, alignment=Qt.AlignLeft)

        # Título
        titulo = QLabel("CARGAR ARCHIVOS")
        titulo.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(titulo, alignment=Qt.AlignLeft)

        layout.addLayout(self.crear_seccion("IMPORTAR ESTUDIANTE", "lista de estudiantes"))
        layout.addLayout(self.crear_seccion("IMPORTAR LABORATORIO", "lista de laboratorios"))

    def crear_seccion(self, titulo, tipo):
        layout = QVBoxLayout()

        lbl = QLabel(titulo)
        lbl.setStyleSheet("font-weight: bold; font-size: 16px;")
        layout.addWidget(lbl)

        row = QHBoxLayout()
        self.input_path = QLabel("Ningún archivo seleccionado")
        self.input_path.setStyleSheet("border: 1px solid #ccc; padding: 4px;")
        row.addWidget(self.input_path, stretch=3)

        btn_subir = QPushButton("Subir")
        btn_subir.setStyleSheet("background-color: #2567B3; color: white;")
        btn_subir.clicked.connect(lambda: self.subir_archivo(tipo))
        row.addWidget(btn_subir, stretch=1)
        layout.addLayout(row)

        # Área simulada de drag & drop
        area = QLabel("⬆️ Selecciona archivo para subir\n o arrástralo aquí")
        area.setAlignment(Qt.AlignCenter)
        area.setStyleSheet("border: 2px dashed #888; padding: 30px; font-style: italic;")
        layout.addWidget(area)

        return layout

    def subir_archivo(self, tipo):
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "CSV Files (*.csv);;All Files (*)")
        if not archivo:
            return

        self.input_path.setText(os.path.basename(archivo))

        # Validaciones simuladas
        if not archivo.endswith(".csv"):
            self.mostrar_error("Formato no válido (.pdf)", "Por favor suba un archivo .CSV")
        elif "error" in os.path.basename(archivo).lower():
            self.mostrar_error("Falta campo correo", "Verifique la estructura del archivo")
        else:
            self.mostrar_exito(tipo)

    def mostrar_exito(self, tipo):
        mensaje = "Estudiantes importados correctamente" if "estudiante" in tipo else "Laboratorios importados correctamente"
        QMessageBox.information(self, "Cargar Exitoso", mensaje)

    def mostrar_error(self, titulo, detalle):
        msg = QMessageBox(self)
        msg.setWindowTitle("Error al cargar")
        msg.setText(titulo)
        msg.setInformativeText(detalle)
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Help)
        msg.exec()

# Para ejecutar esta pantalla de forma independiente
if __name__ == "__main__":
    def volver_al_menu():
        print("Volver al menú principal")

    app = QApplication(sys.argv)
    ventana = PantallaCargarArchivos(volver_al_menu)
    ventana.show()
    sys.exit(app.exec())
