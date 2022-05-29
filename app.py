import os, uuid, json, datetime
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

# Read Configuration details from Json file / os.environ
try:
    with open('./config.json') as config_file:
        CONFIG = json.load(config_file)
except Exception as e:
    print("\nMake sure there is a file called 'config.json' in the root directory")
    exit(1)

try:
    print("--- This is AZ Storage Account from Python ---")
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(CONFIG["STORAGE_ACCOUNT_CONNECTION_STRING"])
    
    # Create a unique name for the container
    container_name = "1-pics"

    # Create the container
    # container_client = blob_service_client.create_container(container_name)

    # Read an Existing Container
    container_client = blob_service_client.get_container_client(container_name)

except Exception as ex:
    print('\nException:')
    print(ex)
    exit(1)



print("\nListing blobs... For Container: " + container_name)

# List the blobs in the container
blob_list = container_client.list_blobs()
print("Created on \t Blob Name")
for blob in blob_list:
    print(blob.creation_time.date(),"\t",blob.name)
