import os
import boto3

TABLE_NAME = os.getenv('CAR_DATA_TABLE_NAME')

def save_data_to_dynamo_db(partion_key: str, sort_key: str, generations: str) -> None:
    dynamodb = boto3.client('dynamodb')
    item = {
        'make': {
            'S': partion_key
        },
        'model': {
            'S': sort_key
        },
        'generations': {
            'S': generations
        }
    }

    dynamodb.put_item(TableName=TABLE_NAME, Item=item)