"""Python application importing Jac modules"""
import jaclang #Enable Jac Imports

from validators import validate_title
from task_graph import Task, TaskCreator, generate_desc
from jaclang.lib import spawn, root

def create_task(title: str):
    "Python function using Jac features"
    if not validate_title(title):
        print("Title too short!")
        return
    
    #Use Jac walker
    creator = TaskCreator(title=title)
    spawn(creator, root())

    desc = generate_desc(title)
    print(f" AI: {desc}")

if __name__ == "__main__":
    create_task("Build API")