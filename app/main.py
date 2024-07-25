from bottle import Bottle, run, template

app = Bottle()

@app.route('/')
def welcome():
    return template('<b>欢迎来到我的简单Bottle应用！</b>')

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080)
