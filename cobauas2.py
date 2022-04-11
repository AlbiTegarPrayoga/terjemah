
from fnmatch import translate
import sys
import os
import random
from xml.dom.expatbuilder import parseString
from deep_translator import GoogleTranslator
import gtts
import pyperclip

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaContent,QMediaPlayer


class Translator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        vb = QVBoxLayout()
        self.setLayout(vb)
       
        font = QFont("Times",14)
        self.insert_text = QTextEdit()
        self.insert_text.setFont(font)
        vb.addWidget(self.insert_text)
        
        self.show_translation =  QTextEdit()
        self.show_translation.setFont(font)
        vb.addWidget(self.show_translation)
        
        self.translatebtn = QPushButton("Terjemah")
        self.translatebtn.setFont(font)
        vb.addWidget(self.translatebtn)
        
        self.playsoundbtn = QPushButton("Terjemah Suara")
        self.playsoundbtn.setFont(font)
        vb.addWidget(self.playsoundbtn)
        
        self.copybtn = QPushButton("Salin")
        self.copybtn.setFont(font)
        vb.addWidget(self.copybtn)
        
        self.deletebtn = QPushButton("Hapus")
        self.deletebtn.setFont(font)
        vb.addWidget(self.deletebtn)
        
        self.combo = QComboBox()
        self.combo.setFont(font)
        bahasa = ["English","Arabic","Indonesian","Japanese","Korean","Spainsh","Thai"]
        self.combo.addItems(bahasa)
        self.combo.setEditable(True)
        self.combo.lineEdit().setAlignment(Qt.AlignCenter)
        vb.addWidget(self.combo)
        self.target = {"English":"en","Arabic":"ar","French":"fr","Indonesian":"id","Japanese":"ja","Korean":"ko","Spanish":"es","Thai":"th"}

        self.player = QMediaPlayer()
        self.translatebtn.clicked.connect(self.translate_text)
        self.playsoundbtn.clicked.connect(self.play_sound)
        self.copybtn.clicked.connect(self.copy_text)
        self.deletebtn.clicked.connect(self.translate_text)
    def translate_text(self):
        global mp3
        mp3 = random.randint(10000, 1000000)
        target = self.target[self.combo.currentText()]
        text = self.insert_text.toPlainText()
        translated = GoogleTranslator(source="auto",target=target).translate(text)
        self.show_translation.clear()
        self.show_translation.setText(translated)
        tts = gtts.gTTS(translated,lang=target)
        tts.save(str(mp3)+'.mp3')
        
    def play_sound(self):
        path = os.path.join(os.getcwd(), str(mp3)+".mp3")
        url = QUrl.fromLocalFile(path)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
        
    def copy_text(self):
        global copy, paste
        self.show_translation.copy()
        
        
    def delete_text():
        Translator.setEnabled(False)
        
           
    
def main():
    app = QApplication(sys.argv)
    gui = Translator()
    gui.setGeometry(100,100,500,500)
    gui.setWindowTitle("Penerjemah")
    gui.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()    
    
        
    
        
