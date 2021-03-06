import csv
import random

experienced_players = [] #added list for all experienced_players
inexperienced_players = [] #add list for all inexperienced players
teammembers = ''

sharks = []
dragons = []
raptors = []

#get a random sample of experienced and inexperienced players for each team
def add_players(members, number_of_players):
    teammembers = random.sample(members, number_of_players)
    for team_member in teammembers:
        members.remove(team_member)
    return teammembers

#function to add players to each team
def add_to_team(team_name):
    team_name.extend(add_players(experienced_players, number_of_experienced_players))
    team_name.extend(add_players(inexperienced_players, number_of_inexperienced_players))
    return (team_name)

def print_teams(team, teamname):
    print('\n')
    print(teamname)
    print('\n')
    for row in team:
        print(row['Name'],row['Soccer Experience'],row['Guardian Name(s)']) #Print fields and data to screen

if __name__ == "__main__":
    with open('soccer_players.csv' ) as csvfile:
        playerreader = csv.DictReader(csvfile, delimiter = ',' )
        rows = list(playerreader)

        for row in rows:
            del row['Height (inches)'] #height was not required in output removed
            if row['Soccer Experience'].lower() == 'yes':
                experienced_players.append(row)
            if row['Soccer Experience'].lower() == 'no':
                inexperienced_players.append(row)

    number_of_experienced_players = len(experienced_players) / 3 #even number of players on each of 3 teams
    number_of_inexperienced_players = len(inexperienced_players) / 3
    teammembers = ''
    #get a random sample of experienced and inexperienced players for each team
    def add_players(members, number_of_players):
        #in python 2.7 divide by float on .sample does not generate error
        #in python 3.6 divide by float generates an error corrected by int(number_of_players)
        teammembers = random.sample(members, int(number_of_players))
        for team_member in teammembers:
            members.remove(team_member)
        return teammembers
    #function to add players to each team
    def add_to_team(team_name):
        team_name.extend(add_players(experienced_players, number_of_experienced_players))
        team_name.extend(add_players(inexperienced_players, number_of_inexperienced_players))
        return (team_name)

    def print_teams(team, teamname):
        print('\n')
        print(teamname)
        print('\n')
        for row in team:
            print(row['Name'],row['Soccer Experience'],row['Guardian Name(s)']) #Print fields and data to screen
    # add players to teams
    add_to_team(sharks)
    add_to_team(dragons)
    add_to_team(raptors)
    # Use Print Function to print teams to screen
    print_teams(sharks, 'Sharks')
    print_teams(dragons, 'Dragons')
    print_teams(raptors, 'Raptors')

    # Print Teams to file added Header Row for Clarification
    with open('teams.txt', 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['Name', 'Guardian Name(s)', 'Soccer Experience',], delimiter=',')
        csv_file.write("Sharks"'\n')
        writer.writeheader()
        for row in sharks:
            writer.writerow(row)

        csv_file.write('\n'"Raptors"'\n')
        writer.writeheader()
        for row in raptors:
            writer.writerow(row)

        csv_file.write('\n'"Dragons"'\n')
        writer.writeheader()
        for row in dragons:
            writer.writerow(row)
