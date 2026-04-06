from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import edge_tts
import asyncio
import os
from deep_translator import GoogleTranslator

app = Flask(__name__)
CORS(app)

async def generate_audio(text, output_file, voice):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)

@app.route("/tts", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        hindi_text = data.get("text", "नमस्ते भाई, मैं आपकी एआई आवाज़ हूँ।")
        selected_voice = data.get("voice", "ur-PK-AsadNeural") 
        
        # अगर आवाज़ उर्दू (ur) की है, तो हिंदी को उर्दू में ट्रांसलेट करें
        if "ur-" in selected_voice:
            text_to_speak = GoogleTranslator(source='hi', target='ur').translate(hindi_text)
        else:
            text_to_speak = hindi_text
            
        output_path = "output.mp3"
        
        asyncio.run(generate_audio(text_to_speak, output_path, selected_voice))

        return send_file(output_path, mimetype="audio/mpeg")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# यह रूट सीधा आपकी index.html वेबसाइट को दिखाएगा
@app.route("/", methods=["GET"])
def home():
    return send_file("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
