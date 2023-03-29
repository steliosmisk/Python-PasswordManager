import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QEventLoop


# Function to show or hide the password
def show_pass(password):
    if password.echoMode() == QLineEdit.Password:
        password.setEchoMode(QLineEdit.Normal)
    else:
        password.setEchoMode(QLineEdit.Password)
        
def check_errors(app, name, mail, password):
    if len(app.text()) == 0:
        QMessageBox.critical(None, "ERROR","ENTER A VALID NAME")
    elif len(password.text()) == 0:
        QMessageBox.critical(None, "ERROR","ENTER A VALID PASSWORD")
    elif len(name.text()) == 0:
        QMessageBox.critical(None, "ERROR","ENTER A VALID USERNAME")
    elif len(mail.text()) == 0:
        QMessageBox.critical(None, "ERROR","ENTER A VALID MAIL")
    else:
        save_file.clicked.connect(lambda: confirm(app, name,  mail, password))
        
def confirm(app, name, mail, password):
        # Create the main window
        display = QMainWindow()
        display.setWindowTitle('Save File')
        display.setFont(QFont('Courier', 12))
        display.resize(300, 300)

        # Create the widgets
        label = QLabel('NAME THE FILE')
        name_file = QLineEdit()
        name_file.setPlaceholderText('ENTER THE NAME OF THE FILE')
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        button = QPushButton('CONFIRM SAVE')

        def save_file():
            file_name = f'{name_file.text()}.txt'
            if file_name:
                if os.path.isfile(file_name):
                    with open(file_name, 'a') as file:
                        file.write("\n")
                        file.write(f"{f'NAME: {app.text().upper()}'}\n")
                        file.write(f"{f'USERNAME: {name.text()}'}\n")
                        file.write(f"{f'E-MAIL: {mail.text()}'}\n")
                        file.write(f"{f'PASSWORD: {password.text()}'}\n")
                else:
                    with open(file_name, 'w') as file:
                        file.write(f"{f'NAME: {app.text().upper()}'}\n")
                        file.write(f"{f'USERNAME: {name.text()}'}\n")
                        file.write(f"{f'E-MAIL: {mail.text()}'}\n")
                        file.write(f"{f'PASSWORD: {password.text()}'}\n")
                path = os.path.abspath(file_name)  # get absolute path of file
                QMessageBox.information(None, 'Success', f'saved in the path: {path}')
                sys.exit()

        button.clicked.connect(save_file)
        name_file.returnPressed.connect(save_file)


         # Create the layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        display.setLayout(layout)

        # Create a central widget, set the layout, and set it to the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        display.setCentralWidget(central_widget)
        display.show()

        # Create the layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(name_file)
        layout.addWidget(button)

        layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        display.setLayout(layout)

        # Create a central widget, set the layout, and set it to the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        display.setCentralWidget(central_widget)

        # Start an event loop to keep the window open
        loop = QEventLoop()
        while display.isVisible():
                loop.processEvents()

        # Clean up the event loop
        loop.deleteLater()

        # Create the layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        display.setLayout(layout)


        # Show the window
        display.show()

        # Clean up the event loop
        loop.deleteLater()


# Create the application and main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Password Manager by @SteliosMisk")
window.setGeometry(300, 300, 300, 300)

# Add the widgets to the main window
title_font = QFont('Arial', 16, QFont.Bold)
title_label = QLabel("PASSWORD MANAGER")
title_label.setFont(title_font)

app_font = QFont('Arial', 13)
naming_application_label = QLabel("WEBSITE/APP:")
naming_application_label.setFont(app_font)

entering_info = QLineEdit()
entering_info.setPlaceholderText("Enter website name or an app")
entering_info.setFont(app_font)

name_application_label = QLabel("USERNAME:")
name_application_label.setFont(app_font)

name = QLineEdit()
name.setPlaceholderText("Enter your username")
name.setFont(app_font)

email_application_label = QLabel("E-MAIL:")
email_application_label.setFont(app_font)

email = QLineEdit()
email.setPlaceholderText("Enter the e-mail:")
email.setFont(app_font)


password_application_label = QLabel("PASSWORD:")
password_application_label.setFont(app_font)

password = QLineEdit()
password.setPlaceholderText("Enter a password")
password.setEchoMode(QLineEdit.Password)
password.setFont(app_font)


show_password_button = QPushButton("SHOW PASSWORD")
show_password_button.clicked.connect(lambda: show_pass(password))
save_file = QPushButton("Save")
save_file.clicked.connect(lambda: check_errors(entering_info, name, email, password))


widgets_layout = QVBoxLayout()
widgets_layout.addWidget(title_label, alignment=Qt.AlignTop | Qt.AlignHCenter)
widgets_layout.addWidget(naming_application_label)
widgets_layout.addWidget(entering_info)
widgets_layout.addWidget(password_application_label)
widgets_layout.addWidget(password)
widgets_layout.addWidget(name_application_label)
widgets_layout.addWidget(name)
widgets_layout.addWidget(email_application_label)
widgets_layout.addWidget(email)
widgets_layout.addWidget(show_password_button)
widgets_layout.addWidget(save_file)
window.setLayout(widgets_layout)

# Show the main window
window.show()
sys.exit(app.exec_())
