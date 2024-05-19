#!/usr/bin/python3
"""
Check student JSON output
"""

import json
import sys

def user_info(id):
    """Check user info"""
    try:
        with open(f"{id}.json", 'r') as f:
            student_json = json.load(f)

        if str(id) in student_json and len(student_json) == 1:
            print("Correct USER_ID: OK")
        else:
            print("Correct USER_ID: Incorrect")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    user_info(sys.argv[1])
