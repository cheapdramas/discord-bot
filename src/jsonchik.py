from pathlib import Path
import json
import config 

json_filename = config.getenv("JSON_FILENAME") 
MAX_WARNINGS  = config.getenv("MAX_WARNINGS")
json_path = Path(json_filename)

class UserModel():
    def add_user(self):
        with json_path.open("w") as json_file:
            self.json_obj[self.id] = {"warn":self.warn }
            json_file.write(json.dumps(self.json_obj))


    def __init__(self,id:int, warn:int = 0) -> None:
        self.id = str(id)
        self.warn = warn
        with json_path.open("r") as json_file:
            self.json_obj = json.loads(json_file.read())
            user_payload : dict | None = self.json_obj.get(self.id)

            if not user_payload:
                print(f"User '{self.id}' not detected in json, adding")
                json_file.close()
                self.add_user()
            else:
                self.warn = user_payload["warn"]


    def add_warn(self):
        if self.warn < MAX_WARNINGS:
            self.warn = self.json_obj[self.id]["warn"] + 1
            self.add_user()
        
       
        
           

def create_json() -> bool:
    #file exists
    if json_path.exists():
        return False

    with json_path.open("w") as json_file:
        json_file.write(json.dumps({}))

    return True


def add_warn(user_id:int) -> int:
    print("Adding warn to json")
    user_model = UserModel(user_id)
    user_model.add_warn()

    return user_model.warn
