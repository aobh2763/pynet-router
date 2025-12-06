from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class UI_NetworkCreator(object):
    def setupUi(self, network_creator):
        if not network_creator.objectName():
            network_creator.setObjectName(u"network_creator")
        network_creator.resize(640, 240)
        self.buttonBox = QDialogButtonBox(network_creator)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 200, 621, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(network_creator)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 621, 51))
        self.label_2 = QLabel(network_creator)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 110, 91, 31))
        self.name_input = QLineEdit(network_creator)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setGeometry(QRect(110, 110, 511, 31))
        self.name_input.setMaxLength(128)
        self.error_label = QLabel(network_creator)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(20, 200, 411, 31))

        self.retranslateUi(network_creator)
        self.buttonBox.accepted.connect(network_creator.accept)
        self.buttonBox.rejected.connect(network_creator.reject)

        QMetaObject.connectSlotsByName(network_creator)
    # setupUi

    def retranslateUi(self, network_creator):
        network_creator.setWindowTitle(QCoreApplication.translate("network_creator", u"Network Creator", None))
        self.label.setText(QCoreApplication.translate("network_creator", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Network Creator</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("network_creator", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Name :</span></p></body></html>", None))
        self.error_label.setText("")
    # retranslateUi