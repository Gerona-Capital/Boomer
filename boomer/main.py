import sys
from PyQt5.QtWidgets import QApplication
from boomer.gui.dialogs import FinancialStatementDateEntryDialog

__version__ = '0.1'
__appname__ = 'Boomer'

APP = QApplication(sys.argv)
APP.setOrganizationName('Gerona Capital')
APP.setOrganizationDomain('geronacapital')
APP.setApplicationName(__appname__)
APP.setApplicationDisplayName(f'{__appname__} {__version__}')
APP.setApplicationVersion(__version__)

dialog = FinancialStatementDateEntryDialog()

if __name__ == '__main__':
    dialog.show()
    APP.exec()
