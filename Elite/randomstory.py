import random

def generate_story():
    characters = ["Baahubali", "Sita", "Pushpa", "Arjun Reddy", "Raju"]
    settings = ["the ancient city of Amaravati", "the bustling streets of Hyderabad", "the serene Godavari riverbank", "the dense Nallamala forest", "the mystical Tirupati hills"]
    goals = ["restore peace to the land", "avenge a loved one", "conquer their fears", "unite divided clans", "protect a sacred artifact"]
    obstacles = ["an army of invaders", "a devious spy", "a curse from an ancient deity", "an unexpected betrayal", "a fierce beast guarding the way"]
    endings = ["find a new purpose", "achieve legendary status", "forge an unbreakable bond", "uncover a hidden truth", "change the course of history"]

    character = random.choice(characters)
    setting = random.choice(settings)
    goal = random.choice(goals)
    obstacle = random.choice(obstacles)
    ending = random.choice(endings)

    story = (
        f"In a time of turmoil, {character} ventured into {setting}. Their quest was to {goal}. "
        f"However, their path was fraught with danger, as they faced {obstacle}. "
        f"Through resilience and courage, they ultimately managed to {ending}, leaving a lasting legacy."
    )

    return story
if __name__ == "__main__":
    print(generate_story())
