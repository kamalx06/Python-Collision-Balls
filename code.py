from tkinter import Tk, Canvas

def roll():
    global dx, dy, ball_x, ball_y, dx2, dy2, ball_x2, ball_y2

    ball_x += dx
    ball_y += dy
    ball_x2 += dx2
    ball_y2 += dy2

    if ball_x > 700 or ball_x < 0:
        dx = -dx
    canv.coords(oval, ball_x, ball_y, ball_x + 100, ball_y + 100)
    canv.coords(rectangle, rectangle_x, rectangle_y, rectangle_x1, rectangle_y1)
    if ball_y > 500 or ball_y < 0:
        dy = -dy
    canv.coords(oval, ball_x, ball_y, ball_x + 100, ball_y + 100)
    canv.coords(rectangle, rectangle_x, rectangle_y, rectangle_x1, rectangle_y1)
    if ball_x2 > 698 or ball_x2 < 0:
        dx2 = -dx2
    canv.coords(oval2, ball_x2, ball_y2, ball_x2 + 100, ball_y2 + 100)
    canv.coords(rectangle, rectangle_x, rectangle_y, rectangle_x1, rectangle_y1)
    if ball_y2 > 498 or ball_y2 < 0:
        dy2 = -dy2
    canv.coords(oval2, ball_x2, ball_y2, ball_x2 + 100, ball_y2 + 100)
    canv.coords(rectangle, rectangle_x, rectangle_y, rectangle_x1, rectangle_y1)

    form.after(10, roll)

def collisionDetection():
    global dx, dy, ball_x, ball_y, dx2, dy2, ball_x2, ball_y2

    ball_x = ball_x + dx
    ball_y = ball_y + dy
    ball_x2 = ball_x2 + dx2
    ball_y2 = ball_y2 + dy2

    if (ball_x + 100 >= rectangle_x and ball_x <= rectangle_x1 and
        ball_y + 100 >= rectangle_y and ball_y <= rectangle_y1):
        dx = -dx
        dy = -dy

    if (ball_x2 + 100 >= rectangle_x and ball_x2 <= rectangle_x1 and
        ball_y2 + 100 >= rectangle_y and ball_y2 <= rectangle_y1):
        dx2 = -dx2
        dy2 = -dy2
    
    form.after(10, collisionDetection)

form = Tk()
form.title("Canvas")
form.geometry("800x600")

canv = Canvas(form, width=800, height=600, bg="lightblue")
canv.pack()

# Left ball
ball_x = 2
ball_y = 2
dx = 5
dy = 5

# Right ball
ball_x2 = 698
ball_y2 = 498
dx2 = 5
dy2 = 5

# Rectangle
rectangle_x = 350
rectangle_y = 250
rectangle_x1 = 450
rectangle_y1 = 350

oval = canv.create_oval(ball_x, ball_y, ball_x + 100, ball_y + 100, fill="red")
oval2 = canv.create_oval(ball_x2, ball_y2, ball_x2 + 100, ball_y2 + 100, fill="blue")
rectangle = canv.create_rectangle(rectangle_x, rectangle_y, rectangle_x1, rectangle_y1, fill="gray")

form.after(0, roll)
form.after(0, collisionDetection)

form.mainloop()
