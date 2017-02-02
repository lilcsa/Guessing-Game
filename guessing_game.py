secret = 32
guess = int(raw_input("Which number is in my head? : "))
if guess == secret:
    print "Congrats! How did you know?"
else:
    print "Sorry, you guessed wrong! :( "
