from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "3669e80dafmshf0fe5272ec00724p116f42jsn1ed1c524f436",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def helloworldview(request):
    if request.method == "POST":
        selectedcountry = request.POST['selectedcountry']
        print(selectedcountry)
    mylist = []
    numofresults = (response['results'])
    for x in range (0, numofresults):
        mylist.append(response['response'][x]['country'])
    context = {'mylist' : mylist}
    return render(request, 'helloworld.html', context)