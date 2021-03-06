# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 21:06:25 2020

@author: Salihcan
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

from random import randint

class builder(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it 
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.resize(300,100)
        self.setLayout(layout)