import os
import json
import boto3
import copy
from datetime import datetime
from dateutil.parser import parse

boto3.setup_default_session(profile_name='rdpdp')

adx = boto3.client('dataexchange', region_name='us-east-1')
marketplace = boto3.client(service_name='marketplace-catalog', region_name='us-east-1')

# Get all of our Marketplace Products
adx_products = []
response = marketplace.list_entities(Catalog='AWSMarketplace', EntityType="DataProduct")
adx_products += response['EntitySummaryList']
while 'NextToken' in response:
  response = marketplace.list_entities(Catalog='AWSMarketplace', EntityType="DataProduct",NextToken = response['NextToken'])
  adx_products += response['EntitySummaryList']
 
 
# For every ADX Product extend info (from describe_entity)
 
for product in adx_products:
  response = marketplace.describe_entity(Catalog='AWSMarketplace',EntityId=product['EntityId'])
  details = json.loads(response['Details'])
  product['Details'] = details

print(adx_products)

#   # Get all of our DataSets
# datasets = []
# response = adx.list_data_sets(
#     MaxResults=200,
#     Origin='OWNED',
# )
# print(len(response['DataSets']))
# datasets += response['DataSets']
# while 'NextToken' in response:
#   response = adx.list_data_sets(
#     MaxResults=200,
#     Origin='OWNED',
#     NextToken = response['NextToken']
#   )
#   print(len(response['DataSets']))
#   datasets += response['DataSets']

#   datasets[0]
