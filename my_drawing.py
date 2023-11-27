"""
File: my_drawing.py
Name: Tony
----------------------
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLine, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved

# Below are constants
WINDOW_X = 50
WINDOW_Y = 50
CONAN_F_X = 45
CONAN_F_Y = 370
NOBI_F_X = 200
NOBI_F_Y = 250
BAN_X = 560
BAN_Y = 50
JERRY_X = 388
JERRY_Y = 135

# Global var
window = GWindow(1000, 700)
n = 1
a = 0
b = 0
position_label = GLabel("x: " + "y: ")
position_label.font = "-10"


def main():
    """
    Title: stanCode創辦人Jerry與兩位日本小學生柯南、大雄的合照

    stanCode 獲得全世界程式教育機構的評選第一名，
    因此受邀到日本參加全世界程式教育機構展覽會，剛好碰到當地小學生江戶川柯南、野比大雄來參觀，
    兩人發現stanCode使用Karel來入門學習Python非常新奇，因此兩人聽完Jerry的介紹後，
    除了認同stanCode的教育理念，也決定要介紹給各自的朋友，邀請他們一起來stanCode學習。
    更重要的是他們在離開前決定要跟stanCode的創辦人Jerry來一張合照，留做紀念。
    """
    global window

    floor = GRect(1000, 35, x=0, y=665)
    floor.filled = "True"
    floor.fill_color = "rosybrown"

    window.add(floor)
    back = GRect(1000, 665, x=0, y=0)
    back.filled = "True"
    back.fill_color = "palegoldenrod"
    window.add(back)
    window1 = GRect(200, 150, x=WINDOW_X, y=WINDOW_Y)
    window1.filled = True
    window1.fill_color = "brown"
    window.add(window1)
    window2 = GRect(85, 60, x=WINDOW_X+10, y=WINDOW_Y+10)
    window2.filled = True
    window2.fill_color = "lightskyblue"
    window.add(window2)
    window3 = GRect(85, 60, x=WINDOW_X+105, y=WINDOW_Y+10)
    window3.filled = True
    window3.fill_color = "lightskyblue"
    window.add(window3)
    window4 = GRect(85, 60, x=WINDOW_X+10, y=WINDOW_Y+80)
    window4.filled = True
    window4.fill_color = "lightskyblue"
    window.add(window4)
    window5 = GRect(85, 60, x=WINDOW_X+105, y=WINDOW_Y+80)
    window5.filled = True
    window5.fill_color = "lightskyblue"
    window.add(window5)

    jerry_cloth = GPolygon()
    jerry_cloth.add_vertex((JERRY_X + 13, JERRY_Y + 95))
    jerry_cloth.add_vertex((JERRY_X + 68, JERRY_Y + 95))
    jerry_cloth.add_vertex((JERRY_X + 115, JERRY_Y + 120))
    jerry_cloth.add_vertex((JERRY_X + 140, JERRY_Y + 180))
    jerry_cloth.add_vertex((JERRY_X + 105, JERRY_Y + 185))
    jerry_cloth.add_vertex((JERRY_X + 93, JERRY_Y + 160))
    jerry_cloth.add_vertex((JERRY_X + 93, JERRY_Y + 290))
    jerry_cloth.add_vertex((JERRY_X - 11, JERRY_Y + 290))
    jerry_cloth.add_vertex((JERRY_X - 11, JERRY_Y + 160))
    jerry_cloth.add_vertex((JERRY_X - 38, JERRY_Y + 160))
    jerry_cloth.add_vertex((JERRY_X - 38, JERRY_Y + 125))
    jerry_cloth.add_vertex((JERRY_X - 34, JERRY_Y + 120))
    jerry_cloth.filled = True
    jerry_cloth.fill_color = "red"
    window.add(jerry_cloth)
    jerry_hand = GPolygon()
    jerry_hand.add_vertex((JERRY_X + 133, JERRY_Y + 181))
    jerry_hand.add_vertex((JERRY_X + 112, JERRY_Y + 184))
    jerry_hand.add_vertex((JERRY_X + 112, JERRY_Y + 300))
    jerry_hand.add_vertex((JERRY_X + 108, JERRY_Y + 316))
    jerry_hand.add_vertex((JERRY_X + 114, JERRY_Y + 316))
    jerry_hand.add_vertex((JERRY_X + 114, JERRY_Y + 321))
    jerry_hand.add_vertex((JERRY_X + 120, JERRY_Y + 321))
    jerry_hand.add_vertex((JERRY_X + 120, JERRY_Y + 323))
    jerry_hand.add_vertex((JERRY_X + 125, JERRY_Y + 323))
    jerry_hand.add_vertex((JERRY_X + 125, JERRY_Y + 321))
    jerry_hand.add_vertex((JERRY_X + 131, JERRY_Y + 321))
    jerry_hand.add_vertex((JERRY_X + 131, JERRY_Y + 316))
    jerry_hand.add_vertex((JERRY_X + 137, JERRY_Y + 316))
    jerry_hand.add_vertex((JERRY_X + 134, JERRY_Y + 300))
    jerry_hand.filled = True
    jerry_hand.fill_color = "antiquewhite"
    window.add(jerry_hand)
    jerry_hand1 = GPolygon()
    jerry_hand1.add_vertex((JERRY_X - 38, JERRY_Y + 132))
    jerry_hand1.add_vertex((JERRY_X - 38, JERRY_Y + 153))
    jerry_hand1.add_vertex((JERRY_X - 75, JERRY_Y + 153))
    jerry_hand1.add_vertex((JERRY_X - 77, JERRY_Y + 150))
    jerry_hand1.add_vertex((JERRY_X - 68, JERRY_Y + 75))
    jerry_hand1.add_vertex((JERRY_X - 70, JERRY_Y + 35))
    jerry_hand1.add_vertex((JERRY_X - 40, JERRY_Y + 30))
    jerry_hand1.add_vertex((JERRY_X - 38, JERRY_Y + 36))
    jerry_hand1.add_vertex((JERRY_X - 60, JERRY_Y + 40))
    jerry_hand1.add_vertex((JERRY_X - 55, JERRY_Y + 55))
    jerry_hand1.add_vertex((JERRY_X - 40, JERRY_Y + 55))
    jerry_hand1.add_vertex((JERRY_X - 40, JERRY_Y + 60))
    jerry_hand1.add_vertex((JERRY_X - 52, JERRY_Y + 63))
    jerry_hand1.add_vertex((JERRY_X - 54, JERRY_Y + 75))
    jerry_hand1.add_vertex((JERRY_X - 54, JERRY_Y + 135))
    jerry_hand1.filled = True
    jerry_hand1.fill_color = "antiquewhite"
    window.add(jerry_hand1)
    jerry_neck = GPolygon()
    jerry_neck.add_vertex((JERRY_X+23, JERRY_Y + 60))
    jerry_neck.add_vertex((JERRY_X + 58, JERRY_Y + 60))
    jerry_neck.add_vertex((JERRY_X + 58, JERRY_Y + 105))
    jerry_neck.add_vertex((JERRY_X + 54, JERRY_Y + 109))
    jerry_neck.add_vertex((JERRY_X + 50, JERRY_Y + 112))
    jerry_neck.add_vertex((JERRY_X + 46, JERRY_Y + 114))
    jerry_neck.add_vertex((JERRY_X + 42, JERRY_Y + 115))
    jerry_neck.add_vertex((JERRY_X + 39, JERRY_Y + 115))
    jerry_neck.add_vertex((JERRY_X + 35, JERRY_Y + 114))
    jerry_neck.add_vertex((JERRY_X + 31, JERRY_Y + 112))
    jerry_neck.add_vertex((JERRY_X + 27, JERRY_Y + 109))
    jerry_neck.add_vertex((JERRY_X + 23, JERRY_Y + 105))
    jerry_neck.filled = True
    jerry_neck.fill_color = "antiquewhite"
    window.add(jerry_neck)
    jerry_watch1 = GRect(21, 5, x=JERRY_X + 112, y=JERRY_Y + 275)
    jerry_watch1.filled = True
    jerry_watch1.fill_color = "black"
    window.add(jerry_watch1)
    jerry_watch2 = GOval(15, 15, x=JERRY_X + 115, y=JERRY_Y + 270)
    jerry_watch2.filled = True
    jerry_watch2.color = "dimgrey"
    jerry_watch2.fill_color = "black"
    window.add(jerry_watch2)
    jerry_hair = GPolygon()
    jerry_hair.add_vertex((JERRY_X+3, JERRY_Y + 40))
    jerry_hair.add_vertex((JERRY_X+3, JERRY_Y-10))
    jerry_hair.add_vertex((JERRY_X+5, JERRY_Y - 17))
    jerry_hair.add_vertex((JERRY_X + 7, JERRY_Y - 20))
    jerry_hair.add_vertex((JERRY_X + 10, JERRY_Y - 24))
    jerry_hair.add_vertex((JERRY_X + 20, JERRY_Y - 26))
    jerry_hair.add_vertex((JERRY_X + 30, JERRY_Y - 29))
    jerry_hair.add_vertex((JERRY_X + 40, JERRY_Y - 31))
    jerry_hair.add_vertex((JERRY_X + 50, JERRY_Y - 32))
    jerry_hair.add_vertex((JERRY_X + 60, JERRY_Y - 30))
    jerry_hair.add_vertex((JERRY_X + 70, JERRY_Y - 27))
    jerry_hair.add_vertex((JERRY_X + 81, JERRY_Y - 20))
    jerry_hair.add_vertex((JERRY_X + 81, JERRY_Y + 40))
    jerry_hair.filled = True
    jerry_hair.fill_color = "black"
    window.add(jerry_hair)
    jerry_ear = GPolygon()
    jerry_ear.add_vertex((JERRY_X+5, JERRY_Y+49))
    jerry_ear.add_vertex((JERRY_X+5, JERRY_Y+25))
    jerry_ear.add_vertex((JERRY_X - 2, JERRY_Y + 20))
    jerry_ear.add_vertex((JERRY_X - 7, JERRY_Y + 22))
    jerry_ear.add_vertex((JERRY_X - 4, JERRY_Y + 54))
    jerry_ear.add_vertex((JERRY_X - 1, JERRY_Y + 55))
    jerry_ear.add_vertex((JERRY_X + 3, JERRY_Y + 54))
    jerry_ear.filled = True
    jerry_ear.fill_color = "antiquewhite"
    window.add(jerry_ear)
    jerry_ear1 = GPolygon()
    jerry_ear1.add_vertex((JERRY_X+76, JERRY_Y+49))
    jerry_ear1.add_vertex((JERRY_X+76, JERRY_Y+25))
    jerry_ear1.add_vertex((JERRY_X + 83, JERRY_Y + 20))
    jerry_ear1.add_vertex((JERRY_X + 88, JERRY_Y + 22))
    jerry_ear1.add_vertex((JERRY_X + 85, JERRY_Y + 54))
    jerry_ear1.add_vertex((JERRY_X + 82, JERRY_Y + 55))
    jerry_ear1.add_vertex((JERRY_X + 78, JERRY_Y + 54))
    jerry_ear1.filled = True
    jerry_ear1.fill_color = "antiquewhite"
    window.add(jerry_ear1)
    jerry_face = GPolygon()
    jerry_face.add_vertex((JERRY_X+10, JERRY_Y-5))
    jerry_face.add_vertex((JERRY_X + 5, JERRY_Y + 25))
    jerry_face.add_vertex((JERRY_X+5, JERRY_Y+65))
    jerry_face.add_vertex((JERRY_X+27, JERRY_Y + 85))
    jerry_face.add_vertex((JERRY_X + 54, JERRY_Y + 85))
    jerry_face.add_vertex((JERRY_X + 76, JERRY_Y + 65))
    jerry_face.add_vertex((JERRY_X + 76, JERRY_Y + 25))
    jerry_face.add_vertex((JERRY_X + 71, JERRY_Y-10))
    jerry_face.add_vertex((JERRY_X + 66, JERRY_Y-12))
    jerry_face.add_vertex((JERRY_X + 46, JERRY_Y-16))
    jerry_face.add_vertex((JERRY_X + 25, JERRY_Y - 16))
    jerry_face.add_vertex((JERRY_X + 15, JERRY_Y - 14))
    jerry_face.filled = True
    jerry_face.fill_color = "antiquewhite"
    window.add(jerry_face)
    jerry_glass1 = GLine(JERRY_X+5, JERRY_Y+25+5, JERRY_X+10, JERRY_Y+25+5)
    jerry_glass1.color = "dimgrey"
    window.add(jerry_glass1)
    jerry_glass2 = GLine(JERRY_X+71, JERRY_Y+25+5, JERRY_X+76, JERRY_Y+25+5)
    jerry_glass2.color = "dimgrey"
    window.add(jerry_glass2)
    jerry_glass3 = GLine(JERRY_X + 35, JERRY_Y + 25+5, JERRY_X + 46, JERRY_Y + 25+5)
    jerry_glass3.color = "dimgrey"
    window.add(jerry_glass3)
    jerry_glass4 = GPolygon()
    jerry_glass4.add_vertex((JERRY_X + 11, JERRY_Y + 20 + 5))
    jerry_glass4.add_vertex((JERRY_X + 10, JERRY_Y + 25+5))
    jerry_glass4.add_vertex((JERRY_X + 12, JERRY_Y + 36+5))
    jerry_glass4.add_vertex((JERRY_X + 20, JERRY_Y + 38+5))
    jerry_glass4.add_vertex((JERRY_X + 25, JERRY_Y + 38+5))
    jerry_glass4.add_vertex((JERRY_X + 33, JERRY_Y + 36+5))
    jerry_glass4.add_vertex((JERRY_X + 35, JERRY_Y + 25+5))
    jerry_glass4.add_vertex((JERRY_X + 34, JERRY_Y + 20+5))
    jerry_glass4.add_vertex((JERRY_X + 22, JERRY_Y + 18+5))
    jerry_glass4.color = "dimgrey"
    window.add(jerry_glass4)
    jerry_glass5 = GPolygon()
    jerry_glass5.add_vertex((JERRY_X + 47, JERRY_Y + 20 + 5))
    jerry_glass5.add_vertex((JERRY_X + 46, JERRY_Y + 25+5))
    jerry_glass5.add_vertex((JERRY_X + 48, JERRY_Y + 36+5))
    jerry_glass5.add_vertex((JERRY_X + 56, JERRY_Y + 38+5))
    jerry_glass5.add_vertex((JERRY_X + 61, JERRY_Y + 38+5))
    jerry_glass5.add_vertex((JERRY_X + 69, JERRY_Y + 36+5))
    jerry_glass5.add_vertex((JERRY_X + 71, JERRY_Y + 25+5))
    jerry_glass5.add_vertex((JERRY_X + 70, JERRY_Y + 20+5))
    jerry_glass5.add_vertex((JERRY_X + 58, JERRY_Y + 18+5))
    jerry_glass5.color = "dimgrey"
    window.add(jerry_glass5)
    jerry_eb1 = GPolygon()
    jerry_eb1.add_vertex((JERRY_X + 11, JERRY_Y + 21))
    jerry_eb1.add_vertex((JERRY_X + 11, JERRY_Y + 20))
    jerry_eb1.add_vertex((JERRY_X + 18, JERRY_Y + 18))
    jerry_eb1.add_vertex((JERRY_X + 21, JERRY_Y + 17))
    jerry_eb1.add_vertex((JERRY_X + 35, JERRY_Y + 22))
    jerry_eb1.add_vertex((JERRY_X + 35, JERRY_Y + 23))
    jerry_eb1.add_vertex((JERRY_X + 18, JERRY_Y + 21))
    jerry_eb1.filled = True
    jerry_eb1.fill_color = "black"
    window.add(jerry_eb1)
    jerry_eb2 = GPolygon()
    jerry_eb2.add_vertex((JERRY_X + 70, JERRY_Y + 21))
    jerry_eb2.add_vertex((JERRY_X + 70, JERRY_Y + 20))
    jerry_eb2.add_vertex((JERRY_X + 63, JERRY_Y + 18))
    jerry_eb2.add_vertex((JERRY_X + 60, JERRY_Y + 17))
    jerry_eb2.add_vertex((JERRY_X + 46, JERRY_Y + 22))
    jerry_eb2.add_vertex((JERRY_X + 46, JERRY_Y + 23))
    jerry_eb2.add_vertex((JERRY_X + 63, JERRY_Y + 21))
    jerry_eb2.filled = True
    jerry_eb2.fill_color = "black"
    window.add(jerry_eb2)
    jerry_nose = GPolygon()
    jerry_nose.add_vertex((JERRY_X + 38, JERRY_Y + 35+5))
    jerry_nose.add_vertex((JERRY_X + 36, JERRY_Y + 42+5))
    jerry_nose.add_vertex((JERRY_X + 32, JERRY_Y + 47+5))
    jerry_nose.add_vertex((JERRY_X + 32, JERRY_Y + 52+5))
    jerry_nose.add_vertex((JERRY_X + 40, JERRY_Y + 54+5))
    jerry_nose.add_vertex((JERRY_X + 48, JERRY_Y + 52+5))
    jerry_nose.add_vertex((JERRY_X + 48, JERRY_Y + 47+5))
    jerry_nose.add_vertex((JERRY_X + 44, JERRY_Y + 42+5))
    jerry_nose.add_vertex((JERRY_X + 42, JERRY_Y + 35+5))
    window.add(jerry_nose)
    jerry_mouth = GPolygon()
    jerry_mouth.add_vertex((JERRY_X + 25, JERRY_Y + 67))
    jerry_mouth.add_vertex((JERRY_X + 30, JERRY_Y + 67))
    jerry_mouth.add_vertex((JERRY_X + 35, JERRY_Y + 67))
    jerry_mouth.add_vertex((JERRY_X + 45, JERRY_Y + 67))
    jerry_mouth.add_vertex((JERRY_X + 50, JERRY_Y + 67))
    jerry_mouth.add_vertex((JERRY_X + 55, JERRY_Y + 67))
    jerry_mouth.add_vertex((JERRY_X + 54, JERRY_Y + 70))
    jerry_mouth.add_vertex((JERRY_X + 50, JERRY_Y + 73))
    jerry_mouth.add_vertex((JERRY_X + 45, JERRY_Y + 74))
    jerry_mouth.add_vertex((JERRY_X + 40, JERRY_Y + 75))
    jerry_mouth.add_vertex((JERRY_X + 35, JERRY_Y + 74))
    jerry_mouth.add_vertex((JERRY_X + 30, JERRY_Y + 73))
    jerry_mouth.add_vertex((JERRY_X + 26, JERRY_Y + 70))
    jerry_mouth.filled = True
    jerry_mouth.fill_color = "Red"
    window.add(jerry_mouth)
    jerry_eye1 = GOval(18, 9, x=JERRY_X+13, y=JERRY_Y+28)
    jerry_eye1.filled = True
    jerry_eye1.fill_color = "white"
    window.add(jerry_eye1)
    jerry_eye1 = GOval(18, 9, x=JERRY_X+50, y=JERRY_Y+28)
    jerry_eye1.filled = True
    jerry_eye1.fill_color = "white"
    window.add(jerry_eye1)
    jerry_eye1 = GOval(7, 7, x=JERRY_X+19, y=JERRY_Y+29)
    jerry_eye1.filled = True
    jerry_eye1.fill_color = "black"
    window.add(jerry_eye1)
    jerry_eye1 = GOval(7, 7, x=JERRY_X+56, y=JERRY_Y+29)
    jerry_eye1.filled = True
    jerry_eye1.fill_color = "black"
    window.add(jerry_eye1)
    jerry_pant = GPolygon()
    jerry_pant.add_vertex((JERRY_X - 8, JERRY_Y + 290))
    jerry_pant.add_vertex((JERRY_X + 90, JERRY_Y + 290))
    jerry_pant.add_vertex((JERRY_X + 95, JERRY_Y + 515))
    jerry_pant.add_vertex((JERRY_X + 51, JERRY_Y + 515))
    jerry_pant.add_vertex((JERRY_X + 41, JERRY_Y + 330))
    jerry_pant.add_vertex((JERRY_X + 31, JERRY_Y + 515))
    jerry_pant.add_vertex((JERRY_X - 13, JERRY_Y + 515))
    jerry_pant.filled = True
    jerry_pant.fill_color = "black"
    window.add(jerry_pant)
    jerry_shoe1 = GPolygon()
    jerry_shoe1.add_vertex((JERRY_X + 56, JERRY_Y + 515))
    jerry_shoe1.add_vertex((JERRY_X + 80, JERRY_Y + 515))
    jerry_shoe1.add_vertex((JERRY_X + 100, JERRY_Y + 525))
    jerry_shoe1.add_vertex((JERRY_X + 105, JERRY_Y + 535))
    jerry_shoe1.add_vertex((JERRY_X + 56, JERRY_Y + 535))
    jerry_shoe1.filled = True
    jerry_shoe1.fill_color = "white"
    window.add(jerry_shoe1)
    jerry_shoe2 = GPolygon()
    jerry_shoe2.add_vertex((JERRY_X + 26, JERRY_Y + 515))
    jerry_shoe2.add_vertex((JERRY_X + 2, JERRY_Y + 515))
    jerry_shoe2.add_vertex((JERRY_X - 18, JERRY_Y + 525))
    jerry_shoe2.add_vertex((JERRY_X - 23, JERRY_Y + 535))
    jerry_shoe2.add_vertex((JERRY_X + 26, JERRY_Y + 535))
    jerry_shoe2.filled = True
    jerry_shoe2.fill_color = "white"
    window.add(jerry_shoe2)
    jerry_label1 = GLabel("stanCode", x=JERRY_X - 10, y=JERRY_Y + 160)
    jerry_label1.font = "Times New Roman-20"
    jerry_label1.color = "white"
    window.add(jerry_label1)
    jerry_label2 = GLabel("turn_left()", x=JERRY_X - 7, y=JERRY_Y + 165)
    jerry_label2.font = "Times New Roman-4"
    jerry_label2.color = "white"
    window.add(jerry_label2)
    jerry_label3 = GLabel("move()", x=JERRY_X - 7, y=JERRY_Y + 170)
    jerry_label3.font = "Times New Roman-4"
    jerry_label3.color = "white"
    window.add(jerry_label3)
    jerry_label4 = GLabel("pick_beeper", x=JERRY_X - 7, y=JERRY_Y + 175)
    jerry_label4.font = "Times New Roman-4"
    jerry_label4.color = "white"
    window.add(jerry_label4)
    jerry_label5 = GLabel("put_beeper", x=JERRY_X - 7, y=JERRY_Y + 180)
    jerry_label5.font = "Times New Roman-4"
    jerry_label5.color = "white"
    window.add(jerry_label5)
    jerry_label6 = GLabel("taiwan(stanCode)", x=JERRY_X - 7, y=JERRY_Y + 185)
    jerry_label6.font = "Times New Roman-4"
    jerry_label6.color = "white"
    window.add(jerry_label6)

    back_show = GRect(450, 640, x=BAN_X-20, y=BAN_Y-20)
    back_show.filled = True
    back_show.fill_color = "lightgreen"
    window.add(back_show)
    ban_b = GRect(350, 80, x=BAN_X, y=BAN_Y)
    ban_b.filled = True
    ban_b.fill_color = "Red"
    window.add(ban_b)
    ban_label = GLabel("stanCode", x=BAN_X+40, y=BAN_Y+80)
    ban_label.font = "Times New Roman-55"
    ban_label.color = "white"
    window.add(ban_label)
    ban_crowd = GPolygon()
    ban_crowd.add_vertex((BAN_X+365, BAN_Y+70))
    ban_crowd.add_vertex((BAN_X + 415, BAN_Y + 70))
    ban_crowd.add_vertex((BAN_X + 420, BAN_Y + 10))
    ban_crowd.add_vertex((BAN_X + 405, BAN_Y + 35))
    ban_crowd.add_vertex((BAN_X + 390, BAN_Y + 10))
    ban_crowd.add_vertex((BAN_X + 375, BAN_Y + 35))
    ban_crowd.add_vertex((BAN_X + 360, BAN_Y + 10))
    ban_crowd.filled = True
    ban_crowd.fill_color = "Gold"
    window.add(ban_crowd)
    ban_crowd1 = GOval(10, 10, x=BAN_X+355, y=BAN_Y)
    ban_crowd1.filled = True
    ban_crowd1.fill_color = "Gold"
    window.add(ban_crowd1)
    ban_crowd2 = GOval(10, 10, x=BAN_X+385, y=BAN_Y)
    ban_crowd2.filled = True
    ban_crowd2.fill_color = "Gold"
    window.add(ban_crowd2)
    ban_crowd3 = GOval(10, 10, x=BAN_X+415, y=BAN_Y)
    ban_crowd3.filled = True
    ban_crowd3.fill_color = "Gold"
    window.add(ban_crowd3)
    crown_label = GLabel("1", x=BAN_X + 380, y=BAN_Y + 70)
    crown_label.font = "Times New Roman-30"
    crown_label.color = "black"
    window.add(crown_label)
    karel_b = GRect(410, 280, x=BAN_X, y=BAN_Y + 90)
    karel_b.filled = True
    karel_b.fill_color = "white"
    window.add(karel_b)
    karel_l1 = GLine(BAN_X+40, BAN_Y + 120, BAN_X+40, BAN_Y + 340)
    window.add(karel_l1)
    karel_l2 = GLine(BAN_X + 370, BAN_Y + 340, BAN_X + 40, BAN_Y + 340)
    window.add(karel_l2)
    karel_l3 = GLine(BAN_X + 370, BAN_Y + 300, BAN_X + 40, BAN_Y + 300)
    karel_l3.color = "Red"
    window.add(karel_l3)
    karel_l4 = GLine(BAN_X + 370, BAN_Y + 247, BAN_X + 40, BAN_Y + 247)
    karel_l4.color = "Red"
    window.add(karel_l4)
    karel_l5 = GLine(BAN_X + 370, BAN_Y + 194, BAN_X + 40, BAN_Y + 194)
    karel_l5.color = "Red"
    window.add(karel_l5)
    karel_l6 = GLine(BAN_X + 370, BAN_Y + 141, BAN_X + 40, BAN_Y + 141)
    karel_l6.color = "Red"
    window.add(karel_l6)
    karel_l7 = GLine(BAN_X+80, BAN_Y + 120, BAN_X+80, BAN_Y + 340)
    karel_l7.color = "Red"
    window.add(karel_l7)
    karel_l8 = GLine(BAN_X+133, BAN_Y + 120, BAN_X+133, BAN_Y + 340)
    karel_l8.color = "Red"
    window.add(karel_l8)
    karel_l9 = GLine(BAN_X+186, BAN_Y + 120, BAN_X+186, BAN_Y + 340)
    karel_l9.color = "Red"
    window.add(karel_l9)
    karel_l10 = GLine(BAN_X+239, BAN_Y + 120, BAN_X+239, BAN_Y + 340)
    karel_l10.color = "Red"
    window.add(karel_l10)
    karel_l11 = GLine(BAN_X+292, BAN_Y + 120, BAN_X+292, BAN_Y + 340)
    karel_l11.color = "Red"
    window.add(karel_l11)
    karel_l12 = GLine(BAN_X+345, BAN_Y + 120, BAN_X+345, BAN_Y + 340)
    karel_l12.color = "Red"
    window.add(karel_l12)
    karel_l13 = GLine(BAN_X + 212, BAN_Y + 340, BAN_X + 212, BAN_Y + 274)
    karel_l13.color = "black"
    window.add(karel_l13)
    karel_l13 = GLine(BAN_X + 370, BAN_Y + 274, BAN_X + 212, BAN_Y + 274)
    karel_l13.color = "black"
    window.add(karel_l13)
    axis_label1 = GLabel("1", x=BAN_X + 75, y=BAN_Y + 365)
    axis_label1.font = "Times New Roman-15"
    axis_label1.color = "black"
    window.add(axis_label1)
    axis_label2 = GLabel("2", x=BAN_X + 128, y=BAN_Y + 365)
    axis_label2.font = "Times New Roman-15"
    axis_label2.color = "black"
    window.add(axis_label2)
    axis_label3 = GLabel("3", x=BAN_X + 181, y=BAN_Y + 365)
    axis_label3.font = "Times New Roman-15"
    axis_label3.color = "black"
    window.add(axis_label3)
    axis_label4 = GLabel("4", x=BAN_X + 234, y=BAN_Y + 365)
    axis_label4.font = "Times New Roman-15"
    axis_label4.color = "black"
    window.add(axis_label4)
    axis_label5 = GLabel("5", x=BAN_X + 287, y=BAN_Y + 365)
    axis_label5.font = "Times New Roman-15"
    axis_label5.color = "black"
    window.add(axis_label5)
    axis_label6 = GLabel("6", x=BAN_X + 340, y=BAN_Y + 365)
    axis_label6.font = "Times New Roman-15"
    axis_label6.color = "black"
    window.add(axis_label6)
    axis_label7 = GLabel("1", x=BAN_X + 25, y=BAN_Y + 310)
    axis_label7.font = "Times New Roman-15"
    axis_label7.color = "black"
    window.add(axis_label7)
    axis_label8 = GLabel("2", x=BAN_X + 25, y=BAN_Y + 257)
    axis_label8.font = "Times New Roman-15"
    axis_label8.color = "black"
    window.add(axis_label8)
    axis_label9 = GLabel("3", x=BAN_X + 25, y=BAN_Y + 204)
    axis_label9.font = "Times New Roman-15"
    axis_label9.color = "black"
    window.add(axis_label9)
    axis_label10 = GLabel("4", x=BAN_X + 25, y=BAN_Y + 151)
    axis_label10.font = "Times New Roman-15"
    axis_label10.color = "black"
    window.add(axis_label10)
    ball_99 = GOval(24, 24, x=BAN_X + 227, y=BAN_Y + 235)
    ball_99.filled = True
    ball_99.fill_color = "blue"
    window.add(ball_99)
    ball_label1 = GLabel("99", x=BAN_X + 231, y=BAN_Y + 259)
    ball_label1.font = "Times New Roman-14"
    ball_label1.color = "white"
    window.add(ball_label1)
    karelw1 = GRect(24, 24, x=BAN_X + 274, y=BAN_Y + 235)
    karelw1.filled = True
    karelw1.fill_color = "blue"
    window.add(karelw1)
    karelw2 = GRect(18, 5, x=BAN_X + 277, y=BAN_Y + 259)
    karelw2.filled = True
    karelw2.fill_color = "lime"
    window.add(karelw2)
    karelw3 = GRect(18, 5, x=BAN_X + 277, y=BAN_Y + 230)
    karelw3.filled = True
    karelw3.fill_color = "lime"
    window.add(karelw3)
    karelw4 = GOval(14, 24, x=BAN_X + 298, y=BAN_Y + 235)
    karelw4.filled = True
    karelw4.fill_color = "lightgrey"
    window.add(karelw4)
    karelw5 = GRect(4, 4, x=BAN_X + 302, y=BAN_Y + 242)
    karelw5.filled = True
    karelw5.fill_color = "blue"
    window.add(karelw5)
    karelw6 = GRect(4, 4, x=BAN_X + 302, y=BAN_Y + 249)
    karelw6.filled = True
    karelw6.fill_color = "blue"
    window.add(karelw6)
    karelw7 = GOval(7, 9, x=BAN_X + 267, y=BAN_Y + 235)
    karelw7.filled = True
    karelw7.fill_color = "Red"
    window.add(karelw7)
    karelw8 = GOval(7, 9, x=BAN_X + 267, y=BAN_Y + 250)
    karelw8.filled = True
    karelw8.fill_color = "Red"
    window.add(karelw8)
    karelw9 = GLine(BAN_X + 278, BAN_Y + 240, BAN_X + 294, BAN_Y + 240)
    karelw9.color = "black"
    window.add(karelw9)
    karelw10 = GLine(BAN_X + 286, BAN_Y + 240, BAN_X + 280, BAN_Y + 252)
    karelw10.color = "black"
    window.add(karelw10)
    karelw11 = GLine(BAN_X + 286, BAN_Y + 240, BAN_X + 292, BAN_Y + 252)
    karelw11.color = "black"
    window.add(karelw11)
    title_label1 = GLabel("Put 99 beepers", x=BAN_X + 155, y=BAN_Y + 115)
    title_label1.font = "Times New Roman-14"
    title_label1.color = "black"
    window.add(title_label1)
    karel1 = GPolygon()
    karel1.add_vertex((BAN_X+20, BAN_Y + 450))
    karel1.add_vertex((BAN_X + 40, BAN_Y + 450))
    karel1.add_vertex((BAN_X + 40, BAN_Y + 435))
    karel1.add_vertex((BAN_X + 130, BAN_Y + 435))
    karel1.add_vertex((BAN_X + 130, BAN_Y + 450))
    karel1.add_vertex((BAN_X + 150, BAN_Y + 450))
    karel1.add_vertex((BAN_X + 150, BAN_Y + 580))
    karel1.add_vertex((BAN_X + 20, BAN_Y + 580))
    karel1.filled = True
    karel1.fill_color = "blue"
    window.add(karel1)
    karel2 = GOval(120, 60, x=BAN_X + 25, y=BAN_Y + 375)
    karel2.filled = True
    karel2.fill_color = "lightgrey"
    window.add(karel2)
    karel3 = GRect(15, 15, x=BAN_X + 55, y=BAN_Y + 402)
    karel3.filled = True
    karel3.fill_color = "blue"
    window.add(karel3)
    karel4 = GRect(15, 15, x=BAN_X + 100, y=BAN_Y + 402)
    karel4.filled = True
    karel4.fill_color = "blue"
    window.add(karel4)
    karel5 = GRect(20, 100, x=BAN_X, y=BAN_Y + 460)
    karel5.filled = True
    karel5.fill_color = "lime"
    window.add(karel5)
    karel6 = GRect(20, 100, x=BAN_X+150, y=BAN_Y + 460)
    karel6.filled = True
    karel6.fill_color = "lime"
    window.add(karel6)
    karel7 = GOval(50, 35, x=BAN_X + 30, y=BAN_Y + 580)
    karel7.filled = True
    karel7.fill_color = "red"
    window.add(karel7)
    karel8 = GOval(50, 35, x=BAN_X + 90, y=BAN_Y + 580)
    karel8.filled = True
    karel8.fill_color = "red"
    window.add(karel8)
    karel9 = GLine(BAN_X + 65, BAN_Y + 470, BAN_X + 65, BAN_Y + 560)
    karel9.color = "black"
    window.add(karel9)
    karel10 = GLine(BAN_X + 65, BAN_Y + 515, BAN_X + 120, BAN_Y + 470)
    karel10.color = "black"
    window.add(karel10)
    karel11 = GLine(BAN_X + 65, BAN_Y + 515, BAN_X + 120, BAN_Y + 560)
    karel11.color = "black"
    window.add(karel11)
    karelt = GPolygon()
    karelt.add_vertex((BAN_X+180, BAN_Y + 385))
    karelt.add_vertex((BAN_X + 410, BAN_Y + 385))
    karelt.add_vertex((BAN_X + 410, BAN_Y + 535))
    karelt.add_vertex((BAN_X + 180, BAN_Y + 535))
    karelt.add_vertex((BAN_X + 180, BAN_Y + 425))
    karelt.add_vertex((BAN_X + 160, BAN_Y + 412))
    karelt.add_vertex((BAN_X + 180, BAN_Y + 400))
    karelt.filled = "True"
    karelt.fill_color = "lightskyblue"
    window.add(karelt)
    karel_label1 = GLabel("Hi, I am Karel.", x=BAN_X + 190, y=BAN_Y + 410)
    karel_label1.font = "Helvetica-14"
    karel_label1.color = "black"
    window.add(karel_label1)
    karel_label2 = GLabel("I help beginners ", x=BAN_X + 190, y=BAN_Y + 430)
    karel_label2.font = "Helvetica-14"
    karel_label2.color = "black"
    window.add(karel_label2)
    karel_label3 = GLabel("to develop a passion", x=BAN_X + 190, y=BAN_Y + 450)
    karel_label3.font = "Helvetica-14"
    karel_label3.color = "black"
    window.add(karel_label3)
    karel_label4 = GLabel("for learning Python.", x=BAN_X + 190, y=BAN_Y + 470)
    karel_label4.font = "Helvetica-14"
    karel_label4.color = "black"
    window.add(karel_label4)
    karel_label5 = GLabel("Let's tackle challenges", x=BAN_X + 190, y=BAN_Y + 510)
    karel_label5.font = "Helvetica-14"
    karel_label5.color = "black"
    window.add(karel_label5)
    karel_label6 = GLabel("together !!!", x=BAN_X + 190, y=BAN_Y + 530)
    karel_label6.font = "Helvetica-14"
    karel_label6.color = "black"
    window.add(karel_label6)
    karel8b = GRect(165, 50, x=BAN_X + 245, y=BAN_Y + 555)
    karel8b.filled = False
    karel8b.fill_color = "red"
    window.add(karel8b)
    karel_label6 = GLabel("Founder: Jerry Liao", x=BAN_X + 250, y=BAN_Y + 580)
    karel_label6.font = "Times-14-italic"
    karel_label6.color = "black"
    window.add(karel_label6)
    karel_label7 = GLabel("Since 2019", x=BAN_X + 250, y=BAN_Y + 600)
    karel_label7.font = "Times-14-italic"
    karel_label7.color = "black"
    window.add(karel_label7)

    hair_of_boy = GArc(100, 125, 0, 180)
    hair_of_boy.filled = True
    hair_of_boy.fill_color = "Black"
    window.add(hair_of_boy, x=NOBI_F_X, y=NOBI_F_Y)
    hair_of_boy1 = GRect(5, 35)
    hair_of_boy1.filled = True
    hair_of_boy1.fill_color = "Black"
    window.add(hair_of_boy1, x=NOBI_F_X, y=NOBI_F_Y+30)
    hair_of_boy2 = GRect(5, 35)
    hair_of_boy2.filled = True
    hair_of_boy2.fill_color = "Black"
    window.add(hair_of_boy2, x=NOBI_F_X+95, y=NOBI_F_Y + 30)
    neck_of_boy = GRect(40, 13, x=NOBI_F_X+30, y=NOBI_F_Y + 115)
    neck_of_boy.fill_color = "antiquewhite"
    window.add(neck_of_boy)
    face_of_boy = GPolygon()
    face_of_boy.add_vertex((NOBI_F_X+5, NOBI_F_Y+30))
    face_of_boy.add_vertex((NOBI_F_X + 95, NOBI_F_Y + 30))
    face_of_boy.add_vertex((NOBI_F_X + 95, NOBI_F_Y + 92))
    face_of_boy.add_vertex((NOBI_F_X + 93, NOBI_F_Y + 99))
    face_of_boy.add_vertex((NOBI_F_X + 86, NOBI_F_Y + 105))
    face_of_boy.add_vertex((NOBI_F_X + 79, NOBI_F_Y + 110))
    face_of_boy.add_vertex((NOBI_F_X + 72, NOBI_F_Y + 114))
    face_of_boy.add_vertex((NOBI_F_X + 65, NOBI_F_Y + 117))
    face_of_boy.add_vertex((NOBI_F_X + 58, NOBI_F_Y + 119))
    face_of_boy.add_vertex((NOBI_F_X + 51, NOBI_F_Y + 120))
    face_of_boy.add_vertex((NOBI_F_X + 49, NOBI_F_Y + 120))
    face_of_boy.add_vertex((NOBI_F_X + 42, NOBI_F_Y + 119))
    face_of_boy.add_vertex((NOBI_F_X + 35, NOBI_F_Y + 117))
    face_of_boy.add_vertex((NOBI_F_X + 28, NOBI_F_Y + 114))
    face_of_boy.add_vertex((NOBI_F_X + 21, NOBI_F_Y + 110))
    face_of_boy.add_vertex((NOBI_F_X + 14, NOBI_F_Y + 105))
    face_of_boy.add_vertex((NOBI_F_X + 7, NOBI_F_Y + 99))
    face_of_boy.add_vertex((NOBI_F_X+5, NOBI_F_Y + 92))
    face_of_boy.filled = True
    face_of_boy.fill_color = "antiquewhite"
    window.add(face_of_boy)
    ear_of_boy = GPolygon()
    ear_of_boy.add_vertex((NOBI_F_X+5, NOBI_F_Y+50))
    ear_of_boy.add_vertex((NOBI_F_X + 5, NOBI_F_Y + 70))
    ear_of_boy.add_vertex((NOBI_F_X + 3, NOBI_F_Y + 78))
    ear_of_boy.add_vertex((NOBI_F_X - 5, NOBI_F_Y + 76))
    ear_of_boy.add_vertex((NOBI_F_X - 5, NOBI_F_Y + 44))
    ear_of_boy.add_vertex((NOBI_F_X + 3, NOBI_F_Y + 42))
    ear_of_boy.filled = True
    ear_of_boy.fill_color = "antiquewhite"
    window.add(ear_of_boy)
    ear2_of_boy = GPolygon()
    ear2_of_boy.add_vertex((NOBI_F_X + 95, NOBI_F_Y + 50))
    ear2_of_boy.add_vertex((NOBI_F_X + 95, NOBI_F_Y + 70))
    ear2_of_boy.add_vertex((NOBI_F_X + 97, NOBI_F_Y + 78))
    ear2_of_boy.add_vertex((NOBI_F_X + 103, NOBI_F_Y + 76))
    ear2_of_boy.add_vertex((NOBI_F_X + 103, NOBI_F_Y + 44))
    ear2_of_boy.add_vertex((NOBI_F_X + 97, NOBI_F_Y + 42))
    ear2_of_boy.filled = True
    ear2_of_boy.fill_color = "antiquewhite"
    window.add(ear2_of_boy)
    glass_of_boy_1 = GLine(NOBI_F_X+5, NOBI_F_Y+60, NOBI_F_X+15, NOBI_F_Y+60)
    window.add(glass_of_boy_1)
    glass_of_boy_2 = GLine(NOBI_F_X+85, NOBI_F_Y+60, NOBI_F_X+95, NOBI_F_Y+60)
    window.add(glass_of_boy_2)
    glass_of_boy_3 = GOval(30, 30, x=NOBI_F_X+15, y=NOBI_F_Y+45)
    glass_of_boy_3.filled = "True"
    glass_of_boy_3.fill_color = "white"
    window.add(glass_of_boy_3)
    glass_of_boy_4 = GLine(NOBI_F_X+45, NOBI_F_Y+60, NOBI_F_X+55, NOBI_F_Y+60)
    window.add(glass_of_boy_4)
    glass_of_boy_5 = GOval(30, 30, x=NOBI_F_X+55, y=NOBI_F_Y+45)
    glass_of_boy_5.filled = "True"
    glass_of_boy_5.fill_color = "white"
    window.add(glass_of_boy_5)
    left_eye_of_boy = GOval(7, 10)
    window.add(left_eye_of_boy, x=NOBI_F_X+30, y=NOBI_F_Y+55)
    left_eye_of_boy.filled = "True"
    left_eye_of_boy.fill_color = "Black"
    right_eye_of_boy = GOval(7, 10)
    window.add(right_eye_of_boy, x=NOBI_F_X+65, y=NOBI_F_Y+55)
    right_eye_of_boy.filled = "True"
    right_eye_of_boy.fill_color = "black"
    left_eye_of_boy2 = GOval(4, 4)
    window.add(left_eye_of_boy2, x=NOBI_F_X + 32, y=NOBI_F_Y + 58)
    left_eye_of_boy2.filled = "True"
    left_eye_of_boy2.fill_color = "white"
    right_eye_of_boy2 = GOval(4, 4)
    window.add(right_eye_of_boy2, x=NOBI_F_X + 67, y=NOBI_F_Y + 58)
    right_eye_of_boy2.filled = "True"
    right_eye_of_boy2.fill_color = "white"
    nose_of_boy = GOval(10, 10)
    window.add(nose_of_boy, x=NOBI_F_X + 45, y=NOBI_F_Y + 70)
    mouth_of_boy = GArc(40, 60, 0, -180)
    mouth_of_boy.filled = True
    mouth_of_boy.fill_color = "Red"
    window.add(mouth_of_boy, x=NOBI_F_X + 30, y=NOBI_F_Y + 75)
    eyebrow_of_boy = GArc(25, 25, 0, 180)
    window.add(eyebrow_of_boy, x=NOBI_F_X + 17, y=NOBI_F_Y + 38)
    eyebrow_of_boy1 = GArc(25, 25, 0, 180)
    window.add(eyebrow_of_boy1, x=NOBI_F_X + 57, y=NOBI_F_Y + 38)
    shirt_of_boy = GPolygon()
    shirt_of_boy.add_vertex((NOBI_F_X + 30, NOBI_F_Y + 128))
    shirt_of_boy.add_vertex((NOBI_F_X + 70, NOBI_F_Y + 128))
    shirt_of_boy.add_vertex((NOBI_F_X+100, NOBI_F_Y + 135))
    shirt_of_boy.add_vertex((NOBI_F_X + 125, NOBI_F_Y + 190))
    shirt_of_boy.add_vertex((NOBI_F_X + 138, NOBI_F_Y + 245))
    shirt_of_boy.add_vertex((NOBI_F_X + 113, NOBI_F_Y + 245))
    shirt_of_boy.add_vertex((NOBI_F_X + 90, NOBI_F_Y + 175))
    shirt_of_boy.add_vertex((NOBI_F_X + 90, NOBI_F_Y + 260))
    shirt_of_boy.add_vertex((NOBI_F_X + 10, NOBI_F_Y + 260))
    shirt_of_boy.add_vertex((NOBI_F_X + 10, NOBI_F_Y + 175))
    shirt_of_boy.add_vertex((NOBI_F_X, NOBI_F_Y + 185))
    shirt_of_boy.add_vertex((NOBI_F_X-25, NOBI_F_Y + 185))
    shirt_of_boy.add_vertex((NOBI_F_X - 45, NOBI_F_Y + 130))
    shirt_of_boy.add_vertex((NOBI_F_X - 20, NOBI_F_Y + 130))
    shirt_of_boy.add_vertex((NOBI_F_X-10, NOBI_F_Y + 157))
    shirt_of_boy.add_vertex((NOBI_F_X, NOBI_F_Y + 135))
    shirt_of_boy.filled = True
    shirt_of_boy.fill_color = "gold"
    window.add(shirt_of_boy)
    t1_shirt_of_boy = GPolygon()
    t1_shirt_of_boy.add_vertex((NOBI_F_X + 30, NOBI_F_Y + 128))
    t1_shirt_of_boy.add_vertex((NOBI_F_X + 50, NOBI_F_Y + 128))
    t1_shirt_of_boy.add_vertex((NOBI_F_X + 30, NOBI_F_Y + 145))
    t1_shirt_of_boy.filled = True
    t1_shirt_of_boy.fill_color = "white"
    window.add(t1_shirt_of_boy)
    t2_shirt_of_boy = GPolygon()
    t2_shirt_of_boy.add_vertex((NOBI_F_X + 50, NOBI_F_Y + 128))
    t2_shirt_of_boy.add_vertex((NOBI_F_X + 70, NOBI_F_Y + 128))
    t2_shirt_of_boy.add_vertex((NOBI_F_X + 70, NOBI_F_Y + 145))
    t2_shirt_of_boy.filled = True
    t2_shirt_of_boy.fill_color = "white"
    window.add(t2_shirt_of_boy)
    hand_of_boy = GPolygon()
    hand_of_boy.add_vertex((NOBI_F_X-29, NOBI_F_Y + 130))
    hand_of_boy.add_vertex((NOBI_F_X-36, NOBI_F_Y + 130))
    hand_of_boy.add_vertex((NOBI_F_X - 38, NOBI_F_Y + 106))
    hand_of_boy.add_vertex((NOBI_F_X - 18, NOBI_F_Y + 103))
    hand_of_boy.add_vertex((NOBI_F_X - 18, NOBI_F_Y + 107))
    hand_of_boy.add_vertex((NOBI_F_X - 32, NOBI_F_Y + 111))
    hand_of_boy.add_vertex((NOBI_F_X - 31, NOBI_F_Y + 120))
    hand_of_boy.add_vertex((NOBI_F_X - 21, NOBI_F_Y + 120))
    hand_of_boy.add_vertex((NOBI_F_X - 21, NOBI_F_Y + 124))
    hand_of_boy.add_vertex((NOBI_F_X - 28, NOBI_F_Y + 127))
    hand_of_boy.filled = True
    hand_of_boy.fill_color = "Antiquewhite"
    window.add(hand_of_boy)
    handl_of_boy = GPolygon()
    handl_of_boy.add_vertex((NOBI_F_X + 136, NOBI_F_Y + 245))
    handl_of_boy.add_vertex((NOBI_F_X + 115, NOBI_F_Y + 245))
    handl_of_boy.add_vertex((NOBI_F_X + 110, NOBI_F_Y + 256))
    handl_of_boy.add_vertex((NOBI_F_X + 116, NOBI_F_Y + 256))
    handl_of_boy.add_vertex((NOBI_F_X + 116, NOBI_F_Y + 260))
    handl_of_boy.add_vertex((NOBI_F_X + 122, NOBI_F_Y + 260))
    handl_of_boy.add_vertex((NOBI_F_X + 122, NOBI_F_Y + 262))
    handl_of_boy.add_vertex((NOBI_F_X + 128, NOBI_F_Y + 262))
    handl_of_boy.add_vertex((NOBI_F_X + 128, NOBI_F_Y + 260))
    handl_of_boy.add_vertex((NOBI_F_X + 134, NOBI_F_Y + 260))
    handl_of_boy.add_vertex((NOBI_F_X + 134, NOBI_F_Y + 256))
    handl_of_boy.add_vertex((NOBI_F_X + 140, NOBI_F_Y + 256))
    handl_of_boy.filled = True
    handl_of_boy.fill_color = "Antiquewhite"
    window.add(handl_of_boy)
    pant_of_boy = GPolygon()
    pant_of_boy.add_vertex((NOBI_F_X + 10, NOBI_F_Y + 260))
    pant_of_boy.add_vertex((NOBI_F_X + 90, NOBI_F_Y + 260))
    pant_of_boy.add_vertex((NOBI_F_X + 90, NOBI_F_Y + 330))
    pant_of_boy.add_vertex((NOBI_F_X + 55, NOBI_F_Y + 330))
    pant_of_boy.add_vertex((NOBI_F_X + 50, NOBI_F_Y + 285))
    pant_of_boy.add_vertex((NOBI_F_X + 45, NOBI_F_Y + 330))
    pant_of_boy.add_vertex((NOBI_F_X + 10, NOBI_F_Y + 330))
    pant_of_boy.filled = True
    pant_of_boy.fill_color = "navy"
    window.add(pant_of_boy)
    leg_of_boy = GRect(23, 75, x=NOBI_F_X + 16, y=NOBI_F_Y + 330)
    leg_of_boy.filled = True
    leg_of_boy.fill_color = "antiquewhite"
    window.add(leg_of_boy)
    leg1_of_boy = GRect(23, 75, x=NOBI_F_X + 61, y=NOBI_F_Y + 330)
    leg1_of_boy.filled = True
    leg1_of_boy.fill_color = "antiquewhite"
    window.add(leg1_of_boy)
    shoe1_of_boy = GPolygon()
    shoe1_of_boy.add_vertex((NOBI_F_X + 16, NOBI_F_Y + 405))
    shoe1_of_boy.add_vertex((NOBI_F_X + 39, NOBI_F_Y + 405))
    shoe1_of_boy.add_vertex((NOBI_F_X + 39, NOBI_F_Y + 420))
    shoe1_of_boy.add_vertex((NOBI_F_X + 5, NOBI_F_Y + 420))
    shoe1_of_boy.add_vertex((NOBI_F_X + 5, NOBI_F_Y + 415))
    shoe1_of_boy.filled = True
    shoe1_of_boy.fill_color = "aqua"
    window.add(shoe1_of_boy)
    shoe1_of_boy = GPolygon()
    shoe1_of_boy.add_vertex((NOBI_F_X + 84, NOBI_F_Y + 405))
    shoe1_of_boy.add_vertex((NOBI_F_X + 61, NOBI_F_Y + 405))
    shoe1_of_boy.add_vertex((NOBI_F_X + 61, NOBI_F_Y + 420))
    shoe1_of_boy.add_vertex((NOBI_F_X + 95, NOBI_F_Y + 420))
    shoe1_of_boy.add_vertex((NOBI_F_X + 95, NOBI_F_Y + 415))
    shoe1_of_boy.filled = True
    shoe1_of_boy.fill_color = "aqua"
    window.add(shoe1_of_boy)

    neck_of_conan = GRect(30, 10, x=CONAN_F_X+35, y=CONAN_F_Y+71)
    neck_of_boy.filled = True
    neck_of_conan.fill_color = "antiquewhite"
    window.add(neck_of_conan)
    face_of_conan = GPolygon()
    face_of_conan.add_vertex((CONAN_F_X, CONAN_F_Y))
    face_of_conan.add_vertex((CONAN_F_X+10, CONAN_F_Y+60))
    face_of_conan.add_vertex((CONAN_F_X+45, CONAN_F_Y+75))
    face_of_conan.add_vertex((CONAN_F_X + 55, CONAN_F_Y + 75))
    face_of_conan.add_vertex((CONAN_F_X + 90, CONAN_F_Y + 60))
    face_of_conan.add_vertex((CONAN_F_X + 100, CONAN_F_Y))
    face_of_conan.filled = True
    face_of_conan.fill_color = "antiquewhite"
    window.add(face_of_conan)
    hair_of_conan = GArc(100, 120, 0, 180)
    hair_of_conan.filled = True
    hair_of_conan.fill_color = "Black"
    window.add(hair_of_conan, x=CONAN_F_X, y=CONAN_F_Y-25)
    hair_of_conan_1 = GPolygon()
    hair_of_conan_1.add_vertex((CONAN_F_X+70, CONAN_F_Y-20))
    hair_of_conan_1.add_vertex((CONAN_F_X + 80, CONAN_F_Y - 40))
    hair_of_conan_1.add_vertex((CONAN_F_X + 90, CONAN_F_Y - 30))
    hair_of_conan_1.add_vertex((CONAN_F_X + 80, CONAN_F_Y - 20))
    hair_of_conan_1.filled = True
    hair_of_conan_1.fill_color = "Black"
    window.add(hair_of_conan_1)
    hair_of_conan_2 = GPolygon()
    hair_of_conan_2.add_vertex((CONAN_F_X, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 5, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 5, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 8, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 8, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 13, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 13, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X+15, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X+15, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 20, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 20, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 23, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 23, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 28, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 28, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 30, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 30, CONAN_F_Y + 11))
    hair_of_conan_2.add_vertex((CONAN_F_X + 35, CONAN_F_Y + 12))
    hair_of_conan_2.add_vertex((CONAN_F_X + 35, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 38, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 38, CONAN_F_Y + 12))
    hair_of_conan_2.add_vertex((CONAN_F_X + 43, CONAN_F_Y + 13))
    hair_of_conan_2.add_vertex((CONAN_F_X + 43, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 48, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 48, CONAN_F_Y+10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 50, CONAN_F_Y+13))
    hair_of_conan_2.add_vertex((CONAN_F_X + 55, CONAN_F_Y + 20))
    hair_of_conan_2.add_vertex((CONAN_F_X + 58, CONAN_F_Y + 23))
    hair_of_conan_2.add_vertex((CONAN_F_X + 57, CONAN_F_Y + 20))
    hair_of_conan_2.add_vertex((CONAN_F_X + 54, CONAN_F_Y+10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 54, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 60, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 60, CONAN_F_Y + 13))
    hair_of_conan_2.add_vertex((CONAN_F_X + 65, CONAN_F_Y + 12))
    hair_of_conan_2.add_vertex((CONAN_F_X + 65, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 68, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 68, CONAN_F_Y + 12))
    hair_of_conan_2.add_vertex((CONAN_F_X + 73, CONAN_F_Y + 11))
    hair_of_conan_2.add_vertex((CONAN_F_X + 73, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 70, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 70, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 75, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 75, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 78, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 78, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 83, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 83, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 85, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 85, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 90, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 90, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 93, CONAN_F_Y))
    hair_of_conan_2.add_vertex((CONAN_F_X + 93, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 98, CONAN_F_Y + 10))
    hair_of_conan_2.add_vertex((CONAN_F_X + 98, CONAN_F_Y))
    hair_of_conan_2.filled = True
    hair_of_conan_2.fill_color = "Black"
    window.add(hair_of_conan_2)
    hair_of_conan_3 = GPolygon()
    hair_of_conan_3.add_vertex((CONAN_F_X, CONAN_F_Y))
    hair_of_conan_3.add_vertex((CONAN_F_X, CONAN_F_Y + 10))
    hair_of_conan_3.add_vertex((CONAN_F_X + 5, CONAN_F_Y + 10))
    hair_of_conan_3.add_vertex((CONAN_F_X + 5, CONAN_F_Y))
    hair_of_conan_3.add_vertex((CONAN_F_X + 8, CONAN_F_Y))
    hair_of_conan_3.add_vertex((CONAN_F_X + 8, CONAN_F_Y + 10))
    hair_of_conan_3.add_vertex((CONAN_F_X + 13, CONAN_F_Y + 10))
    hair_of_conan_3.filled = True
    hair_of_conan_3.fill_color = "Black"
    window.add(hair_of_conan_3)
    hair_of_conan_4 = GArc(40, 20, 0, 180)
    hair_of_conan_4.filled = True
    hair_of_conan_4.fill_color = "Black"
    window.add(hair_of_conan_4, x=CONAN_F_X + 3, y=CONAN_F_Y - 18)
    hair_of_conan_5 = GArc(40, 20, 0, 180)
    hair_of_conan_5.filled = True
    hair_of_conan_5.fill_color = "Black"
    window.add(hair_of_conan_5, x=CONAN_F_X-5, y=CONAN_F_Y - 11)
    hair_of_conan_6 = GArc(55, 10, 30, 170)
    hair_of_conan_6.filled = True
    hair_of_conan_6.fill_color = "Black"
    window.add(hair_of_conan_6, x=CONAN_F_X - 12, y=CONAN_F_Y - 4)
    glass_of_conan_1 = GLine(CONAN_F_X+4, CONAN_F_Y+30, CONAN_F_X+20, CONAN_F_Y+30)
    window.add(glass_of_conan_1)
    glass_of_conan_2 = GLine(CONAN_F_X+95, CONAN_F_Y+30, CONAN_F_X+79, CONAN_F_Y+30)
    window.add(glass_of_conan_2)
    glass_of_conan_3 = GOval(25, 25, x=CONAN_F_X+20, y=CONAN_F_Y+18)
    window.add(glass_of_conan_3)
    glass_of_conan_4 = GLine(CONAN_F_X+45, CONAN_F_Y+30, CONAN_F_X+54, CONAN_F_Y+30)
    window.add(glass_of_conan_4)
    glass_of_conan_5 = GOval(25, 25, x=CONAN_F_X+54, y=CONAN_F_Y+18)
    window.add(glass_of_conan_5)
    nose_of_conan = GPolygon()
    nose_of_conan.add_vertex((CONAN_F_X+50, CONAN_F_Y+39))
    nose_of_conan.add_vertex((CONAN_F_X+46, CONAN_F_Y + 42))
    nose_of_conan.add_vertex((CONAN_F_X + 50, CONAN_F_Y + 45))
    nose_of_conan.fill_color = "Black"
    window.add(nose_of_conan)
    mouth_of_conan = GArc(40, 40, 0, -180)
    mouth_of_conan.filled = True
    mouth_of_conan.fill_color = "Red"
    window.add(mouth_of_conan, x=CONAN_F_X + 30, y=CONAN_F_Y + 45)
    ear_of_conan = GPolygon()
    ear_of_conan.add_vertex((CONAN_F_X+2, CONAN_F_Y+20))
    ear_of_conan.add_vertex((CONAN_F_X-2, CONAN_F_Y + 17))
    ear_of_conan.add_vertex((CONAN_F_X - 4, CONAN_F_Y + 19))
    ear_of_conan.add_vertex((CONAN_F_X-4, CONAN_F_Y+43))
    ear_of_conan.add_vertex((CONAN_F_X-2, CONAN_F_Y + 45))
    ear_of_conan.add_vertex((CONAN_F_X + 5, CONAN_F_Y + 40))
    ear_of_conan.filled = True
    ear_of_conan.fill_color = "antiquewhite"
    window.add(ear_of_conan)
    ear1_of_conan = GPolygon()
    ear1_of_conan.add_vertex((CONAN_F_X+97, CONAN_F_Y+20))
    ear1_of_conan.add_vertex((CONAN_F_X+101, CONAN_F_Y + 17))
    ear1_of_conan.add_vertex((CONAN_F_X+103, CONAN_F_Y + 19))
    ear1_of_conan.add_vertex((CONAN_F_X+103, CONAN_F_Y+43))
    ear1_of_conan.add_vertex((CONAN_F_X+101, CONAN_F_Y + 45))
    ear1_of_conan.add_vertex((CONAN_F_X+94, CONAN_F_Y + 40))
    ear1_of_conan.filled = True
    ear1_of_conan.fill_color = "antiquewhite"
    window.add(ear1_of_conan)
    left_eye_of_conan = GArc(10, 20, 0, 180)
    window.add(left_eye_of_conan, x=CONAN_F_X + 27, y=CONAN_F_Y + 27)
    right_eye_of_conan = GArc(10, 20, 0, 180)
    window.add(right_eye_of_conan, x=CONAN_F_X + 61, y=CONAN_F_Y + 27)
    leg1_of_conan = GRect(15, 30, x=CONAN_F_X+5, y=CONAN_F_Y + 260)
    leg1_of_conan.filled = True
    leg1_of_conan.fill_color = "antiquewhite"
    window.add(leg1_of_conan)
    leg2_of_conan = GRect(15, 30, x=CONAN_F_X+80, y=CONAN_F_Y + 260)
    leg2_of_conan.filled = True
    leg2_of_conan.fill_color = "antiquewhite"
    window.add(leg2_of_conan)
    pant_of_conan = GPolygon()
    pant_of_conan.add_vertex((CONAN_F_X+7, CONAN_F_Y+180))
    pant_of_conan.add_vertex((CONAN_F_X+93, CONAN_F_Y + 180))
    pant_of_conan.add_vertex((CONAN_F_X + 105, CONAN_F_Y + 260))
    pant_of_conan.add_vertex((CONAN_F_X + 70, CONAN_F_Y + 260))
    pant_of_conan.add_vertex((CONAN_F_X + 50, CONAN_F_Y + 230))
    pant_of_conan.add_vertex((CONAN_F_X + 30, CONAN_F_Y + 260))
    pant_of_conan.add_vertex((CONAN_F_X - 5, CONAN_F_Y + 260))
    pant_of_conan.filled = True
    pant_of_conan.fill_color = "dimgrey"
    window.add(pant_of_conan)
    shoe1_of_conan = GPolygon()
    shoe1_of_conan.add_vertex((CONAN_F_X, CONAN_F_Y + 290))
    shoe1_of_conan.add_vertex((CONAN_F_X + 20, CONAN_F_Y + 290))
    shoe1_of_conan.add_vertex((CONAN_F_X + 20, CONAN_F_Y + 300))
    shoe1_of_conan.add_vertex((CONAN_F_X - 15, CONAN_F_Y + 300))
    shoe1_of_conan.add_vertex((CONAN_F_X - 15, CONAN_F_Y + 295))
    shoe1_of_conan.filled = True
    shoe1_of_conan.fill_color = "red"
    window.add(shoe1_of_conan)
    shoe2_of_conan = GPolygon()
    shoe2_of_conan.add_vertex((CONAN_F_X+80, CONAN_F_Y + 290))
    shoe2_of_conan.add_vertex((CONAN_F_X + 100, CONAN_F_Y + 290))
    shoe2_of_conan.add_vertex((CONAN_F_X + 115, CONAN_F_Y + 295))
    shoe2_of_conan.add_vertex((CONAN_F_X + 115, CONAN_F_Y + 300))
    shoe2_of_conan.add_vertex((CONAN_F_X + 80, CONAN_F_Y + 300))
    shoe2_of_conan.filled = True
    shoe2_of_conan.fill_color = "red"
    window.add(shoe2_of_conan)
    coat_of_conan = GPolygon()
    coat_of_conan.add_vertex((CONAN_F_X+35, CONAN_F_Y+81))
    coat_of_conan.add_vertex((CONAN_F_X+65, CONAN_F_Y + 81))
    coat_of_conan.add_vertex((CONAN_F_X+100, CONAN_F_Y + 86))
    coat_of_conan.add_vertex((CONAN_F_X + 120, CONAN_F_Y + 131))
    coat_of_conan.add_vertex((CONAN_F_X + 130, CONAN_F_Y + 176))
    coat_of_conan.add_vertex((CONAN_F_X + 110, CONAN_F_Y + 176))
    coat_of_conan.add_vertex((CONAN_F_X + 95, CONAN_F_Y + 131))
    coat_of_conan.add_vertex((CONAN_F_X + 95, CONAN_F_Y + 200))
    coat_of_conan.add_vertex((CONAN_F_X + 60, CONAN_F_Y + 200))
    coat_of_conan.add_vertex((CONAN_F_X + 50, CONAN_F_Y + 180))
    coat_of_conan.add_vertex((CONAN_F_X + 40, CONAN_F_Y + 200))
    coat_of_conan.add_vertex((CONAN_F_X+5, CONAN_F_Y + 200))
    coat_of_conan.add_vertex((CONAN_F_X+5, CONAN_F_Y + 131))
    coat_of_conan.add_vertex((CONAN_F_X-2, CONAN_F_Y + 138))
    coat_of_conan.add_vertex((CONAN_F_X - 22, CONAN_F_Y + 138))
    coat_of_conan.add_vertex((CONAN_F_X - 37, CONAN_F_Y + 86))
    coat_of_conan.add_vertex((CONAN_F_X - 17, CONAN_F_Y + 86))
    coat_of_conan.add_vertex((CONAN_F_X-10, CONAN_F_Y + 110))
    coat_of_conan.add_vertex((CONAN_F_X, CONAN_F_Y + 86))
    coat_of_conan.filled = True
    coat_of_conan.fill_color = "navy"
    window.add(coat_of_conan)
    hand_of_conan = GPolygon()
    hand_of_conan.add_vertex((CONAN_F_X-25, CONAN_F_Y + 86))
    hand_of_conan.add_vertex((CONAN_F_X-30, CONAN_F_Y + 86))
    hand_of_conan.add_vertex((CONAN_F_X - 32, CONAN_F_Y + 67))
    hand_of_conan.add_vertex((CONAN_F_X - 15, CONAN_F_Y + 65))
    hand_of_conan.add_vertex((CONAN_F_X - 15, CONAN_F_Y + 68))
    hand_of_conan.add_vertex((CONAN_F_X - 26, CONAN_F_Y + 71))
    hand_of_conan.add_vertex((CONAN_F_X - 25, CONAN_F_Y + 78))
    hand_of_conan.add_vertex((CONAN_F_X - 18, CONAN_F_Y + 78))
    hand_of_conan.add_vertex((CONAN_F_X - 18, CONAN_F_Y + 81))
    hand_of_conan.add_vertex((CONAN_F_X - 24, CONAN_F_Y + 83))
    hand_of_conan.filled = True
    hand_of_conan.fill_color = "Antiquewhite"
    window.add(hand_of_conan)
    handl_of_conan = GPolygon()
    handl_of_conan.add_vertex((CONAN_F_X + 128, CONAN_F_Y + 176))
    handl_of_conan.add_vertex((CONAN_F_X + 112, CONAN_F_Y + 176))
    handl_of_conan.add_vertex((CONAN_F_X + 110, CONAN_F_Y + 185))
    handl_of_conan.add_vertex((CONAN_F_X + 114, CONAN_F_Y + 185))
    handl_of_conan.add_vertex((CONAN_F_X + 114, CONAN_F_Y + 188))
    handl_of_conan.add_vertex((CONAN_F_X + 118, CONAN_F_Y + 188))
    handl_of_conan.add_vertex((CONAN_F_X + 118, CONAN_F_Y + 189))
    handl_of_conan.add_vertex((CONAN_F_X + 122, CONAN_F_Y + 189))
    handl_of_conan.add_vertex((CONAN_F_X + 122, CONAN_F_Y + 188))
    handl_of_conan.add_vertex((CONAN_F_X + 126, CONAN_F_Y + 188))
    handl_of_conan.add_vertex((CONAN_F_X + 126, CONAN_F_Y + 185))
    handl_of_conan.add_vertex((CONAN_F_X + 130, CONAN_F_Y + 185))
    handl_of_conan.filled = True
    handl_of_conan.fill_color = "Antiquewhite"
    window.add(handl_of_conan)
    suit_of_conan = GPolygon()
    suit_of_conan.add_vertex((CONAN_F_X + 35, CONAN_F_Y + 81))
    suit_of_conan.add_vertex((CONAN_F_X + 65, CONAN_F_Y + 81))
    suit_of_conan.add_vertex((CONAN_F_X + 75, CONAN_F_Y + 82))
    suit_of_conan.add_vertex((CONAN_F_X + 65, CONAN_F_Y + 120))
    suit_of_conan.add_vertex((CONAN_F_X + 50, CONAN_F_Y + 160))
    suit_of_conan.add_vertex((CONAN_F_X + 35, CONAN_F_Y + 120))
    suit_of_conan.add_vertex((CONAN_F_X + 25, CONAN_F_Y + 83))
    suit_of_conan.filled = True
    suit_of_conan.fill_color = "White"
    window.add(suit_of_conan)
    button_of_conan = GOval(20, 20, x=CONAN_F_X+40, y=CONAN_F_Y+160)
    button_of_conan.filled = True
    button_of_conan.fill_color = "Gold"
    window.add(button_of_conan)
    suit_line_of_conan = GLine(CONAN_F_X+50, CONAN_F_Y + 81, CONAN_F_X+50, CONAN_F_Y+160)
    window.add(suit_line_of_conan)
    tie1_of_conan = GOval(14, 14, x=CONAN_F_X + 43, y=CONAN_F_Y + 90)
    tie1_of_conan.filled = True
    tie1_of_conan.fill_color = "Red"
    window.add(tie1_of_conan)
    tie2_of_conan = GPolygon()
    tie2_of_conan.add_vertex((CONAN_F_X + 43, CONAN_F_Y + 93))
    tie2_of_conan.add_vertex((CONAN_F_X + 43, CONAN_F_Y + 101))
    tie2_of_conan.add_vertex((CONAN_F_X + 33, CONAN_F_Y + 104))
    tie2_of_conan.add_vertex((CONAN_F_X + 33, CONAN_F_Y + 90))
    tie2_of_conan.filled = True
    tie2_of_conan.fill_color = "Red"
    window.add(tie2_of_conan)
    tie3_of_conan = GPolygon()
    tie3_of_conan.add_vertex((CONAN_F_X + 57, CONAN_F_Y + 93))
    tie3_of_conan.add_vertex((CONAN_F_X + 57, CONAN_F_Y + 101))
    tie3_of_conan.add_vertex((CONAN_F_X + 67, CONAN_F_Y + 104))
    tie3_of_conan.add_vertex((CONAN_F_X + 67, CONAN_F_Y + 90))
    tie3_of_conan.filled = True
    tie3_of_conan.fill_color = "Red"
    window.add(tie3_of_conan)

    window.add(position_label, x=900, y=position_label.height + 10)
    onmousemoved(position)


def position(axis):
    global n, a, b
    if n == 1:
        a = 900
        b = position_label.height + 10
        n += 1
    else:
        prior_obj = window.get_object_at(a, b)
        if prior_obj is not None:
            window.remove(prior_obj)
        position_label2 = GLabel("x:" + str(axis.x) + "y:" + str(axis.y))
        position_label2.font = "-10"
        window.add(position_label2, x=900, y=position_label2.height + 10)


if __name__ == '__main__':
    main()
