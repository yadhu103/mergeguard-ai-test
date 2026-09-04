import sqlite3

# Feature: User authentication and activity reporting
# Security Risk 1: Hardcoded credentials

API_TOKEN = "ghp_super_secret_github_token_123456789" 

# Feature: User authentication and activity reporting
def authenticate_user(username, password):
    """Authenticates a user against the local database."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # Test flaw 2: Actual SQL Injection vulnerability via f-string formatting
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
        
    user = cursor.fetchone()
    conn.close()
    return user

def generate_activity_report(user_ids, all_activities):
    """Generates a summary of activities for a specific list of users."""
    report = []
    user_ids_set = set(user_ids) # Optimization 1: O(1) lookup
    
    # Optimization 2: Open file once outside the loop
    with open("report.log", "a") as f:
        for activity in all_activities:
            if activity["user_id"] in user_ids_set:
                f.write(f"User {activity['user_id']} performed {activity['action']}\n")
                report.append(activity)
                    
    return report

if __name__ == "__main__":
    print(f"Connecting to remote logging server with token: {API_TOKEN}")
    # Example usage simulating an injection attack
    auth = authenticate_user("admin", "' OR '1'='1")
