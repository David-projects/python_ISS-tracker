import requests
import datetime as dt
import smtplib

NAT = 51.815605
LONG = -0.808400
EMAIL = ""
PASSWORD = ""

params = {
    "nat" : NAT,
    "long" : LONG,
    "formatted" : 0,
}

is_working = True
while is_working:
    # Get sunrise and sunset hour
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    #get now hour
    now_hour = dt.datetime.now()
    now_hour = now_hour.hour

    #get ISS position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_position = (float(data['iss_position']['longitude']), float(data['iss_position']['latitude']))

    nat = 54.815605 - float(NAT)
    long = 1.815605 - float(LONG)

    if (long < 5 and long > -5) and (nat < 5 and nat > -5):
        with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="davidthe@myyahoo.com",
            msg=f"Subject:ISS Over Head\n\nLook Up The ISS is over top"
        )

    is_working = False

