import requests
import os

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def download_files(basedir):
    for uri in download_uris:
        file_name = uri.split("/")[-1]
        full_path = os.path.join(basedir, file_name)

        response = requests.get(uri)

        if response.status_code == 200:
            with open(full_path, 'wb') as f:
                f.write(response.content)
        else:
            print(f"Invalid URI - {uri}")
    else:
        print("Finished downloading all files")

def main():
    # your code here
    basedir = os.path.join(os.getcwd(), 'downloads')

    if not os.path.exists(basedir):
        os.mkdir(basedir)

    download_files(basedir)

if __name__ == "__main__":
    main()