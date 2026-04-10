from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

# 🔑 API KEY SEGURA (NO en el código)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/ia", methods=["POST"])
def generar_ia():
    try:
        data = request.json
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"respuesta": "Escribe algo primero"})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un experto en ideas de negocio."},
                {"role": "user", "content": f"Dame una idea sobre: {prompt}"}
            ]
        )

        texto = response.choices[0].message.content

        return jsonify({"respuesta": texto})

    except Exception as e:
        return jsonify({"respuesta": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
