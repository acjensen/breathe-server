import schedule
import time
from datetime import timezone, datetime, timedelta
from google.cloud import firestore

if __name__ == "__main__":
    
    # Project ID is determined by the GCLOUD_PROJECT environment variable
    db = firestore.Client()

    def update_active_users() -> None:

        now = datetime.now(timezone.utc)
        five_minutes_ago = now - timedelta(0, 300)
        num_active_users = 0

        # Count the last 5 minutes worth of pings. Flush anything else.
        query = db.collection(
            u'active_users')
        docs = query.stream()
        for doc in docs:
            if doc.to_dict()["ping_timestamp"] > five_minutes_ago:
                print("Deleting an old ping...")
                doc.ref.delete()
            else:
                num_active_users += 1
        print(f"Active users: {num_active_users}")

        # Update the database.
        db.collection(
            u'num_active_users').document("num_active_users").set({
        "num_active_users": num_active_users})

        return None

    schedule.every(1).minutes.do(update_active_users)

    while True:
        schedule.run_pending()
        time.sleep(1)