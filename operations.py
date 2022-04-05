import json
import datetime


id =1

def insert(data):

    new_data = {}
    new_data['id'] = id
    with open("database/db.json",'r+') as file:
        file_data = json.load(file)
        new_data['data'] = data
        file_data["documents"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
    print("Successfully Inserted!")
    write_db_transaction(1, "INSERT")
    return "True"


def search(condition):
    obj = json.load(open("database/db.json"))
    documents = obj['documents']
    search_item = None
    data_keys = list(dict(condition).keys())
    data_values = list(dict(condition).values())
    for i in range(len(documents)):
        for j in range(len(data_keys)):
            if documents[i]['data'][data_keys[j]]==data_values[j]:
                print("found!")
                search_item = documents[i]
                break
    return search_item

def update(data,condition):
    obj = json.load(open("database/db.json"))
    documents = obj['documents']
    search_item = search(condition)
    id = search_item['id']
    print(id)
    data_keys = dict(data).keys()
    for i in range(len(documents)):
        if documents[i]['id'] == id:
            write_db_history(data,id)
            for key in data_keys:
                if documents[i]['data'][key]!=None:
                    obj['documents'][i]['data'][key] = data[key]
            open("database/db.json", "w").write(json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))
    write_db_transaction(1, "UPDATE")


def write_db_transaction(transaction_id,transaction):
    new_data = {}
    new_data['transaction_id'] = transaction_id
    new_data['transaction'] = transaction
    new_data['time_stamp'] = get_time()
    new_data['user'] = get_user()
    with open("database/db_transaction.json", 'r+') as file:
        file_data = json.load(file)
        file_data["documents"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

def write_db_history(data,id):
    # obj = json.load(open("database/db.json"))
    # documents = obj['documents']
    new_data = {}
    with open("database/db_history.json", 'r+') as file:
        file_data = json.load(file)
        new_data['id'] = id
        new_data['data'] = data
        file_data["documents"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

    print(new_data)

def get_time():
    commit_time = datetime.datetime.now()
        # print(str(commit_time))
    return str(commit_time)

def get_user():
    user_name = "rukmals"
    return user_name

