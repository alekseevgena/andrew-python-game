import gameController

window = gameController.GameWindow(1024, 768, "test")
window.set_bg_color(255,255,255)
obj = gameController.GameObject(window, "man.png")
while True:
    for i in window.get_events():
        if i.type == window.QUIT:
            window.exit()
    window.tick(obj)
    obj.move(1,1)


        