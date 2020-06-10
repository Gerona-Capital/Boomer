import sys
from PyQt5.QtTest import QTest
from boomer.gui.dialogs import FinancialStatementDateEntryDialog
from boomer.main import APP


def test_FinancialStatementDataEntryDialog_default_properties():

    dialog = FinancialStatementDateEntryDialog()

    assert dialog.windowTitle() == 'Financial Statement Data Entry Template'
