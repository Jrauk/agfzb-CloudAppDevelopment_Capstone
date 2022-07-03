import requests
import json
# import related models here
from requests.auth import HTTPBasicAuth
from . import models
from .models import CarDealer, DealerReview
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from cloudant import cloudant
from cloudant import cloudant_iam

API_KEY=hg0CGsW3PZwq8gAwUTnASwbJr3cNRcAnprqj4Prh-Xmy
ACCOUNT_NAME=0abbfc03-f8e0-4ba3-b426-67e37d20cb14-bluemix
url=https://0abbfc03-f8e0-4ba3-b426-67e37d20cb14-bluemix.cloudantnosqldb.appdomain.cloud

with cloudant_iam(ACCOUNT_NAME, API_KEY) as client:

# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        if "api_key" in kwargs:
            params=dict()
            params["text"]=kwargs["text"]
            params["version"]=kwargs["version"]
            params["features"]=kwargs["features"]
            params["return_analyzed_text"]=kwargs["return_analyzed_text"]

            print("params: ",params)

            response = requests.get(url,params=params,headers={'Content-Type': 'application/json'},
                auth=HTTPBasicAuth('apikey',kwargs["api_key"]))

            print("Response_apikey_Provided: ",response)

        else:
            print("No api_key passed to get request.")
        # Call get method of requests library with URL and parameters
            response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
def post_request(url, payload, **kwargs):
    print("Payload: ",payload)
    print("Kwargs: ",kwargs)
    print("POST to {}".format(url))
    try:
        response=requests.post(url,params=kwargs,json=payload)
        print(response)
    except:
        print("Post Network Exception Occured")

    status_code = response.status_code
    print("With status {}".format(status_code))
    json_data=json.loads(response.text)
    print("json_data: ",json_data)
    
    return json_data

# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["body"]["rows"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], state=dealer_doc["state"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



