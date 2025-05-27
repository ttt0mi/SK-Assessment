
tasks = {}

while True:

	print("""

	To-do list manager

	1 >>> Add Task

	2 >>> View Tasks

	3 >>> Mark Task as Complete

	4 >>> Delete Task

	0 >>> Exit

	""")

	choice = str(input("Choose a number: "))

	if userinput_check(choice) != True:
		print(userinput_check(choice))
		continue

	match(choice):
		
		case '1':
			while True:
				print("What task do you want to add?")
				added_task = str(input())

				add(tasks, added_task)


		case '2':
			view_all(tasks)

		case '3':
			view_all(tasks)
			while True:
				mark_task = str(input("\nChoose the number of the task you want to mark as complete: "))

				if userinput_check(mark_task) == True:
					mark(tasks, mark_task)
					break
				else:
					print(userinput_check(mark_task))
					continue	


		case '4':
			view_all(tasks)
			while True:
				delete_task = str(input("\nChoose the number of the task you want to delete: "))
			
				if userinput_check(delete_task) == True:
					delete(tasks, delete_task)
					break
				else:
					print(userinput_check(delete_task))
					continue	



		case '0':
			print("okay, fuck off then")
			break;

		case _:
			print("that's invalid mate c'mon, try again")
			continue
