import urllib.request
import json      

body = { 
  "api_key": "143d1680acbecad3c3abf74b3dbfacc2", 
  "model_text_id": 3586, 
  "model_type_id": 1, 
  "category_id": 63, 
  "subject_id": 63, 
  "description_id": 166, 
  "model_name": "Automobile recall liability for used car dealers", 
  "source_link": "atae.nada.org", 
  "model_legislation_source": "Automobile Trade Association Executives", 
  "model_legislation_text": "A dealer that sells a used motor vehicle at retail that is subject to a recall pursuant to 49 U.S.C. 30111 and remains unremedied at the time of the sale shall provide to the buyer a written disclosure of the recall. If, at the time of sale, there is a remedy available for such used motor vehicle, the dealer shall disclosure to the buyer that there is a remedy for the recall and the buyer must return to have the dealer provide the remedy. If, at the time of sale, there is no remedy available for such used motor vehicle, the dealer shall disclose to the buyer that there is no remedy for the recall and the buyer must return to have the dealer provide the remedy when the buyer learns or has notice that the remedy is available, if the dealer holds a franchise to sell as new and to service the line-make of such used motor vehicle or there is no remedy for the recall and the buyer must contact a dealer of the line-make to provide the remedy when the buyer learns or has notice that the remedy is available." 
}   

myurl = "https://statehouses-api.gannettdigital.com/api/v1.0/UpdateModelText"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print (jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)
