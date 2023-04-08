from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    print("RECEIVING....")
    print(request.data)
    data = request.data.decode('utf-8')
    print(data)
    return 'Data received successfully!\n'

if __name__ == '__main__':
    app.run()
