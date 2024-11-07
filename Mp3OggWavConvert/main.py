from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QComboBox, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon, QFont
import sys
from config import WND_WIDTH, WND_HEIGHT, SIZE, FNT_SIZE, BORDER_W, FONT, TITLE, ICON, HELP
from convert import AudioConverter
from enumerations import FORMATS
from saveload import SaveLoad


class Converter(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        icon: QIcon = QIcon(ICON)
        self.setFixedSize(WND_WIDTH, WND_HEIGHT)
        self.setWindowTitle(TITLE)
        self.setWindowIcon(icon)
        self.converter: AudioConverter = AudioConverter()
        
        # Window
        self.wnd: QWidget = QWidget(self)
        self.wnd.setFixedSize(WND_WIDTH, WND_HEIGHT)
        self.layout: QGridLayout = QGridLayout()
        
        # Style
        border: str = f'border: {BORDER_W}px solid black;'
        font: QFont = QFont(FONT, FNT_SIZE)
        
        # Label help
        hlp_txt: str = SaveLoad.load_file(HELP)
        hlp_sizes: tuple[int, int] = WND_WIDTH, SIZE * 3
        self.hlp_lbl: QLabel = QLabel(self.wnd)
        self.hlp_lbl.setText(hlp_txt)
        self.hlp_lbl.setFont(font)
        self.hlp_lbl.setStyleSheet(border)
        self.hlp_lbl.setFixedSize(hlp_sizes[0], hlp_sizes[1])
        self.layout.addWidget(self.hlp_lbl, 0, 0)
        
        # Input
        inp_txt: str = 'Input'
        inp_sizes: tuple[int, int] = SIZE * 4, SIZE * 2
        self.lbl_inp: QLabel = QLabel(self.wnd)
        self.lbl_inp.setText(inp_txt)
        self.lbl_inp.setFont(font)
        self.lbl_inp.setStyleSheet(border)
        self.lbl_inp.setFixedSize(inp_sizes[0], inp_sizes[1])
        self.layout.addWidget(self.lbl_inp, 1, 0)
        cb_sizes: tuple[int, int] = SIZE * 3, SIZE * 2
        self.cb_inp: QComboBox = QComboBox(self.wnd)
        self.cb_inp.addItems(FORMATS)
        self.cb_inp.setFixedSize(cb_sizes[0], cb_sizes[1])
        self.cb_inp.setFont(font)
        self.layout.addWidget(self.cb_inp, 1, 1)
        
        # Output
        out_txt: str = 'Output'
        out_sizes: tuple[int, int] = SIZE * 4, SIZE * 2
        self.lbl_out: QLabel = QLabel(self.wnd)
        self.lbl_out.setText(out_txt)
        self.lbl_out.setFont(font)
        self.lbl_out.setStyleSheet(border)
        self.lbl_out.setFixedSize(out_sizes[0], out_sizes[1])
        self.layout.addWidget(self.lbl_out, 1, 2)
        self.cb_out: QComboBox = QComboBox(self.wnd)
        self.cb_out.addItems(FORMATS)
        self.cb_out.setFont(font)
        self.cb_out.setFixedSize(cb_sizes[0], cb_sizes[1])
        self.layout.addWidget(self.cb_out, 1, 3)
        
        # Button confirm
        btn1_txt: str = 'Confirm'
        btn1_sizes: tuple[int, int] = SIZE * 4, SIZE * 2
        self.btn_confirm: QPushButton = QPushButton(self.wnd)
        self.btn_confirm.setText(btn1_txt)
        self.btn_confirm.setFont(font)
        self.btn_confirm.setFixedSize(btn1_sizes[0], btn1_sizes[1])
        self.btn_confirm.clicked.connect(self.convert)
        self.layout.addWidget(self.btn_confirm, 1, 4)
        
        # Button quit
        btn2_txt: str = 'Quit'
        btn2_sizes: tuple[int, int] = WND_WIDTH, SIZE * 2
        self.btn_quit: QPushButton = QPushButton(self.wnd)
        self.btn_quit.setText(btn2_txt)
        self.btn_quit.setFont(font)
        self.btn_quit.setFixedSize(btn2_sizes[0], btn2_sizes[1])
        self.btn_quit.clicked.connect(self.quit)
        self.layout.addWidget(self.btn_quit, 2, 0)
        
        self.wnd.setLayout(self.layout)
    
    def convert(self) -> None:
        self.converter.inp = self.cb_inp.currentIndex()
        self.converter.out = self.cb_out.currentIndex()
        self.converter.convert()
    
    def quit(self) -> None:
        self.wnd.destroy()
        self.destroy()
        QApplication.quit()


if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    conv: Converter = Converter()
    conv.show()
    sys.exit(app.exec_())
        