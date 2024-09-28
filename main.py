import easygui,math
while True:
    f = easygui.buttonbox('欢迎使用方程求解器，请选择方程',choices=('一元一次方程','一元二次方程','二元一次方程','退出'))
    if f == "退出":
        break
    elif f == "一元一次方程":
        num = easygui.multenterbox(msg="kx + b = a(k≠0且k,b,a为常数)", title="一元一次方程", fields=["k = ","b = ","a = "])
        try:
            k = int(num[0])
            b = int(num[1])
            a = int(num[2])
            x = (a - b) / k
            easygui.msgbox("x = " + str(x))
        except:
            easygui.msgbox("数据错误")
    elif f == "一元二次方程":
        num = easygui.multenterbox(msg="ax^2 + bx + c = 0(a≠0且a,b,c为常数)", title="一元二次方程", fields=["a = ","b = ","c = "])
        try:
            a = int(num[0])
            b = int(num[1])
            c = int(num[2])
            tf = b * b - 4 * a * c
            if tf < 0:
                easygui.msgbox("方程无实数根")
            elif tf == 0:
                x = (b * -1 + math.sqrt(tf)) / (2 * a)
                easygui.msgbox("x1 = x2 = " + str(x))
            elif tf > 0:
                x1 = (b * -1 + math.sqrt(tf)) / (2 * a)
                x2 = (b * -1 - math.sqrt(tf)) / (2 * a)
                easygui.msgbox("x1 = " + str(x1) + " , x2 = " + str(x2))
        except:
            easygui.msgbox("数据错误")
    elif f == "二元一次方程":
        num = easygui.multenterbox(msg="""ax + by = c
dx + ey = f
(a,b,d,e≠0且a,b,c,d,e,f为常数)""", title="二元一次方程", fields=["a = ","b = ","c = ","d = ","e = ","f = "])
        try:
            a = int(num[0])
            b = int(num[1])
            c = int(num[2])
            d = int(num[3])
            e = int(num[4])
            f = int(num[5])
            x = c/a - (a * b * f - b * c * d)/(a * a * e - a * b * d)
            y = (a * f - c * d)/(a * e - b * d)
            easygui.msgbox("x = " + str(x)+" , y = " + str(y))
        except:
            easygui.msgbox("数据错误")
