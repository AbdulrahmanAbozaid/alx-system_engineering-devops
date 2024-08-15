#!/usr/bin/python3
"""Export to CSV"""

import csv
import requests
from sys import argv


def get_employee_progress(emp_id):
    """Get the Employee todos progress"""
    try:
        url = "https://jsonplaceholder.typicode.com"
        emp_data = requests.get(url + f'/users/{emp_id}')
        emp_data = emp_data.json()
        emp_name = emp_data["username"]

        """Getting the todos"""
        todos = requests.get(url + f'/todos?userId={emp_id}')
        todos = todos.json()

        numof_tasks = len(todos)
        done_tasks = [task for task in todos if task["completed"]]
        numof_done_tasks = len(done_tasks)

        """Results"""
        print(f"Employee {emp_name} is done with "
              f"tasks({numof_done_tasks}/{numof_tasks}):")

        """done tasks titles"""
        for tsk in done_tasks:
            print(f'\t {tsk["title"]}')

        csv_filename = f"{emp_id}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in todos:
                writer.writerow([emp_id, emp_name, task["completed"],
                                 task["title"]])
    except Exception as e:
        print(f"an error occurend: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: Script <employee_id>")
    else:
        get_employee_progress(argv[1])
