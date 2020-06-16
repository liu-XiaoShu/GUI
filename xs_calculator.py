from PyQt5.QtWidgets import QApplication, QWidget
import sys

class Calculator(QWidget):
    def __init__(self):
        self.number_str = ""
        self.version = "小树计算器 V1.0"

        super().__init__()
        self.resize(400,400)

        from PyQt5.uic import loadUi  # 需要导入的模块
        #loadUi("record.ui", self)  #加载UI文件
        loadUi("calculator_gui.ui", self)  #加载UI文件

        #信号槽---- 按键触发
        self.Button_0.clicked.connect(lambda: self.accept_button_value(0))   
        self.Button_1.clicked.connect(lambda: self.accept_button_value(1))   
        self.Button_2.clicked.connect(lambda: self.accept_button_value(2))   
        self.Button_3.clicked.connect(lambda: self.accept_button_value(3))   
        self.Button_4.clicked.connect(lambda: self.accept_button_value(4))   
        self.Button_5.clicked.connect(lambda: self.accept_button_value(5))   
        self.Button_6.clicked.connect(lambda: self.accept_button_value(6))   
        self.Button_7.clicked.connect(lambda: self.accept_button_value(7))   
        self.Button_8.clicked.connect(lambda: self.accept_button_value(8))   
        self.Button_9.clicked.connect(lambda: self.accept_button_value(9))   
        
        #功能按键触发
        self.Button_addition.clicked.connect(lambda: self.accept_button_value("+"))
        self.Button_subtraction.clicked.connect(lambda: self.accept_button_value("-"))
        self.Button_multiplication.clicked.connect(lambda: self.accept_button_value("*"))
        self.Button_division.clicked.connect(lambda: self.accept_button_value("/"))

        self.Button_Backspace.clicked.connect(lambda: self.accept_button_value("Backspace"))
        self.Button_Clean.clicked.connect(lambda: self.accept_button_value("Clean"))   
        self.Button_Infor.clicked.connect(lambda: self.accept_button_value("Infor"))
        self.Button_L_par.clicked.connect(lambda: self.accept_button_value("("))
        self.Button_R_par.clicked.connect(lambda: self.accept_button_value(")"))

        self.Button_result.clicked.connect(lambda: self.calculation_results("计算结果"))

        

    def accept_button_value(self, number):
        if number == "Clean":
            self.number_str = ""
        elif number == "Backspace":
            self.number_str = list(self.number_str)
            if len(self.number_str) > 0:
                self.number_str.pop()
                self.number_str = "".join(self.number_str)
            else:
                self.number_str = ""
        elif number == "Infor":
            self.number_str = self.version
        else:
            line_edit_content = self.lineEdit.text()
            if line_edit_content.find(self.version) >= 0:
                self.number_str = ""
            self.number_str = str(self.number_str) + str(number)
        print(self.number_str)
        self.lineEdit.setText(str(self.number_str))

    def calculation_results(self, infor):
        line_edit_content = self.lineEdit.text()
        print(line_edit_content)
        result = 0.0
        if line_edit_content.find(self.version) >= 0:
            self.lineEdit.setText("输入错误")
        else:
            try:
                result = eval(line_edit_content)
            except:
                result = "计算错误，请检查输入"
            self.lineEdit.setText(str(result))
            

 

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=Calculator()
    w.show()
    sys.exit(app.exec_())
