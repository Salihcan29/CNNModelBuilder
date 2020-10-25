# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 21:06:25 2020

@author: Salihcan
"""

from mainui import Main_ui
from PyQt5.QtWidgets import QApplication

import sys

def main():
    app = QApplication(sys.argv)
    w = Main_ui()
    w.setupUi()
    w.retranslateUi()
    w.show()
    app.exec_()

if __name__ == "__main__":
    main()

