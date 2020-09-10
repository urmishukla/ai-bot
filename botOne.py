import turtle

#wn= turtle.getscreen()
wn=turtle.Screen()
wn.title("AI bot by @urmishukla")
wn.setup(width=800,height=500)
wn.bgcolor("lightcoral")
wn.tracer(0)
#wn.hideturtle()

wn.register_shape("happy.gif")
wn.register_shape("sad.gif")
wn.register_shape("neutral.gif")

bot=turtle.Turtle()
bot.speed(0)
bot.shape("neutral.gif")
bot.goto(190,20)
bot.stamp()
bot.color("black")
#bot.stamp()
#bot.ht()

#box=turtle.Turtle()
#box.shape("square")
#box.shapesize(5,5,12)
#box.goto(400,10)
#box.speed(0)
cont="YES"
pen=turtle.Turtle()
pen.speed(0)
pen.ht()
#pen.goto(100,100)
pen.color("lightcoral")

while (cont !="NO"):
    wordsAC =turtle.textinput("my name is buzz.","anything up?")

    wordsLC= wordsAC.lower()

    pen.goto(-350,-100)
    pen.color("black")
    pen.write(wordsLC, move=False, align="left", font=("Arial", 32,"normal"))
    pen.color("lightcoral")

    niceThings=["great","pretty","beautiful","good morning","happy","smile","nice","what's","going on"]
    meanThings=["gross","nasty","ugly","bad","awful","hate","die","rude","weird","crazy","whatever","loser"]
    questions=["?"]
    greetings=["hi","hello","good morning","good evening"]
    

    niceness=0
    meanness=0
    isQuestion=False

    tone=""

    for word in niceThings:
        if (word in wordsLC):
            niceness+=1
    for word in meanThings:
        if (word in wordsLC):
            meanness+=1
    for word in questions:
        if (word in wordsLC):
            isQuestion=True
    for word in greetings:
        if (word in wordsLC):
            isGreeting= True

    if (meanness>niceness):
        tone="MEAN"
    elif (niceness>meanness):
        tone="NICE"
    elif (niceness==0 and meanness==0 and isGreeting==True):
        tone="GREETING"
    else:
        tone="NEUTRAL"

    if (isQuestion==False):
        if (tone=="NICE"):
            bot.clear()
            #bot.color("skyblue")
            bot.penup()
            bot.shape("happy.gif")
            bot.pendown()
            wn.update()
            pen.color("lightcoral")
            pen.goto(-350,-150)
            pen.color("black")
            pen.write("thanks :)",move=False, align="left", font=("Arial", 20,"normal"))
        elif (tone=="MEAN"):
            bot.clear()
            bot.shape("sad.gif")
            wn.update()
            pen.color("lightcoral")
            pen.goto(-350,-150)
            pen.color("black")
            pen.write("ouch.",move=False, align="left", font=("Arial", 20,"normal"))
        elif (tone=="NEUTRAL"):
            pen.color("lightcoral")
            pen.goto(-350,-150)
            pen.color("black")
            pen.write("that's cool.",move=False, align="left", font=("Arial", 20,"normal"))
        elif (tone=="GREETING"):
            pen.color("lightcoral")
            pen.goto(-350,-150)
            pen.color("black")
            pen.write("hey.",move=False, align="left", font=("Arial", 20,"normal"))
            
    elif (isQuestion==True):
        if (tone=="NICE"):
            bot.clear()
            #bot.color("skyblue")
            bot.penup()
            bot.shape("turtle")
            bot.pendown()
            wn.update()
            pen.color("lightcoral")
            pen.goto(-350,-150)
            pen.color("black")
            pen.write("thanks :)",move=False, align="left", font=("Arial", 20,"normal"))
        if (tone=="MEAN"):
            bot.clear()
            bot.shape("circle")
            wn.update()
            pen.color("lightcoral")
            pen.goto(-350,-150)
            pen.color("black")
            pen.write("rude.",move=False, align="left", font=("Arial", 20,"normal"))
        if (tone=="NEUTRAL"):
            pen.color("lightcoral")
            pen.goto(-350,-150)
            pen.color("black")
            pen.write("i'm great, thanks :)",move=False, align="left", font=("Arial", 20,"normal"))

    cont=(turtle.textinput("awesome.","anything else? type NO if you're done.")).upper()
    pen.clear()
    
wn.bye()
