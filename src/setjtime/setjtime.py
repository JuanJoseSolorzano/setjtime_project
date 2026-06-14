import requests
import os
import argparse
from requests.auth import HTTPBasicAuth
from datetime import date
import sys
sys.stdout.reconfigure(encoding="utf-8")#type: ignore
sys.stderr.reconfigure(encoding="utf-8")#type: ignore

JIRA_SERVER = os.getenv("JIRA_SERVER","")
USERNAME = os.getenv("JIRA_USERNAME","")
PASSWORD = os.getenv("JIRA_PASSWORD","")
TODAY = date.today().strftime("%d/%m/%Y")
ISSUE_KEY = "SETV-%s"
URL = "https://{0}/rest/api/2/issue/{1}/comment"
HEADERS = {"Accept": "application/json","Content-Type": "application/json"}
PAYLOAD = {"body": ""}

def parse_args():
    parser = argparse.ArgumentParser(description="Add a comment to a JIRA issue.")
    parser.add_argument("issue_id", type=int, help="The ID of the JIRA issue (e.g., 6552 for SETV-6552).")
    parser.add_argument("-t", "--time",type=str,required=True, default="0h", help="Time spent to log, e.g., 1h, 30m, 2d, etc.")
    parser.add_argument("-c", "--comment",type=str,required=False, default="", help="for add a short unformatted comment.")
    return parser.parse_args()

def create_payload(args:argparse.Namespace) -> dict[str, str]:
    body = ""
    spent_time = args.time
    if args.comment:
        body = str(args.comment).replace(";", "\n")
    return {"timeSpent": spent_time,"comment": f" [{spent_time}] - {body} Logged on *{TODAY}*"}

def connect_jira(payload: dict[str,str],issue_id:str):
    url = f"https://{JIRA_SERVER}/rest/api/2/issue/{ISSUE_KEY % issue_id}/worklog"
    auth = HTTPBasicAuth(USERNAME, PASSWORD)
    response = requests.post(url, auth=auth, headers=HEADERS, json=payload)
    if response.status_code == 201:
        print("Worklog entry added successfully.")
    else:
        print("Failed to add worklog entry. Status code:", response.status_code)
        print(response.text)

def run():
    args = parse_args()
    payload = create_payload(args)
    connect_jira(payload,args.issue_id)

if __name__ == "__main__":
     run()