import schedule
import time
from pymongo import MongoClient
import requests

# initilize db
db_client = MongoClient('mongodb://db:27017/')
print(db_client.server_info())
mydb = db_client["enphase"]
mycol = mydb["data"]


def job():
    # This API is only for enphase system
    # Delete previous data
    mongoResponse = mycol.delete_many({})
    print(mongoResponse.deleted_count, " documents deleted.")
    # Hit Enphase data
    # URL = "https://api.enphaseenergy.com/api/v2/systems/1383584/stats?user_id=[Add your user id here]&key=[add your key here]"
    # Backup
    r = requests.get(url = URL)
    data = r.json()['intervals']
    print(data)
    # Adding new data to DB
    mongoResponse = mycol.insert_many(data)
    # check if added
    print(mongoResponse.inserted_ids)
    print("I'm working...")

schedule.every(30).minutes.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().hour.do(job)
job()
while 1:
    schedule.run_pending()
    time.sleep(1)
