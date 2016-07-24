import pafy
import os
from flask import Flask, request

app = Flask(__name__)
os.chdir('/Users/Harrison/Desktop/Music')


@app.route('/')
def index():
    return """<form action=\"/getsong\" method=\"post\">Enter YouTube Link:<br><input type=\"text\" name=\"song\"><br>

        <p><input type=\"submit\" value=\"Submit\"></p></form>
        """


@app.route('/getsong', methods = ['POST'])
def getSong():

    song = request.form['song']

    return download(song)

def download(song):

    output = []
    target = pafy.new(song)
    bestTarget = target.getbest()
    filename = bestTarget.download()
    output.append(bestTarget.title + " downloaded to: " + os.getcwd())

    return str(output)


def main():
    song = input("Enter the youtube link of the song you'd like to download: ")
    download(song)


if __name__ == '__main__':
    app.run(debug = True)
