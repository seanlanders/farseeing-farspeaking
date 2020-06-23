from flask import Flask, request
from twilio.twiml.voice_response import Play, VoiceResponse, Gather
import socket
import time

app = Flask(__name__)
port = 10001


@app.route("/", methods=['GET', 'POST'])
def answer():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", port))
    message = ("attract").encode()
    s.sendall(message)
    s.close()

    if 'Digits' in request.values:
        choice = request.values['Digits']
        if choice == '1':
            resp.redirect("/shoulder")
            return str(resp)
        elif choice =='2':
            resp.redirect("/eyes")
            return str(resp)
        elif choice == '3':
            resp.redirect("/fantasy")
            return str(resp)
        else:
            resp.say("Sorry, I didn't catch that.")

    # Read a message aloud to the caller
    gather = Gather(num_digits=1)
    gather.say("If you need a shoulder to lean on, press one.  If you need to feel seen, press two.", voice='alice')
    resp.append(gather)
    """
    resp.say("If you need to feel seen, press two.", voice='alice')
    resp.say("If you'd like to leave a message, press three.", voice='alice')
    resp.say("To speak to an operator, press zero or stay on the line.", voice='alice')
    """
#    resp.redirect('/operator')
    resp.redirect('/')

    return str(resp)
@app.route("/gather", methods=['GET', 'POST'])
def gather():
    resp = VoiceResponse()
    if 'Digits' in request.values:
        choice = request.values['Digits']
        if choice == '1':
            resp.redirect("/shoulder")
            return str(resp)
        elif choice =='2':
            resp.redirect("/eyes")
            return str(resp)
        elif choice == '3':
            resp.redirect('/fantasy')
            return str(resp)
        else:
            resp.redirect("/")
            return str(resp)

@app.route("/shoulder", methods=['GET','POST'])
def myshoulder():
    resp = VoiceResponse()
    resp.play('https://olive-wren-8959.twil.io/assets/donttalk.mp3', loop=10)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", port))
    message = ("shoulder").encode()
    s.sendall(message)
    s.close()
    print(resp)
    resp.redirect("/")
    return str(resp)

@app.route("/eyes", methods=['GET','POST'])
def eyes():
    resp = VoiceResponse()
    resp.play('https://olive-wren-8959.twil.io/assets/onlyhaveeyes.mp3', loop=10)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", port))
    message = ("eyes").encode()
    s.sendall(message)
    s.close()
    print(resp)
    resp.redirect("/")
    return str(resp)

@app.route("/fantasy", methods=['GET','POST'])
def fantasy():
    resp = VoiceResponse()
    resp.play('https://olive-wren-8959.twil.io/assets/CR-2006-04_512kb.mp3', loop=10)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", port))
    message = ("fantasy").encode()
    s.sendall(message)
    s.close()
    print(resp)
    resp.redirect("/")
    return str(resp)


if __name__ == "__main__":
    app.run(port=5025, debug=True)
