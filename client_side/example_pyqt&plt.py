# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:23:33 2021

@author: Fanyi Sun
"""
import sys
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(1000, 500)

        # 解决无法显示中文
        plt.rcParams['font.sans-serif'] = ['SimHei']
        # 解决无法显示负号
        plt.rcParams['axes.unicode_minus'] = False
        # 按钮
        self.one_btn = QPushButton('画一条线')
        self.more_btn = QPushButton('重复画线')
        self.reset_btn = QPushButton('重置')
        # 按钮绑定方法
        self.one_btn.clicked.connect(self.draw_cmd)
        self.more_btn.clicked.connect(self.draw_cmd)
        self.reset_btn.clicked.connect(self.reset_cmd)
        # 设置画布部分
        self.fig = plt.figure(figsize=(10, 4), dpi=80)
        self.canvas = FC(self.fig)
        # 添加第一个图
        self.ax = self.fig.add_subplot('121')
        self.ax.set_title('画一条线')
        # 添加第二个图
        self.ax1 = self.fig.add_subplot('122')
        self.ax1.set_title('重复画线')
        # 设置布局，将组件添加到布局中
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.one_btn)
        self.layout.addWidget(self.more_btn)
        self.layout.addWidget(self.reset_btn)

        self.setLayout(self.layout)

    def draw_cmd(self):
        try:
            # 如果是点击画一条线的按钮，就先清除内容
            if self.sender() == self.one_btn:
                ax = self.ax
                ax.cla()
                self.ax.set_title('画一条线')
            # 如果是点击重复画图的按钮，就不清除原先的内容
            elif self.sender() == self.more_btn:
                ax = self.ax1
            # 绘图部分
            x = [i + 1 for i in range(5)]  # x轴
            y = np.random.randint(0, 10, 5)  # y轴
            ax.plot(x, y)  # 折线图
            self.canvas.draw()  # 绘制
        except Exception as e:
            print(e)

    def reset_cmd(self):
        try:
            # 清除内容
            self.ax.cla()
            self.ax1.cla()
            # 重新设置标题
            self.ax.set_title('画一条线')
            self.ax1.set_title('重复画线')
            # 重新绘制
            self.canvas.draw()
        except Exception as e:
            print(e)


def start():
    app = QApplication(sys.argv)
    m = MyWidget()
    m.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start()