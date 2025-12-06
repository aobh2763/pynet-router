from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QSpinBox, QWidget)

class UI_RouterSelector(object):
    def setupUi(self, router_selector):
        if not router_selector.objectName():
            router_selector.setObjectName(u"router_selector")
        router_selector.resize(640, 200)
        self.button_box = QDialogButtonBox(router_selector)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setGeometry(QRect(10, 160, 620, 32))
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.spin_box = QSpinBox(router_selector)
        self.spin_box.setObjectName(u"spin_box")
        self.spin_box.setGeometry(QRect(10, 109, 620, 41))
        self.spin_box.setAutoFillBackground(False)
        self.spin_box.setMinimum(0)
        self.spin_box.setMaximum(999999)
        self.spin_box.setValue(0)
        self.label = QLabel(router_selector)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 80, 621, 21))
        self.label_2 = QLabel(router_selector)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 621, 51))
        self.error_label = QLabel(router_selector)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(14, 166, 411, 21))

        self.retranslateUi(router_selector)
        self.button_box.accepted.connect(router_selector.accept)
        self.button_box.rejected.connect(router_selector.reject)

        QMetaObject.connectSlotsByName(router_selector)
    # setupUi

    def retranslateUi(self, router_selector):
        router_selector.setWindowTitle(QCoreApplication.translate("router_selector", u"Router Selector", None))
        self.label.setText(QCoreApplication.translate("router_selector", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Select the ID of the target router :</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("router_selector", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Router Selector</span></p></body></html>", None))
        self.error_label.setText("")
    # retranslateUi