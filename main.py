import random
from flask import Flask

game = Flask(__name__)
RANDOM_NUMBER = random.randint(0, 9)
print(RANDOM_NUMBER)


@game.route("/")
def intro():
    return '<h1 style="text-align: center">Hello, Buddy! Welcome to guess the number!</h1>' \
           '<hr>' \
           "<img src='https://th.bing.com/th/id/R3dbeb9f6ed4608a9175837e076d08418?rik=NMV1D5J8MkGeYA" \
           "&riu=http%3a%2f%2fnrich.maths.org%2fcontent%2f03%2f01%2fpenta5%2fdigit_cards.gif&ehk" \
           "=ZkDeo6NscSv2QBTVeC1Q9%2bNgWX5jTOLLasReaoA88HY%3d&risl=&pid=ImgRaw'" \
           "width=1500px height=200px>" \
           '<br>' \
           "<img src='https://raw.githubusercontent.com/thiagodnf/guess-the-number/master" \
           "/img/logo.png?token=AAG9XwrL" \
           "-t72tifQ-eA47lewNBqqV9Nwks5cDnuJwA%3D%3D' width=850px height=450px>" \



@game.route("/<int:number>")
def start(number):
    if number > RANDOM_NUMBER:
        return "<hr>" \
               "<h1 style='text-align: center'>You're high!</h1>" \
               "<hr>" \
               "<img src='https://media1.giphy.com/media/1jARfPtdz7eE0/giphy.gif?cid" \
               "=ecf05e47ci5pfhnq0ejgzw2efbppauzc4h96set46fowztdw&rid=giphy.gif&ct=g' width=1500px height=600px" \
               "<hr>"

    elif number != RANDOM_NUMBER:
        return "<hr>" \
               "<h1 style='text-align: center'>You're low!</h1>" \
               "<hr>" \
               "<img src='https://media1.giphy.com/media/1jARfPtdz7eE0/giphy.gif?cid" \
               "=ecf05e47ci5pfhnq0ejgzw2efbppauzc4h96set46fowztdw&rid=giphy.gif&ct=g' width=1500px height=600px" \
               "<hr>"
    else:
        return "<hr>" \
               f"<h1 style='text-align: center'>Bravo!</h1>""" \
               "<hr>" \
               "<img src='https://media2.giphy.com/media/3JTrNZgdf4LJGNUN1a/giphy.gif?cid" \
               "=ecf05e47ay0xzsihp50w770r73ieq7015fo6pozzgcosu5vz&rid=giphy.gif&ct=g' width=1500px height=600px>" \
               "<hr>"


if __name__ == "main.py":
    game.run(debug=True)
