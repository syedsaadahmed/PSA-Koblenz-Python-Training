from app import app


@app.route('/')
def helloworld():
    return 'hello world'
