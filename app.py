from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Variabel untuk menyimpan status permainan
status_game = {
    "pemenang": None,
    "terkunci": False
}

# 1. Halaman Utama untuk Juri (Admin)
@app.route('/')
def juri_dashboard():
    return render_template('juri.html')

# 2. Halaman khusus Peserta A
@app.route('/peserta/a')
def peserta_a():
    return render_template('peserta.html', tim="Tim A", warna="#ff4757")

# 3. Halaman khusus Peserta B
@app.route('/peserta/b')
def peserta_b():
    return render_template('peserta.html', tim="Tim B", warna="#2ed573")

# 4. Halaman khusus Peserta C
@app.route('/peserta/c')
def peserta_c():
    return render_template('peserta.html', tim="Tim C", warna="#1e90ff")

# Route saat peserta menekan bel dari perangkat mereka
@app.route('/tekan/<tim>', methods=['POST'])
def tekan_bel(tim):
    global status_game
    if not status_game["terkunci"]:
        status_game["pemenang"] = tim
        status_game["terkunci"] = True
        return jsonify({"status": "sukses", "pemenang": tim})
    return jsonify({"status": "ditolak", "pemenang": status_game["pemenang"]})

# Route untuk Juri mereset bel
@app.route('/reset', methods=['POST'])
def reset_bel():
    global status_game
    status_game["pemenang"] = None
    status_game["terkunci"] = False
    return jsonify({"status": "reset"})

# Route untuk mengecek status secara real-time
@app.route('/status', methods=['GET'])
def cek_status():
    return jsonify(status_game)

if __name__ == '__main__':
    app.run(debug=True)