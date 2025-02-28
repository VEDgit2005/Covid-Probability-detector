from flask import Flask, render_template, request #for creating webserver
app = Flask(__name__) #initalising webserver
import pickle #for taking python value from dump file


file = open('model.pkl', 'rb') #opening the python dump file
clf = pickle.load(file) #taking the value from the dump file
file.close #closing dump file
@app.route('/', methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        myDict = request.form #requesting data from html form
        fever = int(myDict['fever']) #taking fever parameter from form
        age = int(myDict['age'])#taking age parameter from form
        diffBreath = int(myDict['diffBreath'])#taking diffbreath parameter from form
        bodyPain = int(myDict['bodyPain'])#taking bodypain parameter from form
        runnyNose = int(myDict['runnyNose'])#taking runnynose parameter from form
        inputFeatures = [fever, bodyPain, age, runnyNose, diffBreath] #putting all parameters into array
        infProb = clf.predict_proba([inputFeatures])[0][1]#predicting probability using inbuilt function "predictproba"
        print(infProb)#printing probability on cosole
        return render_template('show.html', inf=round(infProb*100))#returning probability to html file
    return render_template('index.html')#loading index.html with input values

if __name__ == "__main__":
    app.run(debug=True)#running the webapp
