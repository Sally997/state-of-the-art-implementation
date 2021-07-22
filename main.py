import os
import random
from os import path
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import os
import sys
from selenium import webdriver
from time import sleep
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog, QWidget, QHBoxLayout
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class Ui_MainWindow(object):
    global inp
    global inp2
    global pathh
    global email
    global number

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        oImage = QImage("C:/Users/Sally/Downloads/collage(3)")
        sImage = oImage.scaled(QSize(1600, 900))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        MainWindow.setPalette(palette)
        # palette_black = QPalette()
        # palette_black.setColor(QPalette.Window, Qt.black)
        # MainWindow.setPalette(palette_black)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(10, 20, 500, 500))
        font = QtGui.QFont()
        font.setPointSize(40)

        self.photo.setFont(font)
        self.photo.setFrameShape(QtWidgets.QFrame.Panel)
        self.photo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.photo.setLineWidth(5)
        self.photo.setMidLineWidth(0)
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.browseFile = QtWidgets.QPushButton(self.centralwidget)
        self.browseFile.setGeometry(QtCore.QRect(550, 550, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.browseFile.setFont(font)
        self.browseFile.setObjectName("browseFile")
        inp2 = self.browseFile.clicked.connect(self.browse_file)
        print(inp2, 'kj', type(inp2))

        ##########################################
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 520, 521, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems([' ','scream.ckpt', 'rain_princess.ckpt', 'udnie.ckpt', 'wave.ckpt', 'wreck.ckpt', 'la_muse.ckpt'])
        self.inp = self.comboBox.currentIndexChanged.connect(self.selectionchange)
        print('inp', self.inp, type(self.inp))
        #########################################

        self.predict = QtWidgets.QPushButton(self.centralwidget)
        self.predict.setGeometry(QtCore.QRect(520, 200, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.predict.setFont(font)
        self.predict.setObjectName("predict")
        self.pathh=self.predict.clicked.connect(self.show_predict)

        self.photo2 = QtWidgets.QLabel(self.centralwidget)
        self.photo2.setGeometry(QtCore.QRect(790, 20, 500, 500))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.photo2.setFont(font)
        self.photo2.setFrameShape(QtWidgets.QFrame.Panel)
        self.photo2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.photo2.setLineWidth(5)
        self.photo2.setScaledContents(True)
        self.photo2.setObjectName("photo2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(720, 550, 521, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        ########################################

        self.label = QtWidgets.QPushButton(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 600, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("Send_Email:")
        self.email = self.label.clicked.connect(self.button_click)
        print("self.email is : ")
        print(self.email)

        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(720, 600, 521, 31))
        self.lineEdit1.setObjectName("lineEdit")

        self.label2 = QtWidgets.QPushButton(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(550, 650, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label2.setFont(font)
        self.label2.setObjectName("Enter_Number:")
        self.number = self.label2.clicked.connect(self.button_click2)
        print("self.number is : ")
        print(self.number)

        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(720, 650, 521, 31))
        self.lineEdit2.setObjectName("lineEdit")

        # connect button to function on_click

        #################################################
        ###############

        ########################################
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.photo.setText(_translate("MainWindow", "INPUT"))
        self.browseFile.setText(_translate("MainWindow", "Browse file"))
        self.predict.setText(_translate("MainWindow", "PREDICT"))
        self.photo2.setText(_translate("MainWindow", "OUTPUT"))
        self.label.setText(_translate("MainWindow", "Send_Email:"))
        self.label2.setText(_translate("MainWindow", "Enter_Number:"))

    def on_click(self):
        textboxValue = self.LineEdit.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.textbox.setText("")

    ########################################################
    def button_click(self):
        # shost is a QString object
        self.email = self.lineEdit1.text()
        strFrom = 'sallyy679@gmail.com'
        
        strTo = str(self.email)
        # Create an instance of MIMEMultipart object, pass 'related' as the constructor parameter.
        msgRoot = MIMEMultipart('related')
        # Set the email subject.
        msgRoot['Subject'] = 'This email contains one image.'
        # Set the email from email address.
        msgRoot['From'] = strFrom
        # Set the email to email address.
        msgRoot['To'] = strTo
        msgAlternative = MIMEMultipart('alternative')
        # Attach the bove object to the root email message.
        msgRoot.attach(msgAlternative)
        # Create a MIMEText object to contains the email Html content. There is also an image in the Html content. The image cid is image1.
        # msgText = MIMEText('<b>This is the <i>HTML</i> content of this email</b> it contains an image.<br><img src="cid:image1"><br>', 'html')
        # Attach the above html content MIMEText object to the msgAlternative object.
        # msgAlternative.attach(msgText)
        # Open a file object to read the image file, the image file is located in the file path it provide.
        fp = open(self.pathh, 'rb')
        # Create a MIMEImage object with the above file object.
        msgImage = MIMEImage(fp.read())
        # Do not forget close the file object after using it.
        fp.close()
        # Add 'Content-ID' header value to the above MIMEImage object to make it refer to the image source (src="cid:image1") in the Html content.
        msgImage.add_header('Content-ID', '<image1>')
        # Attach the MIMEImage object to the email body.
        msgRoot.attach(msgImage)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Login to the SMTP server with username and password.
        server.login('sallyy679@gmail.com', 'password')
        server.sendmail(strFrom, strTo, msgRoot.as_string())
        server.quit()

    def button_click2(self):
        # shost is a QString object
        self.number = self.lineEdit2.text()
        chrom_profile_path = 'user-data-dir=C:/Users/Sally/AppData/Local/Google/Chrome/User Data/wtsp'

        options = webdriver.ChromeOptions()
        options.add_argument(chrom_profile_path)

        driver = webdriver.Chrome(options=options)
        driver.get('https://web.whatsapp.com/')
        sleep(25)
        name = str(self.number)
        # filepath = 'C:/Users/Sally/Desktop/artistic style/picasso.jpg'

        

        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()

        attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
        attachment_box.click()

        image_box = driver.find_element_by_xpath(
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(self.pathh)

        sleep(5)
        # <span data-testid="send" data-icon="send" class="">
        send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
        send_button.click()
        sleep(25)
        driver.close()

        #########################################3

    def browse_file(self):
        #directory = QtWidgets.QFileDialog.getOpenFileName(None, "Browse File", "", "PNG (*.PNG *.png")[0]
        directory = QtWidgets.QFileDialog.getOpenFileName(None, "Browse File", "", "JPG (*.JPG *.jpg")[0]
        self.inp2 = directory
        print(self.inp2)
        pixmap = QtGui.QPixmap(directory)
        self.photo.setPixmap(pixmap.scaled(self.photo.size()))
        self.lineEdit.setText('{}'.format(directory))

    def _set_text(self, text):
        return text

    def selectionchange(self):
        self.inp = self.comboBox.currentText()
        print('inp', self.inp)

    def show_predict(self):
       

        rands = []
        rand = random.randint(0, 10000000)
        rands.append(rand)
        while rand in rands:
            rand = random.randint(0, 10000000)
        rands.append(rand)
        # print(rand)
        filename = "output" + str(rand) + ".jpg"
        print(filename)
        self.pathh = path.join('C:/Users/Sally/Desktop/artisticstyle/', filename)
        print(self.pathh)
        cmd = "python evaluate.py --checkpoint " + self.inp + " --in-path " + self.inp2 + " --out-path " + self.pathh
        os.system(cmd)
        ##################################################################
        # creating watermark
        image = Image.open(self.pathh)
        # text Watermark
        x, y = image.size
        
        watermark_image = image.copy()
        
        draw = ImageDraw.Draw(watermark_image)
        
        font = ImageFont.truetype("arial.ttf", 20)
        draw.text((0, 0), "ITExhibition", (255, 255, 255), font=font)
        watermark_image.save(self.pathh)

        #######################################################
        self.photo2.setPixmap(QtGui.QPixmap(self.pathh))
        
        # self.photo2.setText("Haiii")





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# os.system('python evaluate.py --checkpoint rain_princess.ckpt \
#   --in-path C:/Users/Sally/Desktop/artisticstyle/licensed-image.jpg \
#   --out-path C:/Users/Sally/Desktop/artisticstyle/output2.jpg')

# inp=input('choose from the following: scream, rain_princess, undie, wave, wreck, or la muse ')
# inp2="C:/Users/Sally/Desktop/artisticstyle/licensed-image.jpg"
# inp3=input('output pth')

# print(cmd)


# # import pywhatkit
# # #pywhatkit.sendwhatmsg('+09647713517294','hi, this is python code sending messages',4,16)
# # pywhatkit.
# #
# # pywhatkit.sendwhatmsg_instantly('+09647713517294','hi, this is python code sending messages')


