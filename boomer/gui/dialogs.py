from PyQt5.QtWidgets import QDialog


class FinancialStatementDateEntryDialog(QDialog):

    def __init__(self):

        super().__init__()
        self._properties()

    def _properties(self):

        self.setWindowTitle('Financial Statement Data Entry Template')
