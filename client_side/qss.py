# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 14:34:00 2021

@author: Fanyi Sun
"""

class QSS():
    def __init__(self):
        self.tab = '''
/**********TabWidget**********/
QTabBar::tab {
        color: white;
        background: rgb(50, 180, 251);
        border: none;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
        height: 28px;
        min-width: 20px;
        margin-right: 5px;
        padding-left: 5px;
        padding-right: 5px;
}
QTabBar::tab:hover {
        color: white;
        background: rgb(0, 100, 211);
}
QTabBar::tab:selected {
        color: white;
        height: 33px;
        background: rgb(0, 100, 211);
}
QTabBar::tab:pressed {
        color: white;
        font-size: 21px;
        background: rgb(0, 120, 225);
}
QTabBar#tabWidget::tab {
        border: 1px solid rgb(121, 157, 203);
        border-bottom: none;
        color: rgb(0, 0, 0);
        background: transparent;
}
'''
        self.menubar = '''
/**********MenuBar**********/
QMenuBar {
        font-size: 20px;
        font-family: Microsoft Yahei UI;
        border: 1px solid rgb(101, 146, 203);
        border-left: none;
        border-right: none;
}
QMenuBar::item {
        border: 0px solid transparent;
        padding: 5px 10px 5px 10px;
        background: transparent;
}
QMenuBar::item:enabled {
        color: rgb(3, 68, 127);
}
QMenuBar::item:!enabled {
        color: rgb(155, 155, 155);
}
QMenuBar::item:enabled:selected {
        border-top-color: rgb(111, 156, 207);
        border-bottom-color: rgb(111, 156, 207);
        background: rgb(198, 224, 252);
}
QMenuBar::item:enabled:pressed {
        border: 1px solid;
        border-color: rgb(55, 55, 198);
        color: rgb(0, 0, 0);
        background: rgb(200, 230, 255);
}
'''

        self.toolbar = '''
/**********ToolBar**********/
QToolButton:!checked{
        font-size: 46px;
        background: transparent;
}
QToolButton:checked{
        color: rgb(139, 69, 19);
        font-size: 46px;
        border: none;
        background: transparent;
}
QToolButton:hover{
        font-size: 46px;
        border: none;
        background: transparent;
}
QToolBar{
        background: white;
}
'''

        self.btnStart = '''
/**********ToolButton in formWelcome**********/
QToolButton{
	color: white;
	background-color: rgb(60,179,113);
	border: 8px;
	border-color: rgb(50,169,93);
	border-radius: 35px;
	padding: 4px 4px;
	border-style: solid;
}

QToolButton:hover{
	color: white;
	font-size: 17.5pt;
	padding: 3px 4px;
	border-color: rgb(50,179,93);
	background-color: rgb(60,189,113);
}

QToolButton:pressed{
	color: white;
	font-size: 17pt;
	padding: 3px 4px;
	border-color: rgb(50,179,93);
	background-color: rgb(60,199,113);
}
'''
    
        self.target_listWidget = '''
/**********Left ListWidget in formSetTarget**********/
QListWidget, QListView, QTreeWidget, QTreeView {
    outline: 0px;
    border: 2px solid rgb(0,0,0);
    border-left: none;
    border-top: none;
    border-bottom: none;
}

QListWidget {
    font-family: Microsoft Yahei UI;
    font-size: 12.5pt;
    min-width: 120px;
    max-width: 520px;
    color: Black;
    background: rgb(245, 245, 245);
}

QListWidget::Item:selected {
    color: Black;
    background: lightGray;
    border-left: 8px solid red;
}
'''

        self.target_item = '''
/**********LineEdit in formTargetItem**********/
QLineEdit{
	border: 2px groove gray;
	border-radius: 14px;
	padding: 2px 4px;
	color: rgb(0, 0, 0);
	border-color: rgb(0, 100, 0);
}
/**********PushButton in formTargetItem**********/
QPushButton{
	color: black;
	background-color: rgb(250, 250, 250);
	border: 1.5px;
	border-color: rgb(100, 100, 100);
	border-radius: 15px;
	padding: 4px 4px;
	border-style: solid;
}

QPushButton:hover{
	color: Black;
	font-size: 10pt;
	padding: 3px 4px;
	border-color: rgb(150, 150, 150);
	background-color: rgb(225, 255, 255);
}

QPushButton:pressed{
	color: Black;
	font-size: 10.5pt;
	padding: 3px 4px;
	border-color: rgb(100, 100, 100);
	background-color: rgb(195, 255, 255);
}

'''
     # border: 1px solid rgb(111, 156, 207);
     # background: rgb(232, 241, 250);

# =============================================================================
# QMenu {
#         font-size:13px;
#         font-family:Microsoft YaHei;
#         border: 1px solid rgb(111, 156, 207);
#         background: rgb(232, 241, 250);
# }
# QMenu::item {
#         font-family:Microsoft YaHei;
#         height: 18px;
#         padding: 5px 25px 5px 20px;
#         padding-left: 30px;
#         padding-right: 12px;
# }
# QMenu::item:enabled {
#         color: rgb(84, 84, 84);
# }
# QMenu::item:!enabled {
#         color: rgb(155, 155, 155);
# }
# QMenu::item:enabled:selected {
#         color: rgb(2, 65, 132);
#         background: rgba(255, 255, 255, 200);
# }
# QMenu::separator {
#         height: 1px;
#         background: rgb(111, 156, 207);
# }
# QMenu::indicator {
#         width: 13px;
#         height: 13px;
# }
# QMenu::icon {
#         padding-left: 12px;
#         padding-right: 0px;
# }
# =============================================================================
