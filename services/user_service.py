users = []
user_id_counter = 1

def create_user(user_data):
    global user_id_counter
    user = {**user_data.dict(), "id": user_id_counter, "is_active": True}
    users.append(user)
    user_id_counter += 1
    return user

def get_user(user_id):
    return next((u for u in users if u["id"] == user_id), None)

def get_all_users():
    return users

def update_user(user_id, user_data):
    user = get_user(user_id)
    if user:
        user.update(user_data.dict())
    return user

def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]

def deactivate_user(user_id):
    user = get_user(user_id)
    if user:
        user["is_active"] = False
    return user