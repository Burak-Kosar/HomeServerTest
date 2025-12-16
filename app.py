from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # Sunucunun adini (hostname) alalim ki hangi makinede oldugumuzu gorelim
    hostname = socket.gethostname()
    return f"""
    <h1>Tebrikler Burak! 🚀</h1>
    <p>Bu sayfa senin evdeki sunucundan (<b>{hostname}</b>) sunuluyor.</p>
    <p>CI/CD Boru hatti basariyla calisti!</p>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)