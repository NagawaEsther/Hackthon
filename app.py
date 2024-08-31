from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/ussd", methods = ['POST'])
def ussd():
  # Read the variables sent via POST from our API
  session_id   = request.values.get("sessionId", None)
  serviceCode  = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text         = request.values.get("text", "default")
  symptom = ""
  illness = ['malaria', 'illumina', 'sleeping sickness']


#me
  if text      == '':
      # This is the first request. Note how we start the response with CON
      response  = "CON Welcome to Self MediCaution \n"
      response += "Think before you Dose \n"
      response += "1. what's the problem. please describe \n"
      response += "2. Continue \n"
      symptom = response
      print(text)
      
  elif text.startswith('1* '):
      # Business logic for first level response
      response  = "CON You are likely to be suffering from Malaria \n"
      response += "We recommend you talk to a doctor to get prescription \n"
      response += "1. Contact Nearby doctor / Facility \n"
      print(text)
  elif text    == '1*1':
        # Business logic for first level response
        response  = "CON Enter your location \n"
        response += "To find nearby doctor / Facility \n"
        response += "1. Enter your location"
        print(text)
  elif text    == '1*1*1':
        # Business logic for first level response
        response  = "CON Available doctors /facilities \n"
        response += "1. Dr Morgan, Surgeon / Norvik \n"
        response += "2. Dr. Alex, Medical / Mulago \n"
        response += "3. Dr. Christine, Gyna / KMC"
        print(text)
  elif text    == '1*1*1*1':
            # Business logic for first level response
            response  = "CON Dr. Morgan, Mulago \n"
            response += "1. call  070336373878 \n"
            response += "2. contact on Whatsapp.\n"
            response += "3. email: drmorgan@gmail.com"
            print(text)

  elif text   == '1*1*1*1:1':
      # This is a terminal request. Note how we start the response with END
      print(text)
      response = "END Doctor has been notified. please follow up "


  else :
      response = "END Invalid Selection"

  # Send the response back to the API
  return response

if __name__ == '__main__':
    app.run(debug=True)
