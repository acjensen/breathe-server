from datetime import timezone, datetime, timedelta
from google.cloud import firestore

def update_active_users(firestore: firestore.Client) -> None:

    now = datetime.now(timezone.utc)
    five_minutes_ago = now - timedelta(0, 300)
    num_active_users = 0

    # Count the last 5 minutes worth of pings. Flush anything else.
    query = firestore.collection("active_users")
    docs = query.stream()
    for doc in docs:
        if doc.to_dict()["ping_timestamp"] > five_minutes_ago:
            doc.ref.delete()
            print(f"Deleted expired ping for document [{doc.ref.id}]")
        else:
            num_active_users += 1

    # Update number of active users in the database.
    firestore.collection(u'num_active_users') \
        .document("num_active_users") \
        .set({"num_active_users": num_active_users})
    print(f"Updated active users to [{num_active_users}]")

    return None
