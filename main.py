import speedtest
import os

st = speedtest.Speedtest()
server_names = []
st.get_servers(server_names)

def clear_screen():
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

user_option = int(input(r'''What type of internet speed do you want to test?
                        
1 - Download
                        
2 - Upload

3 - Ping
                        
4 - All three
                        
Enter the number for your choice: 
'''))

clear_screen()

if user_option == 1:
  print("\n")

  download = get_download_speed()

  print(f"Download: {download}")
elif user_option == 2:
  print("\n")

  upload = get_upload_speed()
  print(f"Upload: {upload}")
elif user_option == 3:
  print("\n")
  ping = get_ping()

  print(f"Ping: {ping}")
elif user_option == 4:
  print("\n")

  results = {
    "Download": get_download_speed(),
    "Upload": get_upload_speed(),
    "Ping": get_ping(),
  }

  for result in results:
    print(f"{result}: {results[result]}")
else:
  print(f"Invalid Option: {user_option}.")
  print("Please enter: 1, 2, 3, or 4")

