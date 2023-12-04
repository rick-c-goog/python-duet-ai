# python-duet-ai
Creae a new project
## OpenAPI specs
Chat bot: 
You are backend developer to write API services. Please write Open API 3.0  specs for the stockquotes service, have 2 methods, getQuote with input parameter stockName return a stock object, the 2nd method getQuotes with input parameter a list of stockName to return a list of stock objects, for both method stock object have properties including  stockName, currentPrice, changePercent, bidPrice, askPrice, volume

Save the results to api-spec.yaml

Validate the api specs from the following:

https://editor-next.swagger.io/


## implement API service
Based on the OpenAPI spec, implement the API service with python FastAPI libray

replace the logic to get stock properties from the database, insted using the yahoo finance service to get the properties

Save the results to app.py

## Build and deploy

list all the required modules need to install for this python implmentation

save results to requirements.txt

write a Dockerfile , use python3.10 base image, install the required pip modules, add the app.py code based on service API implementation, expose port 8080
Save results to Dockerfile

Or:


write a cloud build file, step 1, build the stockquote service, step 2, deploy the stock service to new cloud Run service, output the cloud run service url when it completes
Save results to cloudbuild.yaml

provide the gcloud command to submit the cloud build job

## Other prompts
