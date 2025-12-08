from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QSizePolicy, QTableView, QWidget)

class UI_VariableViewer(object):
    def setupUi(self, VariableViewer):
        if not VariableViewer.objectName():
            VariableViewer.setObjectName(u"VariableViewer")
        VariableViewer.resize(640, 480)
        self.label = QLabel(VariableViewer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(14, 10, 611, 71))
        self.variable_table = QTableView(VariableViewer)
        self.variable_table.setObjectName(u"variable_table")
        self.variable_table.setGeometry(QRect(5, 151, 631, 321))
        self.label_2 = QLabel(VariableViewer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(14, 80, 611, 61))

        self.retranslateUi(VariableViewer)

        QMetaObject.connectSlotsByName(VariableViewer)
    # setupUi

    def retranslateUi(self, VariableViewer):
        VariableViewer.setWindowTitle(QCoreApplication.translate("VariableViewer", u"Variable Viewer", None))
        self.label.setText(QCoreApplication.translate("VariableViewer", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Variable Viewer</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("VariableViewer", u"<html><head/><body><p align=\"center\">This table displays the status of all possible links in the latest optimal path found by clicking &quot;Find Route&quot;</p><p align=\"center\">1 = Activated, 0 = Deactivated</p></body></html>", None))
    # retranslateUi

