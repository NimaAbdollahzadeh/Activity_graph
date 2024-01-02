import matplotlib.pyplot as plt 
from datetime import datetime, timedelta
import requests

def get_github_activity(username):
    one_year_ago = datetime.now() - timedelta(days=365)
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    since_date = one_year_ago.strftime(date_format)

    url = f"https://api.github.com/users/{username}/events"
    params = {"since": since_date}
    
    response = requests.get(url, params=params)
    events = response.json()

    return events

def plot_activity_graph(events):
    contributions = {"date": [], "count": []}

    for event in events:
        if event["type"] == "PushEvent":
            date = event["created_at"][:10]
            contributions["date"].append(date)
            contributions["count"].append(len(event["payload"]["commits"]))
    
    plt.figure(figsize=(12, 6))
    plt.plot(contributions["date"], contributions["count"], marker="o")
    plt.title("Gitgub Contribution Activity")
    plt.xlabel("Date")
    plt.ylabel("Number of commits")
    plt.xticks(rotation= 45)
    plt.tight_layout()

    plt.savefig("github_activity_graph.png")
    plt.show()

if __name__ == "__main__":
    github_username = "NimaAbdollahzadeh"
    github_events = get_github_activity(github_username)
    plot_activity_graph(github_events)