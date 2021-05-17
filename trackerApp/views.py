from django.shortcuts import render
# api
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "034b221fffmsh39292572dfd8cbbp132e7djsnec92757dc7aa",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()

# Create your views here.


def helloworldview(request):
    results = int(response['results'])
    countries = []
    for x in range(results):
        countries.append(response['response'][x]['country'])

    if (request.method == 'POST'):
        selectedcountry = request.POST['selectedcountry']
        print(selectedcountry)
        for x in range(results):
            if (selectedcountry == response['response'][x]['country']):
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
                print(deaths)
        post_context = {
            'list': countries,
            'country': selectedcountry,
            'new': new,
            'active': active,
            'critical': critical,
            'recovered': recovered,
            'total': total,
            'deaths': deaths
        }
        return render(request, 'helloworld.html', post_context)

    context = {
        'list': countries,

    }
    return render(request, 'helloworld.html', context)
