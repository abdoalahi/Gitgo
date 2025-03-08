from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="الصفحة الرئيسية")

@app.route('/about')
def about():
    return render_template('index.html', title="من نحن")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
