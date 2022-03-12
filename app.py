from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect('index.html')

        file = request.files["file"]    
        if file.filename == "":
            return redirect('index.html')
        
        if file:
            r = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = r.record(source)
            transcript = r.recognize_google(data, key=None)
    
    return render_template('index.html', transcript=transcript)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)