import json
def lambda_handler(event, context):
	body = "Hello from Lambda"
	statusCode = 200
	return {
	"statusCode": statusCode,
	"body": json.dumps(),
	"headers": {
	"Content-Type": "application/json"
	}
	}

	