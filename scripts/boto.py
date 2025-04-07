import boto3

bucket_name = "my-boto3bucket-using-python1"

my_boto3_bucket_client = boto3.client('s3')


# # Create the bucket # #

# response = my_boto3_bucket_client.create_bucket( ## create_bucket & delete_bucket & list_buckets
#     Bucket = "my-boto3bucket-using-python1"
# )
# print(f"Bucket '{bucket_name}' created successfully.")


# # Delete the bucket # #
# response = my_boto3_bucket_client.delete_bucket( ## create_bucket & delete_bucket & list_buckets
#     Bucket = "my-boto3bucket-using-python1"
# )
# print(f"Bucket '{bucket_name}' deleted successfully.")

# try:
#     my_boto3_bucket_client.delete_bucket(Bucket=bucket_name)
#     print(f"Bucket '{bucket_name}' deleted successfully.")
# except Exception as e:
#     print(f"Error deleting bucket: {e}")


##### same name bucket will create here after deleting the bucket also


# # List the bucket(s) # #

# response = my_boto3_bucket_client.list_buckets() ##get_bucket_acl()
# print("List of buckets:",response)


# # Get the ACL's of the bucket(s) # #

# response = my_boto3_bucket_client.get_bucket_acl(
#     Bucket = "my-boto3bucket-using-python1"
# )
# print("Bucket ACL:",response)


## import requests
# # complete_details = response.json()

# for user_name in range(len(response)):
#     print(response["date"]["DisplayName"])
