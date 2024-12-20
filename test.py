import schedule
import time
from google.cloud import firestore
from breathe.server import update_active_users

if __name__ == "__main__":

    firestore_client = firestore.Client()

    schedule.every(1).minutes.do(lambda: update_active_users(firestore_client))

    while True:
        schedule.run_pending()
        time.sleep(1)
