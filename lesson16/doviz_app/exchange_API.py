from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "50907e5434094925bce8f852"
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":   #POST: formdan veri geldiğinde çalışır
        bozulan = request.form["bozulan"].upper()   # usd -> USD
        alinan = request.form["alinan"].upper()   # try -> TRY
        miktar = float(request.form["miktar"])
        response = requests.get(API_URL + bozulan)
        data = response.json()
        if response.status_code == 200 and alinan in data["conversion_rates"]:
            oran = data["conversion_rates"][alinan]   # USD'nin TRY karşılığı
            sonuc = miktar * oran
            result = {
                "bozulan": bozulan,
                "alınan": alinan,
                "oran": oran,
                "miktar": miktar,
                "sonuc": sonuc
            }
        else:
            result = {"error": "Döviz türü bulunamadı!"}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug = True)