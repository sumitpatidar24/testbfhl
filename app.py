from flask import Flask, render_template, request


app = Flask(__name__)
ans = {
        "is_success": True,
        "user_id": "sumit_patidar_24082000",
        "odd": [],
        "even": []
    }

@app.route("/bfhl")
def home():
    return render_template("index.html")

@app.route("/response", methods=['POST'])
def res():
    numbers = request.form.get("numbers")
    lst = []
    is_success = True
    for i in numbers.split(" "):
        try:
            lst.append(int(i))
            if(int(i)%2==0):
                ans["even"].append(int(i))
            else:
                ans["odd"].append(int(i))
        except:
            is_success = False
            ans["is_success"] = False
            lst.append(i)
    # print(ans)
    return str(ans)    

app.run()



