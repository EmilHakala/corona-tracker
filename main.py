import web
import requests
import json
from web import form

render = web.template.render('templates/')
urls = (
    '/', 'index'
)

c_code = "DE"



r = requests.get("https://disease.sh/v3/covid-19/countries/" + c_code)

print(r.status_code)

dat = r.text
json = json.loads(dat)

country = str(json["country"])
deaths = str(json["deaths"])
tdeaths = str(json["todayDeaths"])
cases = str(json["cases"])
tcases = str(json["todayCases"])
recovered = str(json["recovered"])
trecovered = str(json["todayRecovered"])



class index:
    def GET(self):
        return render.index(country, deaths, tdeaths, cases, tcases, recovered, trecovered)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
