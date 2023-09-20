# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 13:50:02 2021

@author: Fanyi Sun
"""

import sys

from PyQt5.QtWidgets import QApplication

from client_side.myMainWindow import QmyMainWindow


app = QApplication(sys.argv)
form = QmyMainWindow()
form.show()

sys.exit(app.exec_())
