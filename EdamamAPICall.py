from flask import Flask, render_template, request
import urllib.request
import json

a = Flask(__name__, template_folder="template")
count = -1

@a.route("/")
def default():
    return render_template("search.html")

@a.route('/rendering', methods=['POST'])
def rendering():
    item = request.form["item"]
    n2 = calculate_cals_and_macros(item)
    return render_template("cals.html", n2 = n2)
@a.route('/adding', methods = ['POST'])
def adding():
    return render_template("log.html")



def http_get_request(url):
    try:
        info = ""
        url_c = urllib.request.urlopen(url)
        is_ = url_c.read()
        for i in is_.decode("utf-8").splitlines():
            info += i
        url_c.close()
        return info
    except Exception as e:
        print(e)
        return None
    
def calculate_cals_and_macros(food):
    count = 0
    if " " in food:
        for i in food.split():
            if count == 0:
                food = ""
            food += i + "%20"
            count += 1

    fullUrl = http_get_request("https://api.edamam.com/api/food-database/v2/parser?app_id=5498a2c9&app_key=362069b323765afa0e069f3a152c101b&ingr=" + food)
    jsonO = json.loads(fullUrl)
    name = jsonO["hints"][1]["food"]["knownAs"]
    cals = jsonO["hints"][1]["food"]["nutrients"]["ENERC_KCAL"]
    protein = jsonO["hints"][1]["food"]["nutrients"]["PROCNT"]
    fat = jsonO["hints"][1]["food"]["nutrients"]["FAT"]
    carbs = jsonO["hints"][1]["food"]["nutrients"]["CHOCDF"]
    nutrition = [name, cals, protein, fat, carbs]
    return nutrition

    
#search = input("Watchu wanna search? --> ")
#n = calculate_cals_and_macros(search)
#print("The food you have searched up is " + n[0] + ". One serving of " + n[0] + " contains " + str(n[1]) + " calories, " + str(n[2]) + " grams of protein, " + str(n[3]) + " grams of fat, and " + str(n[4]) + " grams of carbohydrates")
if __name__ == "__main__":
    a.run(port=8000)
