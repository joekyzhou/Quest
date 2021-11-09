# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:31:32 2021

@author: joeky

Program to ask someone out
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtGui import *


parameters = {"question": ["Food interest?", "Location?", "Day of the week that you are free?"],
              "answer1": [],
              "answer2": [],
              "answer3": [],
              "answer4": [],
              "choice":[] 
             }


widgets= {"logo" : [],
          "button":[],
          "question":[],
          "answer1":[],
          "answer2":[],
          "answer3":[],
          "answer4":[],
          "result":[]
          }

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Quest")
window.setFixedWidth(700)
window.setFixedHeight(400)
window.setStyleSheet("background: #89CFF0;")

grid = QGridLayout()

def clear_widgets():
    for widget in widgets:
        if widgets[widget]!=[]:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def show_frame1(): 
    clear_widgets()
    frame1()
    
def start_game():
    clear_widgets()
    frame2()

def create_buttons(answer, l_margin, r_margin):
        button=QPushButton(answer)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setFixedWidth(300)
        button.setStyleSheet(
            "*{border: 4px solid '#BC006C';"+
            "margin-left: "+str(l_margin)+"px;"+
            "margin-right: "+str(r_margin)+"px;"+
            "color: white;"
            "font-family: 'shanti';"+
            "font-size:16px;"+
            "border-radius: 50px;"+
            "padding: 15px 0;"+
            "margin-top:20px"+
            "*:hover{background:'#Bc006C'}"
            )
        button.clicked.connect(frame3)
        return button
def create_buttons1(answer, l_margin, r_margin):
        button=QPushButton(answer)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setFixedWidth(300)
        button.setStyleSheet(
            "*{border: 4px solid '#BC006C';"+
            "margin-left: "+str(l_margin)+"px;"+
            "margin-right: "+str(r_margin)+"px;"+
            "color: white;"
            "font-family: 'shanti';"+
            "font-size:16px;"+
            "border-radius: 50px;"+
            "padding: 15px 0;"+
            "margin-top:20px"+
            "*:hover{background:'#Bc006C'}"
            )
        button.clicked.connect(frame4)
        return button
def create_buttons2(answer, l_margin, r_margin):
        button=QPushButton(answer)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setFixedWidth(300)
        button.setStyleSheet(
            "*{border: 4px solid '#BC006C';"+
            "margin-left: "+str(l_margin)+"px;"+
            "margin-right: "+str(r_margin)+"px;"+
            "color: white;"
            "font-family: 'shanti';"+
            "font-size:16px;"+
            "border-radius: 50px;"+
            "padding: 15px 0;"+
            "margin-top:20px"+
            "*:hover{background:'#Bc006C'}"
            )
        button.clicked.connect(frame5)
        return button
def create_buttons3(answer, l_margin, r_margin):
        button=QPushButton(answer)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setFixedWidth(300)
        button.setStyleSheet(
            "*{border: 4px solid '#BC006C';"+
            "margin-left: "+str(l_margin)+"px;"+
            "margin-right: "+str(r_margin)+"px;"+
            "color: white;"
            "font-family: 'shanti';"+
            "font-size:16px;"+
            "border-radius: 50px;"+
            "padding: 15px 0;"+
            "margin-top:20px"+
            "*:hover{background:'#Bc006C'}"
            )
        return button    
def frame1():
#display logo
    logo = QLabel()
    logo.setText("Jamie's Epic Quest")
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "font-size: 40px;"+
        "color: 'pink';"
        
        )
    widgets["logo"].append(logo)
    
    #button widget
    button = QPushButton("PLAY")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "border: 4px solid '#BC006C'"+
        "border-radius: 10px;"+
        "font-size: 35px;"+
        "color: 'white';"+
        "padding:25px 0;"+
        "margin: 100px 200px;"
                         )
    button.clicked.connect(start_game)
    widgets["button"].append(button)

    grid.addWidget(widgets["logo"][-1],0,0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)
    
    
def frame2():
    question = QLabel(parameters["question"][0])
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-family: Shanti;"+
        "font-size: 40px;"+
        "color: 'pink';"+
        "padding: 75px;"  
        )
    widgets["question"].append(question)
    
    button1=create_buttons("Chinese", 85, 5)
    button2=create_buttons("Italian", 5, 85)
    button3=create_buttons("Middle Eastern", 85, 5)
    button4=create_buttons("Japanese", 5, 85)
    
    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)
    
    logo = QLabel()
    logo.setText("Yes? No? Maybe?")
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "font-size: 20px;"+
        "color: 'pink';"
        )
    widgets["logo"].append(logo)
    
    
    grid.addWidget(widgets["question"][-1],1,0, 1, 2)
    grid.addWidget(widgets["answer1"][-1],2,0)
    grid.addWidget(widgets["answer2"][-1],2,1)
    grid.addWidget(widgets["answer3"][-1],3,0)
    grid.addWidget(widgets["answer4"][-1],3,1)
    grid.addWidget(widgets["logo"][-1],4, 0, 1, 2)


def frame3():
    question = QLabel(parameters["question"][1])
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-family: Shanti;"+
        "font-size: 40px;"+
        "color: 'pink';"+
        "padding: 75px;"  
        )
    widgets["question"].append(question)
    
    button1=create_buttons1("Bronx", 85, 5)
    button2=create_buttons1("Brooklyn", 5, 85)
    button3=create_buttons1("Manhattan", 85, 5)
    button4=create_buttons1("Queens", 5, 85)
    
    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)
    
    logo = QLabel()
    logo.setText("Yes? No? Maybe?")
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "font-size: 20px;"+
        "color: 'pink';"
        )
    widgets["logo"].append(logo)
    
    
    grid.addWidget(widgets["question"][-1],1,0, 1, 2)
    grid.addWidget(widgets["answer1"][-1],2,0)
    grid.addWidget(widgets["answer2"][-1],2,1)
    grid.addWidget(widgets["answer3"][-1],3,0)
    grid.addWidget(widgets["answer4"][-1],3,1)
    grid.addWidget(widgets["logo"][-1],4, 0, 1, 2)
    
def frame4():
    question = QLabel(parameters["question"][-1])
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-family: Shanti;"+
        "font-size: 40px;"+
        "color: 'pink';"+
        "padding: 75px;"  
        )
    widgets["question"].append(question)
    
    button1=create_buttons2("Thursday", 85, 5)
    button2=create_buttons2("Friday", 5, 85)
    button3=create_buttons2("Saturday", 85, 5)
    button4=create_buttons2("Sunday", 5, 85)
    
    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)
    
    logo = QLabel()
    logo.setText("Yes? No? Maybe?")
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "font-size: 20px;"+
        "color: 'pink';"
        )
    widgets["logo"].append(logo)
    
    
    grid.addWidget(widgets["question"][-1],1,0, 1, 2)
    grid.addWidget(widgets["answer1"][-1],2,0)
    grid.addWidget(widgets["answer2"][-1],2,1)
    grid.addWidget(widgets["answer3"][-1],3,0)
    grid.addWidget(widgets["answer4"][-1],3,1)
    grid.addWidget(widgets["logo"][-1],4, 0, 1, 2)

def frame5():
    
    result = QLabel("WOULD YOU LIKE TO GO WITH JOEKY?")
    result.setAlignment(QtCore.Qt.AlignCenter)
    result.setWordWrap(True)
    result.setStyleSheet(
        "font-family: shanti;"+
        "font-size: 30px;"+
        "color: 'green';"+
        "padding: 75px;"
        )
    widgets["result"].append(result)
    
    button1=create_buttons3("Yes", 85, 5)
    button2=create_buttons3("No", 5, 85)
    button3=create_buttons3("Defintely Yes", 85, 5)
    button4=create_buttons3("Definitely No", 5, 85)
    
    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)
    
    logo=QLabel()
    logo.setText("Success or Failure?")
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(
        "font-size: 20px;"+
        "color: 'pink';"
        )
    widgets["logo"].append(logo)
    
    grid.addWidget(widgets["result"][-1],1,0,1,2)
    grid.addWidget(widgets["answer1"][-1],2,0)
    grid.addWidget(widgets["answer2"][-1],2,1)
    grid.addWidget(widgets["answer3"][-1],3,0)
    grid.addWidget(widgets["answer4"][-1],3,1)
    grid.addWidget(widgets["logo"][-1],4, 0, 1, 2)
    
#Mediterranean
#Au Zaatar- East Village Manhattan
#Oasis Mediterranean Restaurant- Bronx
#Yemen Cafe & Restaurant - Brooklyn
#Blvd Prime Grill - Queens

#Italian
#Olio e Piu - Manhattan
#Gino's - Brooklyn
#Antonio's Trattoria - Bronx
#Tuscan Hills - Queens

#Japanese
# Sushi Lab Rooftop - Manhattan
# - Bronx
# - Brooklyn
# - Queens

#Korean
# - Manhattan
# - Bronx
# - Brooklyn
# - Queens

frame1()

    
window.setLayout(grid)


window.show()
sys.exit(app.exec())