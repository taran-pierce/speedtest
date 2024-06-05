import speedtest
import asyncio
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
  print("\n")
  print("Testing your download speed...\n")

  bytes = st.download()

  megabytes = round(calculate_megabytes(bytes), 2)

  return f"{megabytes} /Mbps"

def get_upload_speed():
  print("\n")
  print("Testing your upload speed...\n")

  bytes = st.upload()

  megabytes = round(calculate_megabytes(bytes), 2)

  return f"{megabytes} /Mbps"

def get_ping():
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
  print("Download speed it is!")
  print("It may take a few moments while it tests your download speed...\n")

  bytes = st.download()

  megabytes = round(calculate_megabytes(bytes), 2)

  print(f"You have a Download speed of: {megabytes}/Mbps")
elif user_option == 2:
  print("Upload speed it is!")
  testing = st.upload()

  print(testing)
elif user_option == 3:
  asyncio.run(get_ping())
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

