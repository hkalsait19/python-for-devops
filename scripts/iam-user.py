import boto3

# Initialize the IAM client
iam_client = boto3.client('iam')

# # List IAM users
# def list_iam_users():
#     try:
#         response = iam_client.list_users()
#         print("IAM Users:")
#         for user in response['Users']:
#             print(f"User Name: {user['UserName']}")
#             print(f"User ID: {user['UserId']}")
#             print(f"ARN: {user['Arn']}")
#             print(f"Creation Date: {user['CreateDate']}")
#             print("-" * 40)
#     except Exception as e:
#         print(f"Error listing IAM users: {e}")

# # Call the function
# list_iam_users()
