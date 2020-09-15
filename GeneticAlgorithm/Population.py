class Population:

    # has a size
    def __init__(self, size):
        self.size = size
        self.members = [] # each memeber will be a ml class

    # add a member
    # returns index
    def add(self, member):
        self.members.append({
            'member': member,
            'fitness': None,
        })
        return len(self.members)-1

    def get_member(self, index):
        return self.members[index]['member']

    def get_fitness(self, index):
        return self.members[index]['fitness']

    def set_fitness(self, index, fitness):
        self.members[index]['fitness'] = fitness