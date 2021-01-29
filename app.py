from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('first_page.html')

@app.route('/quiz_me')
def testquiz() :
    return render_template('quiz_me.html')
@app.route('/quiz_parents')
def testquiz2() :
    return render_template('quiz_parents.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
