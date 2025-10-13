"""Pure Python using Jac runtime"""

from jaclang.lib import Node, Walker, on_entry, connect, spawn, root
from validators import validate_title

# Define Task node using Jac base clas
class Task(Node):
    title: str
    done: bool 

    def __init__(self, title: str):
        super().__init__()
        self.title = title
        self.done = False


#Define walker using Jac Decorators
class TaskCreator(Walker):
    def __init__(self, title: str):
        super().__init__()
        self.title = title



    @on_entry
    def create(self, here) -> None:
        """Entry point creates a task"""
        if validate_title(self.title):
            task = Task(title=self.title)
            connect(here, task)
            print(f"Created: {task.title}")
            #AI features require .jac syntax
        else:
            print("Title too short!")

if __name__ == "__main__":
    creator = TaskCreator(title="Build API")
    spawn(creator, root())