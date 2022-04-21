import os

directory_of_the_script_being_run = os.path.dirname(os.path.abspath(__file__))
current_working_dir = os.path.abspath(os.getcwd())

print(directory_of_the_script_being_run)
print(current_working_dir)
