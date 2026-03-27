#!/usr/bin/env python3
"""
main.py

Description: Brief description of what this script does.
Author: Your Name
Date: 2026-03-25
"""

import sys
import logging
import pandas as pd
from typing import Any
import matplotlib.pyplot as plt

owners = {
    'Rachel': ['Coach', 'Cirie', 'Rizzo', 'Dee', 'Ozzy', 'Emily', 'Aubry', 'Jenna'],
    'Ian': ['Genevieve', 'Charlie', 'Savannah', 'Tiffany', 'Kyle', 'Joe', 'Devens', 'Johnathan'],
    'Nate': ['Colby', 'Christian', 'Angelina', 'Kamilla', 'Stephanie', 'Q', 'Mike White', 'Chrissy']
}

tribes = {
    "Cila2": [
        "Cirie",
        "Devens",
        "Charlie",
        "Dee",
        "Jonathan",
        "Kamilla",
        "Rizzo"
    ],
    "Kalo2": [
        "Aubry",
        "Colby",
        "Tiffany",
        "Coach",
        "Chrissy",
        "Joe",
        "Genevieve"
    ],
    "Vatu2": [
        "Stephenie",
        "Ozzy",
        "Emily",
        "Christian",
        "Mike White",
        "Q",
        "Angelina"
    ],"Cila": [
        "Jenna",
        "Christian",
        "Cirie",
        "Ozzy",
        "Savannah",
        "Joe",
        "Rick",
        "Emily"
    ],
    "Kalo": [
        "Charlie",
        "Chrissy",
        "Dee",
        "Coach",
        "Jonathan",
        "Kamilla",
        "Mike",
        "Tiffany"
    ],
    "Vatu": [
        "Colby",
        "Stephenie",
        "Angelina",
        "Genevieve",
        "Kyle",
        "Q",
        "Rizo",
        "Aubry"
    ]
}


class Person:
    def __init__(self, name, points=0, items=None):
        self.name = name
        self.points = points
        self.items = items if items is not None else []

    def add_points(self, amount):
        """Increase the person's point total."""
        self.points += amount

    def add_item(self, item):
        """Add a string item to the list."""
        self.items.append(item)

    def add_items(self, items):
        for item in items:
            self.items.append(item)

    def remove_item(self, item):
        """Remove an item if it exists."""
        if item in self.items:
            self.items.remove(item)

    def __str__(self):
        return f"Person(name={self.name}, points={self.points}, items={self.items})"
    

    


    


    
# ----------------------------
# Core Logic
# ----------------------------
def main(args: list[str]) -> int:
    nate = Person("Nate")
    ian = Person("Ian")
    rachel = Person("Rachel")
    people = [nate,ian,rachel]

    kalo_tribe = ['Charlie','Chrissy','Coach','Dee','Johnathan','Kamilla','Mike White','Tiffany']
    vatu_tribe = ['Angelina','Aubry','Colby','Genevieve','Kyle','Q','Rizzo','Stephanie']
    cila_tribe = ['Christian', 'Cirie', 'Emily','Jenna','Joe','Ozzy','Devens','Savannah']

    kalo_tribe2 = ['Aubry', 'Chrissy','Coach','Colby','Genevieve','Joe','Tiffany']
    vatu_tribe2 = ['Angelina','Christian','Emily','Mike','Ozzy','Q','Stephanie']
    cila_tribe2 = ['Charlie','Cirie','Dee','Johnathan','Kamilla','Devens','Rizzo']

    rachel_players = ['Coach', 'Cirie', 'Rizzo', 'Dee','Ozzy','Emily','Aubry','Jenna']
    ian_players = ['Genevieve', 'Charlie', 'Savannah', 'Tiffany','Kyle','Joe','Devens','Johnathan']
    nate_players = ['Colby', 'Christian','Angelina','Kamilla','Stephanie','Q','Mike White','Chrissy']

    
    
    players = [nate_players,ian_players,rachel_players]

    for i in range(len(people)):
        people[i].add_items(players[i])

    results = pd.read_csv("points_ep5.csv")
    
    #Calc Team Points
    nan_rows = results[results.isna().any(axis=1)]
    for idx, row in nan_rows.iterrows():
        team = row['player']
        players = tribes[team]

        for player in players:
            owner = find_tribe(player,owners)
            results.loc[len(results)] = [owner, player, row['points'],row['reason'],row['episode']]

    print(results)

    # Keep only rows where 'player' is NOT a team
    results = results[~results['player'].isin(tribes)]


    #Remove Rows for eliminated players
    remove_elim_rows('Jenna',1,results)
    remove_elim_rows('Kyle',1,results)
    remove_elim_rows('Savannah',2,results)
    remove_elim_rows('Q',3,results)
    remove_elim_rows('Mike White',4,results)
    remove_elim_rows('Charlie',5,results)
    remove_elim_rows('Angelina',5,results)

    results.to_csv("output.csv", index=False)

    results_pre5 =  results [results['episode'] < 5]

    owner_points = results.groupby(["episode", "owner"])["points"].sum().reset_index()
    player_points = results.groupby(["episode", "player"])["points"].sum().reset_index()

    #Owner Points over time
    owner_points_pivot = owner_points.pivot(index='episode', columns='owner', values='points')
    owner_points_pivot.plot(marker='o')
    plt.title('Owner Points Over Episodes')
    plt.xlabel('Episode')
    plt.ylabel('Points')
    plt.legend(title='Owner')
    plt.grid(True)
    plt.show()

    #Owner Points total 
    total_owner_points = owner_points.groupby('owner')['points'].sum().reset_index()
    plt.bar(total_owner_points['owner'], total_owner_points['points'], color='skyblue')
    plt.title('Total Points per Owner')
    plt.xlabel('Owner')
    plt.ylabel('Total Points')
    plt.xticks(rotation=45)  # rotate owner names if needed
    plt.show()

    total_player_points = player_points.groupby('player')['points'].sum().reset_index()
    plt.bar(total_player_points['player'], total_player_points['points'], color='skyblue')
    plt.title('Total Points per Player')
    plt.xlabel('Player')
    plt.ylabel('Total Points')
    plt.xticks(rotation=45)  # rotate owner names if needed
    plt.show()

        

    
    
    

    


    
    return 0

def find_tribe(player_name, tribes_dict):
    """
    Returns the tribe name for a given player.
    
    Args:
        player_name (str): Name of the player to search for.
        tribes_dict (dict): Dictionary of tribes with player lists as values.
        
    Returns:
        str or None: The tribe name if found, else None.
    """
    return next((tribe for tribe, players in tribes_dict.items() if player_name in players), None)

def remove_elim_rows(playername, epNum, df):
    df = df[~((df['player'] == playername) & (df['episode'] > epNum))]
    df = df[~((df['player'] == "Jenna") & (df['reason'] == "CorrectVote") & (df['episode'] == epNum))]
    return df


# ----------------------------
# Entry Point
# ----------------------------
if __name__ == "__main__":
    main(sys.argv[1:])