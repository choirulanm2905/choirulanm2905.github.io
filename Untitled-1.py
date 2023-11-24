from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
     return render_template('Home.html', username='templates')

@app.route('/projects')
def projects():
    # Logika untuk menampilkan halaman proyek
    return render_template('Projects.html')

@app.route('/certificate')
def certificate():
    # Logika untuk menampilkan halaman proyek
    return render_template('Certificate.html')

@app.route('/skill')
def skill():
    # Logika untuk menampilkan halaman proyek
    return render_template('Skill.html')

if __name__ == '__main__':
    app.run(debug=True)
