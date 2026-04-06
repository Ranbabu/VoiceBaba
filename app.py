from flask import Flask, request, send_file
from TTS.api import TTS

app = Flask(__name__)

tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

@app.route("/tts", methods=["POST"])
def generate():
    text = request.json.get("text", "")

    tts.tts_to_file(
        text=text,
        file_path="output.wav"
    )

    return send_file("output.wav", mimetype="audio/wav")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
