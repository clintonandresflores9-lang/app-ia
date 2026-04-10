from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# 🔑 PON TU API KEY AQUÍ
client = OpenAI(api_key="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")

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