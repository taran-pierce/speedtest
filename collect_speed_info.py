import os

from dotenv import load_dotenv

load_dotenv()

# config data
DB_USERNAME = os.getenv("USER_NAME")
DB_PASSWORD = os.getenv("USER_PASSWORD")

# import dependencies
import speedtest
import pymongo
import datetime
import certifi
from pymongo.server_api import ServerApi

# get CA cert using "certifi"
ca_cert_path = certifi.where()

# set up mongodb URI
uri = f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@cluster0.94s77tq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
# setting TLS and adding in CAFile path for the cert
client = pymongo.MongoClient(uri,
  tls=True,
  tlsCAFile=ca_cert_path,
  server_api=ServerApi(
    version='1',
  ))

# grab correct db and collection
db = client["speedtest"]
collection = db["results"]

program_on = True

# initialize speedtest-cli
# it is free, so we get rate limited
try:
  st = speedtest.Speedtest()
  server_names = []
  st.get_servers(server_names)
except Exception as e:
  print("Error with Speedtest-CLI\n")
  print(f"Erorr: {e}\n")
  print("Please try again later...\n")

  # not much we can do if we cant use speedtest-cli
  program_on = False

def clear_screen():
  """
  Function to clear terminal screen
  """
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def get_download_speed():
  """
  Calculates download speed using speedtest-cli
  """
  print("\n")
  print("Testing your download speed...\n")

  bytes = st.download()

  megabytes = round(calculate_megabytes(bytes), 2)

  return f"{megabytes} / Mbps"

def get_upload_speed():
  """
  Calculates upload speed using speedtest-cli
  """
  print("\n")
  print("Testing your upload speed...\n")

  bytes = st.upload()

  megabytes = round(calculate_megabytes(bytes), 2)

  return f"{megabytes} / Mbps"

def get_ping():
  """
  Calculates ping using speedtest-cli
  """
  print("\n")
  print("Calculating your ping...\n")

  return f"{st.results.ping} ms"

def calculate_megabytes(bytes):
  """
  Takes an Integer - Returns an Integer of passed bytes convereted into megabytes.
  """

  # 1 megabyte = 1024 * 1024 bytes
  megabytes = bytes / (1024 * 1024)

  return megabytes

def update_db(type, data):
  try:
    # create dictionary to insert into db
    document = {
      "type": type,
      "speed": data,
      "date": datetime.datetime.now().date().strftime("%m-%d-%Y"),
      "time": datetime.datetime.now().time().strftime("%I:%H:%M"),
    }

    # For CL, printing out values being added
    print("Inserting the following data...\n")

    for data in document:
      print(f"{data} - {document[data]}")

    # insert into db collection
    collection.insert_one(document)
  except Exception as e:
    print(e)

# create dictionary for results
results = {
  "Download": get_download_speed(),
  "Upload": get_upload_speed(),
  "Ping": get_ping(),
}

# upload results to DB
for result in results:
  update_db(result, results[result])

# close connection
client.close()

print("Success")
