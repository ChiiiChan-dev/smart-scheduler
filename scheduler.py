exam_schedule = []

# Adding function of schedule entry including the name, time, date, and assigned room.
def exam_adding(exam_name, time, date, assigned_room):
    exam = {
        "exam name": exam_name,
            "time": time,
            "date": date,
            "assigned_room": assigned_room
            }
    exam_schedule.append(exam)
    print(f"Exam:({exam_name}) added to entry.")

# View function that have access of viewing stored entries in empty list of exam_schedule.
def view_schedule():
    if not exam_schedule:
        print("No exams scheduled.")
        return
    print("Exam Schedule:")
    for exam in exam_schedule:
        print(f"Exam name: {exam['exam name']}, "
              f"Time: {exam['time']}, "
              f"Date: {exam['date']}, "
              f"Room: {exam['assigned_room']}")

# Function edit/update of entry:{name} time, date, and assigned room.
def update_entry():
    exam_name = input("Enter exam:")
    for exam in exam_schedule:
        if exam["exam name"] == exam_name:
            new_time = input("Enter new time: ")
            new_date = input("Enter new exam date:")
            new_room = input("Enter new room: ")

            if new_time:
                exam['time'] = new_time
            if new_date:
                exam['date'] = new_date
            if new_room:
                exam['assigned_room'] = new_room

            print(f"Exam: ('{exam_name}') has been updated successfully.")
            return
    print(f"Exam ({exam_name}) does not exist in the entry.")

#Remove entry schedule permanently in the dictionary by accessing the "exam name" as its requirement for deletion.
def remove_schedule(exam_name):
    for exam in exam_schedule:
        if exam["exam name"] == exam_name:
            exam_schedule.remove(exam)
            print(f"Exam {exam_name} removed from the entry.")
            return
    print(f"Exam ({exam_name}) does not exist in the entry.")

# The main function that runs the entire system code.
def main():
    # User-Interface of the Smart-Scheduler.
    while True:
        print("\n*******SMART-SCHEDULER*******")
        print("Menu:")
        print("1. Add Exam Entry.")
        print("2. View Schedule.")
        print("3. Update Entry Schedule.")
        print("4. Remove Exam Entry.")
        print("5. Exit.")
        print("*****************************")
        user_choice = input("\nEnter a choice (1-5): ")

        if user_choice == "1":
            exam = input("Enter exam name: ")
            time = input("Enter time for the exam: ")
            date = input("Enter date of the exam: ")
            assigned_room = input("Enter assigned room: ")
            exam_adding(exam, time, date, assigned_room)

        elif user_choice == "2":
            view_schedule()

        elif user_choice == "3":
            update_entry()

        elif user_choice == "4":
            exam_name = input("Enter exam name to be remove:")
            remove_schedule(exam_name)

        elif user_choice == "5":
            print("Terminating program...")
            print("Exiting Smart Scheduler.")
            break
        else:
            print("\nInvalid input. Please choose only from (1-5).")


# Run Program
if __name__ == "__main__":
    main()
