import json
from config import base_url
    import requets

def lambda_handler(event, context):
    
    requests.get(url=base_url+'todos/1')
    return {
        'statusCode': res.status_,
        'body': res.json()
    }
