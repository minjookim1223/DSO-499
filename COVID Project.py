import random
import csv
import numpy as np


csvTitle = 'group_info_case_C.csv'  # name of group information file
days = 10
MAX = 0


# The class below creates a person object who could potentially become infected
class Person:
    # Input: person's unique identifier (id)
    def __init__(self, person_id):
        self.id = str(person_id)
        self.status = 0
        self.days_infection = 0
        self.days_hospitalized = 0

    def update_status(self):
        self.status += 1

    def days_infection_update(self):
        if self.status == 1:
            self.days_infection += 1

    def days_hospitalized_update(self):
        if self.status == 2:
            self.days_hospitalized += 1


# The Group class will have person objects
class Group:
    def __init__(self, group_id, prob_infection, member_list, head_count):
        self.group_id = group_id  # group identifier
        self.prob = prob_infection  # probability of infection in the group
        self.member_list = member_list  # list of members
        self.num_sick = 0  # number of infectious
        self.head_count = head_count  # count of people
        self.status = True  # true (open), false (closed)
        self.num_hospitalized = 0

    def num_infectious(self, person_dict, group):
        self.num_sick = 0  # Number of infectious people set to 0 in the beginning
        # Loop through each member in the member list within the group
        for member in group.member_list:
            # If the status is 1 and the days of infection is not 0,
            if person_dict[str(member)].status == 1 and person_dict[str(member)].days_infection != 0:
                # update the variable by adding 1
                self.num_sick += 1

        return self.num_sick

    def get_number_hospitalized(self, person_dict, group):  ######## UPDATE
        for member in group.member_list:
            if person_dict[str(member)].status == 2:
                self.num_hospitalized += 1
        return self.num_hospitalized

    # Check for new infections
    def new_infections(self, person_dict, group):
        for member in group.member_list:  # Loop through the members in the member list
            for i in range(self.num_sick):  # for each infectious person,
                if person_dict[str(member)].status == 0:  # If the status is 0,
                    prob = np.random.rand()  # check for the probability of the infection
                    if prob < self.prob:  # if the condition of the probability is met,
                        person_dict[str(member)].update_status()  # update the status by using the function

    # Change the status if the head count is bigger than than the closed head count
    # False for closed, True for opened
    def change_status(self, headcount_close):
        if self.head_count >= headcount_close:
            self.status = False
        else:
            self.status = True

    def update_hospitalized(self, person_dict, group):
        for member in group.member_list:
            if person_dict[str(member)].days_infection == days - 3:  # if days_infection and days are ==,
                person_dict[str(member)].update_status()
                person_dict[str(member)].days_infection = 0
                # update the status of the member

    # Update the number of those recovered
    def update_recovered(self, person_dict, group):
        for member in group.member_list:
            if person_dict[str(member)].days_hospitalized == 3:  # if days_infection and days are ==,
                person_dict[str(member)].update_status()  # update the status of the member
                person_dict[str(member)].days_hospitalized = 0  # set the infection days to 0 again

    def close_by_hospitalized(self, person_dict, group):
        for member in group.member_list:
            if person_dict[str(member)].status == 2:
                self.status = False


days = 10
MAX = 0


def load():
    group_list = []
    person_dict = {}
    max_head_count = 0

    with open(csvTitle, 'r') as csvFile:
        file = csv.DictReader(csvFile)
        for row in file:
            members = [int(i) for i in row["members"].split(',')]

            for member in members:
                person_dict[str(member)] = person_dict.get(Person(str(member)), Person(str(member)))

            group_list.append(Group(row["group_ID"], float(row["prob"]), members, int(row["headcount"])))
            if int(row["headcount"]) > max_head_count:
                max_head_count = int(row["headcount"])

    MAX = max_head_count

    # list of persons
    person_objects = []

    for person in person_dict.values():
        person_objects.append(person)

    return person_dict, group_list, person_objects


# Simulation function to incorporate into our monte carlo simulations
def simulate(count):
    # load the available information in the csv file and put those into dictionary, list and object lists
    total = 20  # cumulative sum of infected and hospitalized people
    max_hospitalized = 0
    person_dict, group_list, person_list = load()

    # randomly chooses sick people
    infected_people = random.choices(person_list, k=20)

    # for each infected person in infected_people,

    for infected in infected_people:
        # create a person dictionary for each
        person = person_dict.get(str(infected.id))
        # since the person is infected, change the status
        person.update_status()

    # For each group object in group object list,
    for group in group_list:
        # update and change the status based on given head count
        group.change_status(count)

    # Loop until there is 0 infected people
    while total != 0:
        # Iterate through the group_list again
        for group in group_list:
            # finds the number of sick people
            num_sick = group.num_infectious(person_dict, group)
            num_hospitalized = group.num_hospitalized
            # if the number of sick people is less than the length of the member list and group status is open,
            if num_sick + num_hospitalized < len(group.member_list) and group.status:
                # find the number of infected
                group.new_infections(person_dict, group)

        # Again, iterate through the group list
        for group in group_list:
            # to account for those who have been infected but recovered
            group.update_hospitalized(person_dict, group)
            group.update_recovered(person_dict, group)

        total = 0

        # Loop through each person in the person_dict
        for person in person_dict.values():
            # if each person's status is 1 or 2, increase the total number of infected by 1
            if person.status == 1 or person.status == 2:
                total += 1

        # For each person in the dictionary,
        for person in person_dict.values():
            # update each person's infection period
            person.days_infection_update()
            person.days_hospitalized_update()

        # Counter to refresh the max number status 2 on a day
        for group in group_list:
            num_hospitalized = group.get_number_hospitalized(person_dict, group)
            if num_hospitalized > max_hospitalized:
                max_hospitalized = num_hospitalized

        # close the group if a person is hospitalized
        for group in group_list:
            group.close_by_hospitalized(person_dict, group)

    return max_hospitalized


def monte_carlo(m, head_count):
    return round(np.mean([simulate(head_count) for i in range(m)]), 0)


days = 10
MAX = 0


# This function will be used to load the necessary info from the csv file

def main():
    minHeadCountClosed = 10000000000000000
    max_hospitalizedAllowed = 50

    person_dict, group_list, person_list = load()
    maxHeadCount = 0

    for group in group_list:
        if group.head_count > maxHeadCount:
            maxHeadCount = group.head_count

    print("Headcount, Function, HeadClose")
    for head_count in range(2, maxHeadCount + 1):
        objFunction = monte_carlo(100, head_count)
        print(head_count, objFunction, sep=", ")
        if objFunction <= max_hospitalizedAllowed:
            print("Not over max_hospitalizedAllowed(50beds) with ", objFunction, "with a headcount of", head_count)


main()

