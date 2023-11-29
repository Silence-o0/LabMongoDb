from pymongo import MongoClient


def add_exam():
    group = input('Group: ')
    subject = input('Subject: ')
    date = input('Date: ')
    time = input('Time: ')
    teachers = input('Teachers: ')
    type = input('Type of exam(Залік/Екзамен): ')
    while type != 'Залік' and type != 'Екзамен':
        print("Incorrect data.")
        type = input('Type of exam(Залік/Екзамен): ')

    record = {"group": group, "subject": subject, "date": date,
          "time": time, "Teachers": teachers, "type": type}
    exam_collection.insert_one(record)

    additional_field = input("You can add additional field (enter '0' to finish entering): ")
    while additional_field != '0':
        additional_value = input(f"{additional_field}: ")

        add_new_value = {"$set": {additional_field: additional_value}}
        exam_collection.update_one(record, add_new_value)

        additional_field = input("You can add additional field (enter '0' to finish entering): ")


def make_schedule_for_group():
    group = input('Group: ')
    records_filter = {"group": group}
    all_group_records = exam_collection.find(records_filter)

    for x in all_group_records:
        print(x)


if __name__ == '__main__':
    myclient = MongoClient(
        "mongodb://mongo:mongo@localhost:27017")

    db = myclient["schedule"]
    exam_collection = db["exams"]

    # add_exam()
    make_schedule_for_group()

