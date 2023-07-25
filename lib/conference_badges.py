def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    rooms = 1
    messages = []
    for name in names:
        message = f"Hello, {name}! You'll be assigned to room {rooms}!"
        messages.append(message)
        rooms+=1
        
    return messages

def printer(names):
    for name in names:
        print(f"Hello, my name is {name}.")
    messages = (assign_rooms(names))
    for message in messages:
        print(message)