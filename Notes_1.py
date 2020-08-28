    def i(self):
        self.goto(self.xcor(), self.ycor() + self.in_game_speed)

    def w(self):
        self.goto(self.xcor(), self.ycor() + self.in_game_speed)

    def k(self):
        self.goto(self.xcor(), self.ycor() - self.in_game_speed)

    def s(self):
        self.goto(self.xcor(), self.ycor() - self.in_game_speed)



screen.onkeypress(player.up, "i")
screen.onkeypress(player.up, "w")
screen.onkeypress(player.down, "k")
screen.onkeypress(player.down, "s")