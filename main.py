
from turtle import Screen
from player import Player
import time
from invader import Invader
from score import Scoreboard


screen = Screen()
screen.setup(680,660)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
invader = Invader()
score = Scoreboard()
screen.listen()

screen.onkey(player.turn_right, "Right" )
screen.onkey(player.turn_left, "Left" )
screen.onkey(player.create_missile, "space" )


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    player.fire()
    invader.create_invader()
    invader.move()
    screen.update()


    for i in invader.enemies:
        for m in player.missiles:
            if m.distance(i)<15:
                player.missiles.remove(m)
                invader.enemies.remove(i)
                m.hideturtle()
                i.hideturtle()
                score.increase_score()
            if m.distance(player)>600:
                    player.missiles.remove(m)
                    m.hideturtle()

        if i.distance(player)<15:
            score.game_over()
            game_is_on = False


screen.exitonclick()


