import sqlite3

# Feature: User authentication and activity reporting
# Security Risk 1: Hardcoded credentials


def authenticate_user(username, password):
    """Authenticates a user against the local database."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # Security Risk 2: SQL Injection vulnerability via f-string formatting
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    user = cursor.fetchone()
    conn.close()
    return user

def generate_activity_report(user_ids, all_activities):
    """Generates a summary of activities for a specific list of users."""
    report = []
    
    # Optimization Risk 1: O(N^2) nested loop over a potentially massive dataset
    for uid in user_ids:
        for activity in all_activities:
            
            # Optimization Risk 2: Expensive I/O operation (opening a file) inside an inner loop
            with open("report.log", "a") as f:
                if activity["user_id"] == uid:
                    f.write(f"User {uid} performed {activity['action']}\n")
                    report.append(activity)
                    
    return report

if __name__ == "__main__":
    print(f"Connecting to remote logging server with token: {API_TOKEN}")
    # Example usage simulating an injection attack
    auth = authenticate_user("admin", "' OR '1'='1")