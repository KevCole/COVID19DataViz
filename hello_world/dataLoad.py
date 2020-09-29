import boto3
from app import combined
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Covid19Table')

def add_covid_data(event, context):
    for row in combined.iterrows():
        Date = row[1]['Date']
        Cases = row[1]['cases']
        Deaths = row[1]['deaths']
        Recovered = row[1]['Recovered']
        table.put_item( Item={
            'Date': str(Date),
            'Cases': int(Cases),
            'Deaths': int(Deaths),
            'Recovered': int(Recovered)
        })
    print('Put succeeded:')


