"""Application with inline Python validation."""

import models;

def generate_desc(title: str) -> str {
    return f"Task description for: {title}";
}

::py::
#Legacy Python validation - kept as-is
def validate_title(title):
    """Complex validation logic from old codebase"""
    return len(title) > 3 and title.strip() != ""

def get_sample_task():
    """Helper fromlegacy code"""
    return {"title": "Build API"}
::py::

walker TaskCreator {
    can create with `root entry {
        #Use inline python functions
        task_data = get_sample_task();

        if validate_title(task_data["title"]) {
            task = models.Task(title=task_data["title"]);
            here ++> task;
            desc = generate_desc(task.title);
            print(f"Created: {task.title}");
            print(f" AI: {desc}");
        } else {
            print("Title Invalid!");
        }
    }
}

with entry {
    root spawn TaskCreator();
}



