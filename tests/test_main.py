from boomer.main import (APP,
                         __version__,
                         __appname__,
                         dialog)
from boomer.gui.dialogs import FinancialStatementDateEntryDialog


def test_APP_default_values():

    assert APP.organizationDomain() == 'geronacapital'
    assert APP.organizationName() == 'Gerona Capital'
    assert APP.applicationName() == __appname__
    assert APP.applicationDisplayName() == f'{__appname__} {__version__}'
    assert APP.applicationVersion() == __version__


def test_dialog_if_instance_of_FinancialStatementDateEntryDialog():

    assert isinstance(dialog, FinancialStatementDateEntryDialog) == True
