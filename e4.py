import queue

def register_patient(patient_queue):
    patient_name = input("Enter patient name: ")
    patient_queue.put(patient_name)
    print(f"Patient '{patient_name}' registered.")

def remove_patient(patient_queue):
    if not patient_queue.empty():
        removed_patient = patient_queue.get()
        print(f"Patient '{removed_patient}' removed after meeting the doctor.")
    else:
        print("No patients in the queue.")

def display_patient_queue(patient_queue):
    if not patient_queue.empty():
        print("Current patient queue:")
        for patient in list(patient_queue.queue):
            print(patient)
    else:
        print("No patients in the queue.")

def main():
    patient_queue = queue.Queue()

    while True:
        print("\nMenu:")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_patient(patient_queue)
        elif choice == "2":
            remove_patient(patient_queue)
        elif choice == "3":
            display_patient_queue(patient_queue)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
