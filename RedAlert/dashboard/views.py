from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Import the client model from redAlertSite app.
from redAlertSite.models import Client
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
import string
import datetime

# Create your views here.
# Do not show the dashboard if the user isnt logged in!
# login_url is the urls to redirect a user to if they are not logged in!
@login_required( login_url='/' )
def show_dashboard( request ):

    #delete_all_clients()
    #create_client_list()

    #client_json = json.dumps( [{"msg": "yo", "amsg": "hello"}, {"msg": "val", "amsg": "hello"}] )

    all_clients_array = Client.objects.all()

    json_array = []
    for client in all_clients_array:
        a_client_dict = {}
        a_client_dict["id"] = client.id
        a_client_dict["name"] = client.name
        a_client_dict["unit_num"] = client.unit_num
        a_client_dict["street"] = client.street
        a_client_dict["city"] = client.city
        a_client_dict["zip_code"] = client.zip_code
        a_client_dict["state"] = client.state
        a_client_dict["license_num"] = client.license_num
        a_client_dict["policies"] = client.policies
        a_client_dict["age"] = client.age
        a_client_dict["birthdate"] = str(client.birthdate)
        a_client_dict["gender"] = client.gender
        a_client_dict["notification_status"] = client.notification_status
        a_client_dict["email"] = client.email
        a_client_dict["phone"] = client.phone
        a_client_dict["lat"] = client.lat
        a_client_dict["long"] = client.long


        json_array.append( a_client_dict )

    #print( len( json_array ) )
    #print( str(json_array) )


    client_json = json.dumps( json_array )

    response = {
        'client_json' : client_json
    }

    return render(request, 'dashboard/dashboard.html', response)


def create_client_list():

    names =["Zane Roman",
    "Mya Fry",
    "Kailyn Carney",
    "Cael Mcbride",
    "Derick Delgado",
    "Monserrat Vargas",
    "Rowan Buckley",
    "Magdalena Calderon",
    "Kameron Morgan",
    "Jasmine Glover",
    "Noel Thompson",
    "Kenny Quinn",
    "Jovanny Carrillo",
    "Miracle Patterson",
    "Fanni Azzurra",
    "Britt Peta",
    "Neema Marian",
    "Magomed Aldegar",
    "Cirino Tayla",
    "Nkechi Priya",
    "Nayden Urszula",
    "Alkmene Phokas",
    "Berrak Mauro"]

    #unit_num, street, City, State, Zip Code
    addresses = ["3908,E Bronco Trl,Phoenix,Arizona,85044 ".split(','),
     "11221,S 51st St,Phoenix,Arizona,85044".split(','),
     "4234,E Jicarilla St,Phoenix,Arizona(AZ),85044".split(','),
     "1055,W Baseline Rd,Phoenix,Arizona,85041".split(','),
     "2050,W Dunlap Ave,Phoenix,Arizona,85021".split(','),
     "4730,N 19th Ave,Phoenix,Arizona,85015".split(','),
     "2939,W Lamar Rd,Phoenix,Arizona,85017".split(','),
     "5201,N 8th Pl,Phoenix,Arizona,85014".split(','),
     "938,W Glenrosa Ave,Phoenix,Arizona,85013".split(','),
     "8829,S 51st St,Phoenix,Arizona,85044".split(','),
     "919,E Aire Libre Ave,Phoenix,Arizona,85022".split(','),
     "830,E Lawrence Rd,Phoenix,Arizona,85014".split(','),
     "8628,W Pima St,Phoenix,Arizona,85003".split(','),
     "723,E Roosevelt St,Phoenix,Arizona,85006".split(','),
     "901,S Country Club Dr,Mesa,Arizona,85210".split(','),
     "9233,E Neville Ave,Mesa,Arizona,85208".split(','),
     "9804,E Knowles Ave,Mesa,Arizona,85208".split(','),
     "3390,E Lockett Rd,Flagstaff,Arizona,86004".split(','),
     "3300,S Gila Dr,Flagstaff,Arizona,86001".split(','),
     "1830,S Milton Rd,Flagstaff,Arizona,86001".split(','),
     "8961,E Meadow Hill Dr,Scottsdale,Arizona,85260".split(','),
     "9494,E Redfield Rd,Scottsdale,Arizona,85260".split(','),
     "9848,E Thomas Rd,Scottsdale,Arizona,85256".split(',') ]

    # These correspond to the addresses above.
    longLat = [
        # Order is lat, long contrary to the name lol
        [33.3409064444445,	-111.998838666667],
        [33.3451534769561,	-111.974255629502],
        [33.348566684932,	-111.992154585402],
        [33.3776073884457,	-112.086657159916],
        [33.56969965,	-112.103388108672],
        [33.5061482222222,	-112.099985833333],
        [33.5361629115168,	-112.123175020013],
        [33.512979,	-112.06271],
        [33.4985806510067,	-112.085733496644],
        [33.3649547680338,	-111.971815911598],
        [33.63604865,	-112.061387013499],
        [33.5356290909091,	-112.062408121212],
        [33.4330644,	-112.1008284],
        [33.4586047664523,	-112.064775064221],
        [33.398806,	-111.839312],
        [33.36724975,	-111.6336074689],
        [33.3784966969697,	-111.623984090909],
        [35.21868855,	-111.597247788542],
        [35.1666589,	-111.658973392651],
        [35.1815828,	-111.65844995],
        [33.6137616,	-111.8453885],
        [33.615277,	-111.876497411765],
        [33.4803402,	-111.9094363],
     ]

    policies = ['fire auto', 'fire', 'fire boat home', 'home', 'auto fire home', 'auto', 'boat home', 'home fire boat', 'pet home fire', 'pet', 'pet fire','boat fire', 'boat']
    gender = ["M","F"]
    notification_status =['all','emergency','none']
    emails = ["@gmail.com", "@nau.edu", "@cox.com", "@yahoo.com"]



    for index in range( len(addresses) ):
        a_client = Client()
        a_client.name = names[index]
        a_client.unit_num = addresses[index][0]
        a_client.street = addresses[index][1]
        a_client.city = addresses[index][2]
        a_client.state = addresses[index][3]
        a_client.zip_code = addresses[index][4]
        a_client.license_num = random.choice(string.ascii_uppercase ) + str(random.randint(10000000,99999999))
        a_client.policies = policies[random.randint(0, len(policies) - 1 )]
        # YYYY-MM-DD
        a_client.birthdate = datetime.date(random.randint(1920, 2005),random.randint(1, 12), random.randint(1, 28) )
        a_client.age = 2022 - a_client.birthdate.year
        a_client.gender = gender[ random.randint(0,1)]
        a_client.notification_status = notification_status[random.randint(0, len(notification_status) - 1)]
        a_client.email = a_client.name.split(' ')[0] + emails[random.randint(0, len(emails) - 1 )]
        a_client.phone = "4803690030"
        a_client.lat = longLat[index][0]
        a_client.long = longLat[index][1]
        a_client.save()

    print("LENG OF CLIENTS COLLECTION IS: {}".format( len( Client.objects.all()) ) )


def delete_all_clients():
    client_list = Client.objects.all()

    for client in client_list:
        client.delete()










# EXAMPLE AJAX REQUEST RESPONSE METHOD.
# @csrf_exempt
def execute_search( request ):
    print("IN EXECUTE SEARCH")
    if request.is_ajax():
        print("IN EXECUTE SEARCH AJAX SECTION")
        # GEt the users query from the ajax request params
        user_query = request.POST.get('user_query', None)

        response_str = "The users query was {}".format( user_query )

        response = [
            {'msg': response_str, 'amsg': "hello"},
            {'obj2': "val", "objTwo": "hello"}
                   ]

        return JsonResponse(response) # return response as JSON

# email sending method
def send_email( request ):
    if request.method == "POST":
        subject = request.POST['email-subject']
        message = request.POST['email-message']
        # The recipient must be a tuple or list.
        recipients = (request.POST['recipient-email'], )

        for recipientIndex in recipients:
            send_mail(subject, message, "RedAlertTester@gmail.com", recipientIndex)

        return render(request, 'redAlertSite/send_email.html')

    else:
        return render(request, 'redAlertSite/send_email.html')

# SMS sending method
def send_sms_message( request ):
    if request.method =="POST":
        message = request.POST['sms-message']
        sender = '+19087749012'
        recipients = [request.POST['recipient-phone']]

        for recipientIndex in recipients:
            send_sms( message, sender, recipientIndex, fail_silently=False )

        return render(request, 'redAlertSite/send_email.html')

    else:
        return render(request, 'redAlertSite/send_email.html')
