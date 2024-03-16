import turtle

def draw_pifagor_tree(t, branch_length, levels):
    if levels == 0:
        return
    t.forward(branch_length)
    t.left(45)
    draw_pifagor_tree(t, 0.6 * branch_length, levels-1)
    t.right(90)
    draw_pifagor_tree(t, 0.6 * branch_length, levels-1)
    t.left(45)
    t.backward(branch_length)

def main():
    levels = int(input("Введіть рівень рекурсії: "))
    branch_length = 100
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    t.speed(0)
    t.color("green")
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    draw_pifagor_tree(t, branch_length, levels)
    screen.mainloop()

if __name__ == "__main__":
    main()