class SMS_store:

    def __init__(self):
        self.message = []
        self.view_state = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.message.append((from_number, time_arrived, text_of_SMS))
        self.view_state.append(False)

    def message_count(self):
        return len(self.message)

    def get_unread_indexes(self):
        indices = []
        for (i, v) in enumerate(self.view_state):
            if not v:
                indices.append(i)
        return indices

    def get_message(self, i):
        try:
            self.view_state[i] = True
            return self.message[i]
        except:
            return None

    def delete(self, i):
        self.message.remove(self.message[i])
        self.view_state.remove(self.view_state[i])

    def clear(self):
        self.message = []
        self.view_state = []


my_inbox = SMS_store()
my_inbox.add_new_arrival("110011001", "2000-0-0 00:00:00", "It's a nice day today")
my_inbox.add_new_arrival("23", "233", "2333")
my_inbox.add_new_arrival("a", "aa", "aaa")
print(my_inbox.get_unread_indexes())
print(my_inbox.get_message(0))
print(my_inbox.get_unread_indexes())
