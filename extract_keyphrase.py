# Simple program that demonstrates how to invoke Azure ML Text Analytics API: key phrases, language and sentiment detection.
import urllib2
#import urllib
import sys
import base64
import json


def extract_key_phrases(text):
    # Azure portal URL.
    base_url = 'https://westus.api.cognitive.microsoft.com/'
    # Your account key goes here.
    #account_key = '867c7175a7ab4880b4cb82f292aed58a'
    account_key = '782ced9a9e5c42968297cfd84596bef1'

    #headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}
    headers = {'Content-Type':'text/json', 'Ocp-Apim-Subscription-Key':account_key}
    sample_body = "For months, the four scientific instruments at the heart of the James Webb Space Telescope have been sealed in what looks like a huge pressure cooker. "
    json_text_field =  text['text']
    print(json_text_field)
    input_text_json = {
      "documents":[
        {
          "id":"1",
          "text":str(json_text_field)
        }
      ]
    }

    num_detect_langs = 1;

    # Detect key phrases.
    batch_keyphrase_url = base_url + 'text/analytics/v2.0/keyPhrases'
    req = urllib2.Request(batch_keyphrase_url, str(input_text_json), headers)
    response = urllib2.urlopen(req)
    result = response.read()
    obj = json.loads(result)
    for keyphrase_analysis in obj['documents']:
        print('Key phrases ' + str(keyphrase_analysis['id']) + ': ' + ', '.join(map(str,keyphrase_analysis['keyPhrases'])))

    return obj

def lambda_handler(event, context):

    return(extract_key_phrases(event))
