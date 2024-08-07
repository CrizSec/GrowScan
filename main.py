#================================================
#       This Tool is Created By NetCat_^.^      =
#               aKa @Cr1zSec_                   =
#              version 1.5.0                    =
#                                               =
#       Also see the creator of nmap            =
#           at https://nmap.org                 =
#                                               =
#       Thanks for using this tool OwO          =
#================================================

from PyQt5 import QtCore, QtGui, QtWidgets
from script.set_command import command


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 737)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(950, 576))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setStyleSheet("QFrame {\n"
"    background: rgb(112, 112, 112);\n"
"}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.main_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setSpacing(9)
        self.main_layout.setObjectName("main_layout")
        self.frame_kiri = QtWidgets.QFrame(self.main_frame)
        self.frame_kiri.setStyleSheet("QFrame{\n"
"    background: rgb(77, 77, 77);\n"
"}")
        self.frame_kiri.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_kiri.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_kiri.setObjectName("frame_kiri")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_kiri)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.result_frame = QtWidgets.QFrame(self.frame_kiri)
        self.result_frame.setStyleSheet("QFrame {\n"
"    background: rgb(112, 112, 112);\n"
"}")
        self.result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_frame.setObjectName("result_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.result_frame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.result_text = QtWidgets.QTextEdit(self.result_frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.result_text.setFont(font)
        self.result_text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.result_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_text.setStyleSheet("QTextEdit{\n"
"    color: rgb(0, 255, 0)\n"
"}")
        self.result_text.setReadOnly(True)
        self.result_text.setOverwriteMode(False)
        self.result_text.setObjectName("result_text")
        self.verticalLayout_8.addWidget(self.result_text)
        self.verticalLayout_2.addWidget(self.result_frame)
        self.target_frame = QtWidgets.QFrame(self.frame_kiri)
        self.target_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.target_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.target_frame.setObjectName("target_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.target_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.target_label = QtWidgets.QLabel(self.target_frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.target_label.setFont(font)
        self.target_label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.target_label.setObjectName("target_label")
        self.verticalLayout_3.addWidget(self.target_label)
        self.target_input_frame = QtWidgets.QFrame(self.target_frame)
        self.target_input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.target_input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.target_input_frame.setObjectName("target_input_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.target_input_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.target_input = QtWidgets.QLineEdit(self.target_input_frame)
        self.target_input.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.target_input.setFont(font)
        self.target_input.setStyleSheet("QLineEdit {\n"
"  border-radius: 5;\n"
"  padding-left: 5;\n"
"}")
        self.target_input.setObjectName("target_input")
        self.horizontalLayout_2.addWidget(self.target_input)
        self.submit_scan = QtWidgets.QPushButton(self.target_input_frame)
        # connect function
        self.submit_scan.clicked.connect(self.run_command)
        self.submit_scan.setMinimumSize(QtCore.QSize(142, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.submit_scan.setFont(font)
        self.submit_scan.setStyleSheet("QPushButton {\n"
"    background: DodgerBlue;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 8px 20px;\n"
"    border: 1px solid #0056b3;\n"
"    min-width: 100px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #1e90ff;\n"
"    border: 1px solid #007acc;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #0056b3;\n"
"    border: 1px solid #004080;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #b0c4de;\n"
"    color: #696969;\n"
"    border: 1px solid #a9a9a9;\n"
"}\n"
"")
        self.submit_scan.setObjectName("submit_scan")
        self.horizontalLayout_2.addWidget(self.submit_scan)
        self.verticalLayout_3.addWidget(self.target_input_frame)
        self.verticalLayout_2.addWidget(self.target_frame)
        self.main_layout.addWidget(self.frame_kiri)
        self.frame_kanan = QtWidgets.QFrame(self.main_frame)
        self.frame_kanan.setMinimumSize(QtCore.QSize(200, 536))
        self.frame_kanan.setStyleSheet("QFrame{\n"
"    background: rgb(77, 77, 77);\n"
"}")
        self.frame_kanan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_kanan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_kanan.setLineWidth(0)
        self.frame_kanan.setObjectName("frame_kanan")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_kanan)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(self.frame_kanan)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setText("")
        self.logo.setTextFormat(QtCore.Qt.AutoText)
        self.logo.setPixmap(QtGui.QPixmap(":/logo/assets/logo-01.svg"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setWordWrap(False)
        self.logo.setIndent(-1)
        self.logo.setOpenExternalLinks(False)
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo)
        self.checkbox_frame = QtWidgets.QFrame(self.frame_kanan)
        self.checkbox_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.checkbox_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.checkbox_frame.setLineWidth(1)
        self.checkbox_frame.setObjectName("checkbox_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.checkbox_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkerLayout = QtWidgets.QGridLayout()
        self.checkerLayout.setContentsMargins(9, -1, -1, -1)
        self.checkerLayout.setObjectName("checkerLayout")
        self.v = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.v.sizePolicy().hasHeightForWidth())
        self.v.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.v.setFont(font)
        self.v.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.v.setAutoExclusive(False)
        self.v.setObjectName("v")
        self.checkerLayout.addWidget(self.v, 3, 1, 1, 1)
        self.sV = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sV.sizePolicy().hasHeightForWidth())
        self.sV.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sV.setFont(font)
        self.sV.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.sV.setAutoExclusive(False)
        self.sV.setObjectName("sV")
        self.checkerLayout.addWidget(self.sV, 0, 0, 1, 1)
        self.sS = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sS.sizePolicy().hasHeightForWidth())
        self.sS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sS.setFont(font)
        self.sS.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.sS.setAutoExclusive(False)
        self.sS.setObjectName("sS")
        self.checkerLayout.addWidget(self.sS, 1, 0, 1, 1)
        self.PO = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PO.sizePolicy().hasHeightForWidth())
        self.PO.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.PO.setFont(font)
        self.PO.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.PO.setAutoExclusive(False)
        self.PO.setObjectName("PO")
        self.checkerLayout.addWidget(self.PO, 4, 1, 1, 1)
        self.sL = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sL.sizePolicy().hasHeightForWidth())
        self.sL.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sL.setFont(font)
        self.sL.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.sL.setAutoExclusive(False)
        self.sL.setObjectName("sL")
        self.checkerLayout.addWidget(self.sL, 3, 0, 1, 1)
        self.G = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.G.sizePolicy().hasHeightForWidth())
        self.G.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.G.setFont(font)
        self.G.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.G.setAutoExclusive(False)
        self.G.setObjectName("G")
        self.checkerLayout.addWidget(self.G, 4, 2, 1, 1)
        self.A = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A.sizePolicy().hasHeightForWidth())
        self.A.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.A.setFont(font)
        self.A.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.A.setAutoExclusive(False)
        self.A.setObjectName("A")
        self.checkerLayout.addWidget(self.A, 0, 2, 1, 1)
        self.F = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F.sizePolicy().hasHeightForWidth())
        self.F.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.F.setFont(font)
        self.F.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.F.setAutoExclusive(False)
        self.F.setObjectName("F")
        self.checkerLayout.addWidget(self.F, 3, 2, 1, 1)
        self.sY = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sY.sizePolicy().hasHeightForWidth())
        self.sY.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sY.setFont(font)
        self.sY.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.sY.setAutoExclusive(False)
        self.sY.setObjectName("sY")
        self.checkerLayout.addWidget(self.sY, 4, 0, 1, 1)
        self.sO = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sO.sizePolicy().hasHeightForWidth())
        self.sO.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sO.setFont(font)
        self.sO.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.sO.setAutoExclusive(False)
        self.sO.setObjectName("sO")
        self.checkerLayout.addWidget(self.sO, 1, 1, 1, 1)
        self.d = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d.sizePolicy().hasHeightForWidth())
        self.d.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.d.setFont(font)
        self.d.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.d.setAutoExclusive(False)
        self.d.setObjectName("d")
        self.checkerLayout.addWidget(self.d, 1, 2, 1, 1)
        self.O = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.O.sizePolicy().hasHeightForWidth())
        self.O.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.O.setFont(font)
        self.O.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.O.setAutoExclusive(False)
        self.O.setObjectName("O")
        self.checkerLayout.addWidget(self.O, 2, 2, 1, 1)
        self.sC = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sC.sizePolicy().hasHeightForWidth())
        self.sC.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sC.setFont(font)
        self.sC.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.sC.setAutoExclusive(False)
        self.sC.setObjectName("sC")
        self.checkerLayout.addWidget(self.sC, 0, 1, 1, 1)
        self.sU = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sU.sizePolicy().hasHeightForWidth())
        self.sU.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sU.setFont(font)
        self.sU.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.sU.setAutoExclusive(False)
        self.sU.setObjectName("sU")
        self.checkerLayout.addWidget(self.sU, 2, 0, 1, 1)
        self.Pn = QtWidgets.QRadioButton(self.checkbox_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pn.sizePolicy().hasHeightForWidth())
        self.Pn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Pn.setFont(font)
        self.Pn.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.Pn.setAutoExclusive(False)
        self.Pn.setObjectName("Pn")
        self.checkerLayout.addWidget(self.Pn, 2, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.checkerLayout)
        self.verticalLayout.addWidget(self.checkbox_frame)
        self.input_combo_layout = QtWidgets.QVBoxLayout()
        self.input_combo_layout.setObjectName("input_combo_layout")
        self.Thread_option = QtWidgets.QFrame(self.frame_kanan)
        self.Thread_option.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Thread_option.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Thread_option.setObjectName("Thread_option")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Thread_option)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Thread_label = QtWidgets.QLabel(self.Thread_option)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Thread_label.setFont(font)
        self.Thread_label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Thread_label.setObjectName("Thread_label")
        self.verticalLayout_5.addWidget(self.Thread_label)
        self.thread_frame = QtWidgets.QFrame(self.Thread_option)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.thread_frame.setFont(font)
        self.thread_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.thread_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thread_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thread_frame.setObjectName("thread_frame")
        self.Threads_layout = QtWidgets.QHBoxLayout(self.thread_frame)
        self.Threads_layout.setContentsMargins(0, 0, 0, 0)
        self.Threads_layout.setSpacing(0)
        self.Threads_layout.setObjectName("Threads_layout")
        self.Thread_radio = QtWidgets.QRadioButton(self.thread_frame)
        self.Thread_radio.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.Thread_radio.setText("")
        self.Thread_radio.setObjectName("Thread_radio")
        self.Threads_layout.addWidget(self.Thread_radio)
        self.Thread_combox = QtWidgets.QComboBox(self.thread_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Thread_combox.sizePolicy().hasHeightForWidth())
        self.Thread_combox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Thread_combox.setFont(font)
        self.Thread_combox.setStyleSheet("QComboBox {\n"
"    background: #ff6565;\n"
"    color: white; \n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"    border: 1px solid #ff4343;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #ff4343;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #333333;\n"
"    color: white;\n"
"    border: 1px solid #ff4343;\n"
"    selection-background-color: #ff6565;\n"
"    selection-color: white;\n"
"}\n"
"")
        self.Thread_combox.setObjectName("Thread_combox")
        self.Thread_combox.addItem("")
        self.Thread_combox.addItem("")
        self.Thread_combox.addItem("")
        self.Thread_combox.addItem("")
        self.Thread_combox.addItem("")
        self.Thread_combox.addItem("")
        self.Threads_layout.addWidget(self.Thread_combox)
        self.Threads_layout.setStretch(1, 1)
        self.verticalLayout_5.addWidget(self.thread_frame)
        self.input_combo_layout.addWidget(self.Thread_option)
        self.additional_option = QtWidgets.QFrame(self.frame_kanan)
        self.additional_option.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.additional_option.setFrameShadow(QtWidgets.QFrame.Raised)
        self.additional_option.setObjectName("additional_option")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.additional_option)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.additional_title = QtWidgets.QLabel(self.additional_option)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.additional_title.setFont(font)
        self.additional_title.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.additional_title.setObjectName("additional_title")
        self.verticalLayout_11.addWidget(self.additional_title)
        self.additional_frame = QtWidgets.QFrame(self.additional_option)
        self.additional_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.additional_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.additional_frame.setObjectName("additional_frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.additional_frame)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.additional_radio = QtWidgets.QRadioButton(self.additional_frame)
        self.additional_radio.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.additional_radio.setText("")
        self.additional_radio.setObjectName("additional_radio")
        self.horizontalLayout_10.addWidget(self.additional_radio)
        self.additional_combox = QtWidgets.QComboBox(self.additional_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.additional_combox.sizePolicy().hasHeightForWidth())
        self.additional_combox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.additional_combox.setFont(font)
        self.additional_combox.setStyleSheet("QComboBox {\n"
"    background: #ff6565;\n"
"    color: white; \n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"    border: 1px solid #ff4343;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #ff4343;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #333333;\n"
"    color: white;\n"
"    border: 1px solid #ff4343;\n"
"    selection-background-color: #ff6565;\n"
"    selection-color: white;\n"
"}\n"
"")
        self.additional_combox.setObjectName("additional_combox")
        self.additional_combox.addItem("")
        self.additional_combox.addItem("")
        self.additional_combox.addItem("")
        self.additional_combox.addItem("")
        self.additional_combox.addItem("")
        self.additional_combox.addItem("")
        self.horizontalLayout_10.addWidget(self.additional_combox)
        self.horizontalLayout_10.setStretch(1, 1)
        self.verticalLayout_11.addWidget(self.additional_frame)
        self.input_combo_layout.addWidget(self.additional_option)
        self.script_options = QtWidgets.QFrame(self.frame_kanan)
        self.script_options.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.script_options.setFrameShadow(QtWidgets.QFrame.Raised)
        self.script_options.setObjectName("script_options")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.script_options)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.script_label = QtWidgets.QLabel(self.script_options)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.script_label.setFont(font)
        self.script_label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.script_label.setObjectName("script_label")
        self.verticalLayout_9.addWidget(self.script_label)
        self.script_frame = QtWidgets.QFrame(self.script_options)
        self.script_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.script_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.script_frame.setObjectName("script_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.script_frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.script_radio = QtWidgets.QRadioButton(self.script_frame)
        self.script_radio.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.script_radio.setText("")
        self.script_radio.setObjectName("script_radio")
        self.horizontalLayout_8.addWidget(self.script_radio)
        self.script_combox = QtWidgets.QComboBox(self.script_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.script_combox.sizePolicy().hasHeightForWidth())
        self.script_combox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.script_combox.setFont(font)
        self.script_combox.setStyleSheet("QComboBox {\n"
"    background: DodgerBlue;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"    border: 1px solid #0056b3;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #0056b3;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: #333333;\n"
"    color: white;\n"
"    border: 1px solid #0056b3;\n"
"    selection-background-color: DodgerBlue;\n"
"    selection-color: white;\n"
"}\n"
"")
        self.script_combox.setObjectName("script_combox")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.script_combox.addItem("")
        self.horizontalLayout_8.addWidget(self.script_combox)
        self.horizontalLayout_8.setStretch(1, 1)
        self.verticalLayout_9.addWidget(self.script_frame)
        self.input_combo_layout.addWidget(self.script_options)
        self.output_option = QtWidgets.QFrame(self.frame_kanan)
        self.output_option.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output_option.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_option.setObjectName("output_option")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.output_option)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.output_label = QtWidgets.QLabel(self.output_option)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.output_label.setFont(font)
        self.output_label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.output_label.setObjectName("output_label")
        self.verticalLayout_7.addWidget(self.output_label)
        self.output_frame = QtWidgets.QFrame(self.output_option)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.output_frame.setFont(font)
        self.output_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_frame.setObjectName("output_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.output_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.output_radio = QtWidgets.QRadioButton(self.output_frame)
        self.output_radio.setStyleSheet("QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: rgb(85, 255, 0);\n"
"}")
        self.output_radio.setText("")
        self.output_radio.setObjectName("output_radio")
        self.horizontalLayout_6.addWidget(self.output_radio)
        self.output_line = QtWidgets.QLineEdit(self.output_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_line.sizePolicy().hasHeightForWidth())
        self.output_line.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.output_line.setFont(font)
        self.output_line.setStyleSheet("QLineEdit {\n"
"    padding-left: 5;\n"
"}")
        self.output_line.setObjectName("output_line")
        self.horizontalLayout_6.addWidget(self.output_line)
        self.verticalLayout_7.addWidget(self.output_frame)
        self.input_combo_layout.addWidget(self.output_option)
        self.verticalLayout.addLayout(self.input_combo_layout)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.main_layout.addWidget(self.frame_kanan)
        self.main_layout.setStretch(0, 4)
        self.main_layout.setStretch(1, 2)
        self.horizontalLayout_3.addLayout(self.main_layout)
        self.horizontalLayout.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def run_command(self):
        # gabungin checkbox
        command(self.sV, self.sC, self.A, self.sS, 
                self.sO, self.d, self.sU, self.Pn, 
                self.O, self.sL, self.v, self.F, 
                self.sY, self.PO, self.G, 
                target_input=self.target_input, 
                thread_combox=self.Thread_combox, 
                script_combox=self.script_combox, 
                additional_combox=self.additional_combox, 
                output_line=self.output_line, 
                result_text=self.result_text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grow Scan"))
        self.result_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00ff00;\">=============</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00ff00;\">GROWSCAN</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00ff00;\">v.1.5.0</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00ff00;\">Author: NetCat_^.^</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#00ff00;\">=============</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#00ff00;\"><br /></p></body></html>"))
        self.target_label.setText(_translate("MainWindow", "Target IP"))
        self.submit_scan.setText(_translate("MainWindow", "Submit"))
        self.v.setText(_translate("MainWindow", "-v"))
        self.sV.setText(_translate("MainWindow", "-sV"))
        self.sS.setText(_translate("MainWindow", "-sS"))
        self.PO.setText(_translate("MainWindow", "-PO"))
        self.sL.setText(_translate("MainWindow", "-sL"))
        self.G.setText(_translate("MainWindow", "-G"))
        self.A.setText(_translate("MainWindow", "-A"))
        self.F.setText(_translate("MainWindow", "-F"))
        self.sY.setText(_translate("MainWindow", "-sY"))
        self.sO.setText(_translate("MainWindow", "-sO"))
        self.d.setText(_translate("MainWindow", "-d"))
        self.O.setText(_translate("MainWindow", "-O"))
        self.sC.setText(_translate("MainWindow", "-sC"))
        self.sU.setText(_translate("MainWindow", "-sU"))
        self.Pn.setText(_translate("MainWindow", "-Pn"))
        self.Thread_label.setText(_translate("MainWindow", "Threads"))
        self.Thread_combox.setItemText(0, _translate("MainWindow", "Select Option"))
        self.Thread_combox.setItemText(1, _translate("MainWindow", "T1"))
        self.Thread_combox.setItemText(2, _translate("MainWindow", "T2"))
        self.Thread_combox.setItemText(3, _translate("MainWindow", "T3"))
        self.Thread_combox.setItemText(4, _translate("MainWindow", "T4"))
        self.Thread_combox.setItemText(5, _translate("MainWindow", "T5"))
        self.additional_title.setText(_translate("MainWindow", "Additional"))
        self.additional_combox.setItemText(0, _translate("MainWindow", "Select Option"))
        self.additional_combox.setItemText(1, _translate("MainWindow", "-p 80"))
        self.additional_combox.setItemText(2, _translate("MainWindow", "-p 1-1000"))
        self.additional_combox.setItemText(3, _translate("MainWindow", "-p 22,80,443"))
        self.additional_combox.setItemText(4, _translate("MainWindow", "-p-"))
        self.additional_combox.setItemText(5, _translate("MainWindow", "--traceroute"))
        self.script_label.setText(_translate("MainWindow", "Script"))
        self.script_combox.setItemText(0, _translate("MainWindow", "Select Option"))
        self.script_combox.setItemText(1, _translate("MainWindow", "ftp-fuzz"))
        self.script_combox.setItemText(2, _translate("MainWindow", "http-fuzz"))
        self.script_combox.setItemText(3, _translate("MainWindow", "dns-brute"))
        self.script_combox.setItemText(4, _translate("MainWindow", "http-wordpress-brute"))
        self.script_combox.setItemText(5, _translate("MainWindow", "http-default-accounts"))
        self.script_combox.setItemText(6, _translate("MainWindow", "ftp-brute"))
        self.script_combox.setItemText(7, _translate("MainWindow", "snmp-brute"))
        self.script_combox.setItemText(8, _translate("MainWindow", "mysql-brute"))
        self.script_combox.setItemText(9, _translate("MainWindow", "smtp-brute"))
        self.script_combox.setItemText(10, _translate("MainWindow", "telnet-brute"))
        self.script_combox.setItemText(11, _translate("MainWindow", "http-brute"))
        self.script_combox.setItemText(12, _translate("MainWindow", "broadcast-dhcp-discover"))
        self.script_combox.setItemText(13, _translate("MainWindow", "broadcast-dns-service-discovery"))
        self.script_combox.setItemText(14, _translate("MainWindow", "broadcast-netbios-master-browser"))
        self.script_combox.setItemText(15, _translate("MainWindow", "http-slowloris"))
        self.script_combox.setItemText(16, _translate("MainWindow", "snmp-info"))
        self.script_combox.setItemText(17, _translate("MainWindow", "banner"))
        self.script_combox.setItemText(18, _translate("MainWindow", "smtp-vrfy"))
        self.script_combox.setItemText(19, _translate("MainWindow", "ftp-vsftpd-backdoor"))
        self.script_combox.setItemText(20, _translate("MainWindow", "http-shellshock"))
        self.script_combox.setItemText(21, _translate("MainWindow", "smb-vuln-ms17-010"))
        self.script_combox.setItemText(22, _translate("MainWindow", "ip-geolocation-geoplugin"))
        self.script_combox.setItemText(23, _translate("MainWindow", "whois-ip"))
        self.script_combox.setItemText(24, _translate("MainWindow", "http-sql-injection"))
        self.script_combox.setItemText(25, _translate("MainWindow", "smtp-open-relay"))
        self.script_combox.setItemText(26, _translate("MainWindow", "smb-brute"))
        self.script_combox.setItemText(27, _translate("MainWindow", "http-malware-host"))
        self.script_combox.setItemText(28, _translate("MainWindow", "smtp-strangeport"))
        self.script_combox.setItemText(29, _translate("MainWindow", "dns-zone-transfer"))
        self.script_combox.setItemText(30, _translate("MainWindow", "http-headers"))
        self.script_combox.setItemText(31, _translate("MainWindow", "ssl-enum-ciphers"))
        self.script_combox.setItemText(32, _translate("MainWindow", "afp-serverinfo"))
        self.script_combox.setItemText(33, _translate("MainWindow", "dns-service-discovery"))
        self.script_combox.setItemText(34, _translate("MainWindow", "finger"))
        self.script_combox.setItemText(35, _translate("MainWindow", "http-vuln-cve2017-5638"))
        self.script_combox.setItemText(36, _translate("MainWindow", "smb-vuln-ms08-067"))
        self.script_combox.setItemText(37, _translate("MainWindow", "ftp-vuln-cve2010-4221"))
        self.output_label.setText(_translate("MainWindow", "Output File"))
        self.output_line.setPlaceholderText(_translate("MainWindow", "example: result/target.txt"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
