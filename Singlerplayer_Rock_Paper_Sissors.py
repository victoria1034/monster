import random

def main():
    # Score
    total_match = 0
    player_wins = 0
    ai_wins = 0
    ties = 0

    # Keep track of the player inputs
    player_last_choice = ""
    player_past_choices = []
    did_player_won = False
    ai_last_choice = ["Roche", "Papier", "Ciseau"][random.randint(0, 2)]

    # Main game loop
    while True:
        # Get player input
        while True:
            player_choice = input("Roche, Papier, Ciseau: ")

            # Allow some flexibility with the inputs
            if player_choice in ["roche", "r", "R"]:
                player_choice = "Roche"
            if player_choice in ["papier", "p", "P"]:
                player_choice = "Papier"
            if player_choice in ["ciseau", "c", "C"]:
                player_choice = "Ciseau"

            # Check if player input is valid
            if player_choice in ["Roche", "Papier", "Ciseau"]:
                break
            else:
                print("IT WAS A MISS INPUT")
        print(ascii_player[player_choice])
        
        # AI
        ai_choice = ["Roche", "Papier", "Ciseau"][random.randint(0, 2)]

        # Take what will beat the option that is most likely to be used by the player
        if player_past_choices:
            ai_choice = player_past_choices[random.randint(0, len(player_past_choices) - 1)]
            if ai_choice == "Roche":
                ai_choice = "Papier"
            elif ai_choice == "Papier":
                ai_choice = "Ciseau"
            elif ai_choice == "Ciseau":
                ai_choice = "Roche"

        # Counters the player if they won
        if did_player_won:
            if player_last_choice == "Roche":
                ai_choice = "Papier"
            if player_last_choice == "Papier":
                ai_choice = "Ciseau"
            if player_last_choice == "Ciseau":
                ai_choice = "Roche"

        # Change option to prevent the player to counter
        elif not did_player_won:
            if ai_last_choice == "Roche":
                ai_choice = "Papier"
            elif ai_last_choice == "Papier":
                ai_choice = "Ciseau"
            elif ai_last_choice == "Ciseau":
                ai_choice = "Roche"

        # straight up ceahting
        # if player_choice == "Roche":
        #     ai_choice = "Papier"
        # if player_choice == "Papier":
        #     ai_choice = "Ciseau"
        # if player_choice == "Ciseau":
        #     ai_choice = "Roche"

        print(f"L'IA choisi {ai_choice}")

        print(ascii_ai[ai_choice])
        
        # Game logic
        # Check for a tie
        if player_choice == ai_choice:
            print("Match nul")
            ties += 1
            did_player_won = False
        else:
            # Check if the player won
            if player_choice == "Roche" and ai_choice == "Ciseau" or \
               player_choice == "Papier" and ai_choice == "Roche" or \
               player_choice == "Ciseau" and ai_choice == "Papier":
                print("Le Joueur gagne")
                player_wins += 1
                did_player_won = True
            # If not, the AI won
            else:
                print("L'IA gagne")
                ai_wins += 1
                did_player_won = False

        # Keep track of the player inputs
        player_last_choice = player_choice
        player_past_choices.append(player_choice)

        # Keep track of match
        total_match += 1

        # After 10 match annonce who won the most
        if total_match == 10:
            print(f"{player_wins = }")
            print(f"{ai_wins = }")
            print(f"{ties = }")
            if ai_wins == player_wins:
                print("Nul")
            elif ai_wins > player_wins:
                print("L'IA a gagner")
            else:
                print("Tu as gagner")


ascii_player = {"Roche": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
                "Papier": """
    ________
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
                "Ciseau": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""}


ascii_ai = {"Roche": """
                     _______
                    (____   '---
                   (_____)
                   (_____)
                    (____)
                     (___)__.---
""",
            "Papier": """
                        ________
                    ___(____    '---
                   (______
                   (_______
                    (_______
                     (__________.---
"""
            , "Ciseau": """
                         _______
                    ____(____   '---
                   (______
                   (__________
                        (____)
                         (___)__.---
"""}

main()
