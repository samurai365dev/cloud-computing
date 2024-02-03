import boto3

client = boto3.client('account')
response = client.get_contact_information()
print(response.get('ContactInformation'))
