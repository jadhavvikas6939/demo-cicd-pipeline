import json
from datetime import datetime

def lambda_handler(event, context):
    response = {
        "message": "AWS CI/CD Pipeline deployed using GitHub → CodePipeline → Lambda!",
        "event_received": event,
        "runtime": "Python",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(response)
    }
