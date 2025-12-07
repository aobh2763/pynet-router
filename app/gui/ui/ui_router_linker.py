from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QSpinBox, QWidget)

class UI_RouterLinker(object):
    def setupUi(self, router_linker):
        if not router_linker.objectName():
            router_linker.setObjectName(u"router_linker")
        router_linker.resize(640, 360)
        self.buttonBox = QDialogButtonBox(router_linker)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 320, 621, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(router_linker)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 621, 71))
        self.label_2 = QLabel(router_linker)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 120, 141, 41))
        self.label_3 = QLabel(router_linker)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 180, 141, 41))
        self.router_a_input = QSpinBox(router_linker)
        self.router_a_input.setObjectName(u"router_a_input")
        self.router_a_input.setGeometry(QRect(150, 120, 471, 41))
        self.router_a_input.setMaximum(99999)
        self.router_b_input = QSpinBox(router_linker)
        self.router_b_input.setObjectName(u"router_b_input")
        self.router_b_input.setGeometry(QRect(150, 180, 471, 41))
        self.router_b_input.setMinimum(0)
        self.router_b_input.setMaximum(99999)
        self.error_label = QLabel(router_linker)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(20, 320, 401, 31))
        self.cost_input = QSpinBox(router_linker)
        self.cost_input.setObjectName(u"cost_input")
        self.cost_input.setGeometry(QRect(100, 240, 521, 41))
        self.cost_input.setMinimum(1)
        self.cost_input.setMaximum(99999)
        self.cost_input.setValue(1)
        self.label_4 = QLabel(router_linker)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 240, 141, 41))

        self.retranslateUi(router_linker)
        self.buttonBox.accepted.connect(router_linker.accept)
        self.buttonBox.rejected.connect(router_linker.reject)

        QMetaObject.connectSlotsByName(router_linker)
    # setupUi

    def retranslateUi(self, router_linker):
        router_linker.setWindowTitle(QCoreApplication.translate("router_linker", u"Router Linker", None))
        self.label.setText(QCoreApplication.translate("router_linker", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Router Linker</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("router_linker", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Router A :</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("router_linker", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Router B :</span></p></body></html>", None))
        self.error_label.setText("")
        self.label_4.setText(QCoreApplication.translate("router_linker", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Cost :</span></p></body></html>", None))
    # retranslateUi