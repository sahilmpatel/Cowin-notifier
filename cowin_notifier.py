import requests
import time
from datetime import datetime, timedelta
import json

print("Starting search for vaccine slots .......")

age = 18
pinCodes = ["382421"]
print_flag = 'Y'
num_days = 2

actual = datetime.today()
# print(actual)

list_format = [actual + timedelta(days=i) for i in range(num_days)]
# print(list_format)

actual_dates = [i.strftime("%d%m%y") for i in list_format]
# print(actual_dates)

while True:
    counter = 0

    for pinCode in pinCodes:
        for given_date in actual_dates:

            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pinCode,given_date)

            header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
            result = requests.get(URL,headers = header)

            # print(result.text)

            if result.ok:
                response_json = result.json()

                flag = False

                if response_json['centers']:
                    if print_flag.lower() == 'y':
                        for center in response_json['centers']:
                            # print(center)
                            for session in center['sessions']:
                                if (session['min_age_limit'] <= age and session['available_capacity'] > 0):
                                    print('Pincode: '+ pinCode)
                                    print("Available on: {}".format(given_date))
                                    print("\t", center["name"])
                                    print("\t", center["block_name"])
                                    print("\t Price: ",center["fee_type"])
                                    print("\t Availablity : ",session["available_capacity"])

                                    if (session["vaccine"] != ''):
                                        print("\t Vaccine type: ",session["vaccine"])
                                    print("\n")

                                    counter += 1
                                else:
                                    pass
                    else:
                        pass
            else:
                print('No response received..')

        if counter == 0:
            print(' No Vaccination slot is available ')
        else:
            print('Finished Search!')

        dt = datetime.now() + timedelta(minutes=2)

        while datetime.now() < dt:
            time.sleep(1)




