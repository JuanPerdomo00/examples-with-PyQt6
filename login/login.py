import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QCheckBox
from PyQt6.QtGui import QFont
from modules.RegisterUser import RegisterUserView


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.font_arial = QFont("Arial", 10)
        self.init_ui()

    def init_ui(self):
        # Inicializa la interfaz de usuario con las dimensiones y el título específicos.
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Login")
        # Genera el formulario de inicio de sesión.
        self.generate_form()
        self.show()

    def _login_and_register_button(self, name, width, height, x, y, callback):
        # Crea un botón con un nombre específico, tamaño y posición, y lo conecta a una función de devolución de llamada.
        button = QPushButton(self)
        button.setText(name)
        button.setGeometry(x, y, width, height)
        button.clicked.connect(callback)

    def _create_label(self, text, x, y):
        # Crea una etiqueta con un texto específico y la coloca en una posición determinada.
        label = QLabel(self)
        label.setText(text)
        label.setFont(self.font_arial)
        label.move(x, y)

    def _create_input(self, width, x, y, is_password=False):
        # Crea un campo de entrada con un ancho específico y lo coloca en una posición determinada.
        # Si se especifica 'is_password' como True, se configurará el modo de eco para mostrar los caracteres como contraseñas.
        input_field = QLineEdit(self)
        input_field.resize(width, 24)
        input_field.move(x, y)
        if is_password:
            input_field.setEchoMode(QLineEdit.EchoMode.Password)
        return input_field

    def check_view_pass(self) -> None:
        # Crea una casilla de verificación "Ver contraseña" y la coloca en una posición específica.
        self.check_view_password = QCheckBox(self)
        self.check_view_password.setText("View Password")
        self.check_view_password.move(90, 110)
        self.check_view_password.toggled.connect(self.show_view_password)

    def show_view_password(self, clicked):
        # Esta función se activa cuando se hace clic en la casilla de verificación "Ver contraseña".
        # Implementa la lógica para mostrar la contraseña si se marca la casilla de verificación.
        if clicked:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Normal
            )
        else:
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Password
            )

    def init_main_view(self):
        # Inicializa la vista principal después de que el usuario haya iniciado sesión correctamente.
        pass

    def init_register_user(self):
        # Inicializa la vista de registro de usuario para permitir a los usuarios nuevos registrarse en el sistema.
        new_user = RegisterUserView()
        new_user.show()


    def generate_form(self):
        # Inicializa la generación del formulario de inicio de sesión.
        self.is_logged = False

        # Crea la etiqueta "Usuario" y el campo de entrada correspondiente.
        self._create_label("User:", 20, 54)
        self.user_input = self._create_input(250, 90, 50)

        # Crea la etiqueta "Contraseña" y el campo de entrada correspondiente con modo de eco de contraseña.
        self._create_label("Password:", 20, 90)
        self.password_input = self._create_input(250, 90, 82, is_password=True)

        # Agrega la casilla de verificación "Ver contraseña".
        self.check_view_pass()

        # Crea botones de "Login" y "Registro" y los coloca en la ventana.
        self._login_and_register_button(
            "Login", 320, 24, 20, 140, self.init_main_view)
        self._login_and_register_button(
            "Register", 320, 24, 20, 180, self.init_register_user)


def main():
    # Inicializa la aplicación y muestra la ventana de inicio de sesión.
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
