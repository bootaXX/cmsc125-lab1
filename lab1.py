import random
import time
import os


class User:
    def __init__(self, name):
        self.name = 'user' + name

    def sayname(self):
        print(self.name)


class Resource:
    def __init__(self, name):
        self.name = 'resource' + name
        self.time = 0
        self.user = None

    def sayname(self):
        print(self.name)

    def settime(self, t):
        self.time = t

    def setuser(self, u):
        self.user = u


class Generator:
    def __init__(self):
        self.users = []
        self.resources = []
        self.waiting_list = []

    # generators-----------------------------------------------------------------------------------
    def generateUsers(self):
        a = random.randint(1, 30)
        while a == 0:
            a = random.randint(1, 30)
        for x in xrange(1, a):
            u = User(str(x))
            self.users.append(u)

    def generateResources(self):
        a = random.randint(1, 30)
        while a == 0:
            a = random.randint(1, 30)
        for x in xrange(1, a):
            u = Resource(str(x))
            self.resources.append(u)

    # assigner/werker-----------------------------------------------------------------------------------
    def assignUsers(self):
        user_list = self.users[:]
        for resource in self.resources:
            if not user_list:
                resource.setuser(None)
                resource.settime(0)
            else:
                u = random.choice(user_list)
                user_list.remove(u)
                resource.setuser(u)
                resource.settime(random.randint(1, 30))

        if user_list:
            for user in user_list:
                self.waiting_list.append(user)

    def werk(self):
        # check if time is zero, put to waiting list
        for resource in self.resources:
            if resource.user is not None and resource.time == 0:
                self.waiting_list.append(resource.user)
                resource.setuser(None)
                resource.settime(0)

        # randomly place if no user, get head of waiting list, give random time
        for resource in self.resources:
            if resource.user is None and self.waiting_list:
                resource.setuser(self.waiting_list.pop(0))
                resource.settime(random.randint(1, 30))

        # time-=1
        for resource in self.resources:
            if resource.user is not None:
                resource.settime(resource.time-1)

    # printers-----------------------------------------------------------------------------------
    def showResources(self):
        print("Show Resources")
        print("---------------------------------------")
        for resource in self.resources:
            if resource.user is None:
                print(resource.name + " : None")
            else:
                print(resource.name + " : " + resource.user.name + " : " +
                      str(resource.time))

    def showUsers(self):
        print("Show Users")
        for user in self.users:
            user.sayname()

    def showWaitingList(self):
        print("Show Waiting List")
        for waiter in self.waiting_list:
            waiter.sayname()


def main():
    g = Generator()
    g.generateUsers()
    g.generateResources()
    g.assignUsers()
    z = 120

    while z > 0:
        g.showResources()
        print("---------------------------------------")
        g.showWaitingList()
        print("---------------------------------------")
        print("Simulation")
        print(z)
        z -= 1

        g.werk()

        time.sleep(1)
        os.system("clear")

if __name__ == '__main__':
    main()
