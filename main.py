import csv
import pandas as pd

class Task:
    CSV_FILE= "tasks.csv"
    COLUMNS= ["id","title","description"]

    @classmethod
    def read_file(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_tasks(cls, id,title,description):
        inputs= {
            "id":id,
            "title":title,
            "description":description
        }
        with open(cls.CSV_FILE, 'a', newline="") as file:
            update=csv.DictWriter(file, fieldnames=cls.COLUMNS)
            update.writerow(inputs)
        
        print("Task added successfully")

    
    @classmethod
    def delete_task(cls, id):
        df=pd.read_csv(cls.CSV_FILE)
        try:
            id=int(id)
            if id in df['id'].values:
                df=df[df['id'] != id]
                df.to_csv(cls.CSV_FILE, index=False)
                print("Task deleted successfully")
            else:
                print("Task not found")
        except ValueError:
            print("Invalid entry, try again")
        


def main():
    print("Welcome to your task manager")
    while True:
        print("\n1. Add a task.")
        print("2. View all tasks.")
        print("3. To delete task.")
        print("4. To exit.")

        choice=input("Enter your choice: ")
        if choice=="1":
            id=(input("\nEnter task id: "))
            while True:
                try:
                    id=int(id)
                    break
                except ValueError:
                    id=int(input("Invalid entry, try again(id must be an integer): "))

            title=input("Enter task title: ")
            description=input("Enter task description: ")
            Task.add_tasks(id,title,description)
        elif choice=="2":
            file= pd.read_csv(Task.CSV_FILE)
            if file.empty:
                print("No tasks found")
                continue
            print("\nHere are your tasks: \n")
            print(file.to_string(index=False))
            print("\n")
        elif choice=="3":
            id=input("\nEnter task id to delete: ")
            Task.delete_task(id)
        elif choice =="4":
            print("\nThank you for using task manager. Exiting...")
            break
        else:
            print("Invalid entry, try again")


if __name__=="__main__":
    Task.read_file()
    main()