from PySide6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QScrollArea, QHeaderView
from .ui import UI_VariableViewer

class VariableViewer(QDialog):
    def __init__(self, model):
        super().__init__()
        self.ui = UI_VariableViewer()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())  # fixed size dialog

        # Create table
        self.table = self.make_table(model)

        # Put table inside a scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)  # table can grow
        scroll.setWidget(self.table)

        # Add scroll area to the UI layout placeholder
        layout = QVBoxLayout(self.ui.variable_table)
        layout.addWidget(scroll)
        self.ui.variable_table.setLayout(layout)

    def make_table(self, model):
        # Collect router IDs from variable names
        router_ids = set()
        for var in model.getVars():
            name = var.VarName
            if name.startswith("l"):
                try:
                    a, b = name[1:].split("-")
                    router_ids.add(a)
                    router_ids.add(b)
                except ValueError:
                    continue
        router_ids = sorted(router_ids)
        n = len(router_ids)

        # Create table
        table = QTableWidget()
        table.setRowCount(n)
        table.setColumnCount(n)
        table.setHorizontalHeaderLabels(router_ids)
        table.setVerticalHeaderLabels(router_ids)

        # Fill table values
        for i, row_id in enumerate(router_ids):
            for j, col_id in enumerate(router_ids):
                if row_id == col_id:
                    value = 0
                else:
                    var_name = f"l{row_id}-{col_id}"
                    var = model.getVarByName(var_name)
                    value = int(var.X) if var is not None else 0
                table.setItem(i, j, QTableWidgetItem(str(value)))

        # Stretch all columns
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setDefaultSectionSize(30)
        table.setAlternatingRowColors(True)

        # Select whole row when header is clicked
        table.setSortingEnabled(False)                  # disable sorting
        table.setSelectionBehavior(QTableWidget.SelectRows)
        table.setSelectionMode(QTableWidget.SingleSelection)  # optional: select one row at a time
        
        # Dark theme styling
        table.setStyleSheet("""
            QTableWidget {
                background-color: #1e1e1e;
                color: #f0f0f0;
                gridline-color: #444;
                font: 12pt "Segoe UI";
            }
            QHeaderView::section {
                background-color: #2d2d2d;
                color: #f0f0f0;
                padding: 4px;
                border: 1px solid #555;
                font-weight: bold;
            }
            QTableWidget::item:selected {
                background-color: #3d7848;
                color: #ffffff;
            }
        """)

        return table