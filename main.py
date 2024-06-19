class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"Player(name={self.name}, age={self.age}, position={self.position})"

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"

class Team:
    def __init__(self, team_name, team_id):
        self.team_name = team_name
        self.team_id = team_id
        self.players = []

    def __repr__(self):
        return f"Team(team_name={self.team_name}, team_id={self.team_id}, players={self.players})"

    def __str__(self):
        players_string = ', '.join([player.name for player in self.players])
        return f"Team Name: {self.team_name}, Team ID: {self.team_id}, Players: [{players_string}]"

class FootballTeamManagementSystem:
    def __init__(self):
        self.players = []
        self.teams = []

    def add_player(self, player):
        self.players.append(player)
        print(f"\n{player.name} added successfully")

    def view_players(self):
        if not self.players:
            print("\nNo available players")
            return
        for player in self.players:
            print(player)

    def update_player(self, name, new_name=None, new_age=None, new_position=None):
        player = next((p for p in self.players if p.name == name), None)
        if player:
            if new_name:
                player.name = new_name
            if new_age:
                player.age = new_age
            if new_position:
                player.position = new_position
            print(f"Player {name} updated successfully")
        else:
            print(f"No player found with name {name}")

    def delete_player(self, name):
        self.players = [player for player in self.players if player.name != name]
        print(f"Player {name} deleted successfully!")

    def add_team(self, team):
        self.teams.append(team)
        print(f"\n{team.team_name} added successfully")

    def view_teams(self):
        if not self.teams:
            print("\nNo available teams")
            return
        for team in self.teams:
            print(team)

    def update_team(self, team_id, new_name=None):
        team = next((t for t in self.teams if t.team_id == team_id), None)
        if team:
            if new_name:
                team.team_name = new_name
            print(f"Team ID {team_id} updated successfully")
        else:
            print(f"No team found with ID {team_id}")

    def delete_team(self, team_id):
        self.teams = [team for team in self.teams if team.team_id != team_id]
        print(f"Team ID {team_id} deleted successfully!")

    def assign_player_to_team(self, player_name, team_id):
        player = next((p for p in self.players if p.name == player_name), None)
        team = next((t for t in self.teams if t.team_id == team_id), None)
        if player and team:
            team.players.append(player)
            print(f"Player {player_name} assigned to team ID {team_id}")
        else:
            print(f"Either player {player_name} or team ID {team_id} does not exist")

    def remove_player_from_team(self, player_name, team_id):
        team = next((t for t in self.teams if t.team_id == team_id), None)
        if team:
            team.players = [p for p in team.players if p.name != player_name]
            print(f"Player {player_name} removed from team ID {team_id}")
        else:
            print(f"No team found with ID {team_id}")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for player in self.players:
                f.write(f"Player|{player.name}|{player.age}|{player.position}\n")
            for team in self.teams:
                players_string = ','.join([player.name for player in team.players])
                f.write(f"Team|{team.team_name}|{team.team_id}|{players_string}\n")
        print(f"Data saved to {filename}")

    def load_from_file(self, filename):
        self.players = []
        self.teams = []
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                if parts[0] == 'Player':
                    player = Player(parts[1], int(parts[2]), parts[3])
                    self.players.append(player)
                elif parts[0] == 'Team':
                    team = Team(parts[1], int(parts[2]))
                    player_names = parts[3].split(',') if parts[3] else []
                    for player_name in player_names:
                        player = next((p for p in self.players if p.name == player_name), None)
                        if player:
                            team.players.append(player)
                    self.teams.append(team)
        print(f"Data loaded from {filename}")

def main():
    ftms = FootballTeamManagementSystem()
    while True:
        print("\nFootball Team Management System Menu")
        print('1. Add Player')
        print('2. View Players')
        print('3. Update Player')
        print('4. Delete Player')
        print('5. Add Team')
        print('6. View Teams')
        print('7. Update Team')
        print('8. Delete Team')
        print('9. Assign Player to Team')
        print('10. Remove Player from Team')
        print('11. Save to file')
        print('12. Load from file')
        print('13. Exit')

        command = input("Enter your command: ")

        if command == "1":
            name = input("Enter player name: ")
            age = int(input("Enter player age: "))
            position = input("Enter player position: ")
            player = Player(name, age, position)
            ftms.add_player(player)
        elif command == "2":
            ftms.view_players()
        elif command == "3":
            name = input("Enter player name to update: ")
            new_name = input("Enter new name (optional): ")
            new_age = input("Enter new age (optional): ")
            new_position = input("Enter new position (optional): ")
            ftms.update_player(name, new_name or None, int(new_age) if new_age else None, new_position or None)
        elif command == "4":
            name = input("Enter player name to delete: ")
            ftms.delete_player(name)
        elif command == "5":
            team_name = input("Enter team name: ")
            team_id = int(input("Enter team ID: "))
            team = Team(team_name, team_id)
            ftms.add_team(team)
        elif command == "6":
            ftms.view_teams()
        elif command == "7":
            team_id = int(input("Enter team ID to update: "))
            new_name = input("Enter new team name (optional): ")
            ftms.update_team(team_id, new_name or None)
        elif command == "8":
            team_id = int(input("Enter team ID to delete: "))
            ftms.delete_team(team_id)
        elif command == "9":
            player_name = input("Enter player name to assign: ")
            team_id = int(input("Enter team ID to assign to: "))
            ftms.assign_player_to_team(player_name, team_id)
        elif command == "10":
            player_name = input("Enter player name to remove: ")
            team_id = int(input("Enter team ID to remove from: "))
            ftms.remove_player_from_team(player_name, team_id)
        elif command == "11":
            filename = input("Enter filename to save to: ")
            ftms.save_to_file(filename)
        elif command == "12":
            filename = input("Enter filename to load from: ")
            ftms.load_from_file(filename)
        elif command == "13":
            break

if __name__ == "__main__":
    main()
