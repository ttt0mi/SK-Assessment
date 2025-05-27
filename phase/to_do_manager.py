def userinput_check(user_input):

	if not user_input or user_input.isspace():
		return "Input cannot be empty, Try again"
	
	if user_input.isalpha():
		return "Invalid character. Pick a number"

	if user_input.isdecimal():
		return True

	else: return "Invalid"



def add(tasks, task):

	tasks.update({task : "Incomplete"})
	return "Added"



def view_all(tasks):

	"""
	for index, (task, status) in enumerate(tasks.items(), 1):
		print(f"{index}. {task} || status: {status}")
	"""
	return tasks


def mark(tasks, mark_task):
	
	mark_task = int(mark_task)

	if all(index != mark_task for index, (task, status) in enumerate(tasks.items(), 1)):
		return "Task does not exist"

	for index, (task, status) in enumerate(tasks.items(), 1):
		if mark_task == index:
			tasks[task] = "complete"
			return f"Task {index} completed"			
				


def delete(tasks, delete_task):

	delete_task = int(delete_task)

	if all(index != delete_task for index, (task, status) in enumerate(tasks.items(), 1)):
		return "Task does not exist"
		
	for index, (task, status) in enumerate(tasks.items(), 1):
		if delete_task == index:
			tasks.pop(task)
			return f"Task {index} deleted"
	











	