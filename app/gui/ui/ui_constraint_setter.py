from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QSlider, QSpinBox,
    QWidget)

class UI_ConstraintSetter(object):
    def setupUi(self, ConstraintSetter):
        if not ConstraintSetter.objectName():
            ConstraintSetter.setObjectName(u"ConstraintSetter")
        ConstraintSetter.setEnabled(True)
        ConstraintSetter.resize(640, 400)
        self.buttonBox = QDialogButtonBox(ConstraintSetter)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 360, 621, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(ConstraintSetter)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(14, 15, 611, 61))
        self.label_2 = QLabel(ConstraintSetter)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 120, 101, 41))
        self.label_3 = QLabel(ConstraintSetter)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 180, 161, 41))
        self.label_4 = QLabel(ConstraintSetter)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 240, 281, 41))
        self.source_input = QSpinBox(ConstraintSetter)
        self.source_input.setObjectName(u"source_input")
        self.source_input.setGeometry(QRect(131, 121, 491, 41))
        self.source_input.setMaximum(99999)
        self.destination_input = QSpinBox(ConstraintSetter)
        self.destination_input.setObjectName(u"destination_input")
        self.destination_input.setGeometry(QRect(190, 180, 431, 41))
        self.destination_input.setMaximum(99999)
        self.label_5 = QLabel(ConstraintSetter)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 290, 121, 51))
        self.security_input = QSpinBox(ConstraintSetter)
        self.security_input.setObjectName(u"security_input")
        self.security_input.setGeometry(QRect(300, 240, 321, 41))
        self.security_input.setMinimum(1)
        self.security_input.setMaximum(5)
        self.label_6 = QLabel(ConstraintSetter)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 300, 101, 31))
        self.label_7 = QLabel(ConstraintSetter)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(560, 300, 61, 31))
        self.firewall_input = QSlider(ConstraintSetter)
        self.firewall_input.setObjectName(u"firewall_input")
        self.firewall_input.setGeometry(QRect(230, 300, 321, 31))
        self.firewall_input.setMaximum(1)
        self.firewall_input.setOrientation(Qt.Horizontal)

        self.retranslateUi(ConstraintSetter)
        self.buttonBox.accepted.connect(ConstraintSetter.accept)
        self.buttonBox.rejected.connect(ConstraintSetter.reject)

        QMetaObject.connectSlotsByName(ConstraintSetter)
    # setupUi

    def retranslateUi(self, ConstraintSetter):
        ConstraintSetter.setWindowTitle(QCoreApplication.translate("ConstraintSetter", u"Constraint Setter", None))
        self.label.setText(QCoreApplication.translate("ConstraintSetter", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Constraint Setter</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("ConstraintSetter", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Source :</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("ConstraintSetter", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Destination :</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("ConstraintSetter", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Security Requirement :</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("ConstraintSetter", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Firewall :</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("ConstraintSetter", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Not Required</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("ConstraintSetter", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Required</span></p></body></html>", None))
    # retranslateUi