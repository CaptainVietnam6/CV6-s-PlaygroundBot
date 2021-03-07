#code to connect uptimerobot.com to this repl to keep it online
from flask import Flask
from threading import Thread

app = Flask("")

@app.route("/")
def home():
    return "CV6's PlaygroundBot is online on webserver"

def run():
    app.run(host = "0.0.0.0", port = 8080)

def keep_alive():
    t = Thread(target = run)
    t.start()
