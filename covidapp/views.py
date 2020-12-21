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
    mylist = []
    numofresults = (response['results'])
    for x in range (0, numofresults):
        mylist.append(response['response'][x]['country'])
    if request.method == "POST":
        selectedcountry = request.POST['selectedcountry']
        print(selectedcountry)
        numofresults = (response['results'])
        for x in range(0,numofresults):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                death = int(total) - int(active) - int(recovered)
        context = {'selectedcountry': selectedcountry, 'mylist': mylist,'new': new, 'active': active, 'critical': critical, 'recovered': recovered, 'total': total, 'death': death}
        return render(request, 'helloworld.html', context)
    
    context = {'mylist' : mylist}
    return render(request, 'helloworld.html', context)