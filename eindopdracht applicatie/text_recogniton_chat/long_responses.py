import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_NAME = "My name is bot_390782 but you can call my princeps"
R_LANGUAGE = "What code languages do you know?"
R_SAD = "Oh no, well I got a link that might cheer you up! https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"
                "I dont have the knowledge to reply to that."][
        random.randrange(5)]
    return response
