#!/usr/bin/python3
"""Export to CSV"""

import json
import requests


def get_employees_progress():
    """Get the Employees todos progress"""
    try:
        url = "https://jsonplaceholder.typicode.com"
        emps_data = requests.get(url + f'/users')
        emps_data = emps_data.json()

        """Getting Users"""
        users = {}
        json_filename = "todo_all_employees.json.json"

        for user in emps_data:
            emp_id = user["id"]
            emp_name = user["username"]

            """Getting the todos"""
            todos = requests.get(url + f'/todos?userId={emp_id}')
            todos = todos.json()

            """Prepare the JSON"""
            tasks = [
                {
                    "username": emp_name,
                    "task": task['title'],
                    "completed": task['completed']
                } for task in todos
            ]
            users[str(emp_id)] = tasks

        with open(json_filename, mode='w', newline='') as jf:
            json.dump(users, jf)

    except Exception as e:
        print(f"an error occurend: {e}")


if __name__ == "__main__":
    get_employees_progress()
