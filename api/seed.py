from sqlalchemy.orm import Session
from models import Phrase
from database import SessionLocal
import random

# Common English phrases
phrases = [
    # Single words
    "apple", "banana", "cherry", "dolphin", "elephant", "freedom", "garden", "happiness",
    "imagine", "journey", "kindness", "laughter", "mountain", "nature", "ocean", "peace",
    "quality", "rainbow", "sunshine", "treasure", "umbrella", "victory", "wisdom", "xylophone",
    "yellow", "zebra",

    # Two-word phrases
    "blue sky", "cold water", "dark night", "early morning", "fresh air", "golden sun",
    "happy days", "inner peace", "jumping joy", "kind heart", "loving care", "mighty river",
    "northern lights", "open door", "perfect day", "quiet night", "running water", "sweet dreams",
    "tropical breeze", "under stars", "vibrant colors", "warm sunshine", "yellow flowers",
    "zesty lemon",

    # Three-word phrases
    "a beautiful day", "birds in flight", "clouds in sky", "dancing in rain", "early morning walk",
    "fresh morning air", "gentle summer breeze", "happy little moments", "in the garden",
    "jumping for joy", "kind and gentle", "laughing out loud", "morning coffee time",
    "nature's sweet song", "ocean waves crashing", "peaceful mountain view", "quiet country road",
    "running through fields", "sunset on beach", "trees in wind", "under starry night",
    "vibrant autumn colors", "walking in sunshine", "yellow daffodils bloom",
    "zephyr through trees",

    # Common expressions
    "good morning", "thank you", "see you later", "have a nice day", "good night",
    "happy birthday", "merry christmas", "happy new year", "welcome home", "take care",
    "best wishes", "good luck", "well done", "nice to meet you", "how are you",
    "excuse me", "i'm sorry", "you're welcome", "good afternoon", "good evening",

    # Nature phrases
    "autumn leaves falling", "birds singing sweetly", "crystal clear water", "dawn breaking",
    "evening stars twinkle", "forest path winding", "gentle rain falling",
    "island paradise", "jungle sounds", "lake reflecting sky", "mountain peak high",
    "northern lights dance", "ocean waves rolling", "pine trees swaying", "quiet forest stream",
    "river flowing gently", "sunset colors painting", "tropical breeze blowing",
    "valley of flowers", "waterfall cascading", "yellow leaves falling",

    # Action phrases
    "dancing in moonlight", "flying through clouds", "jumping over puddles", "running in rain",
    "swimming in ocean", "walking through forest", "climbing mountains", "sailing on waves",
    "skiing down slopes", "surfing the waves", "hiking through woods", "biking along path",
    "fishing in lake", "camping under stars", "exploring caves", "gardening in sunshine",
    "painting landscapes", "photographing nature", "stargazing at night", "bird watching",

    # Descriptive phrases
    "bright morning sun", "cool evening breeze", "deep blue ocean", "early spring flowers",
    "fresh mountain air", "golden autumn leaves", "high mountain peaks", "icy winter morning",
    "jeweled night sky", "kind gentle soul", "lush green forest", "majestic mountain range",
    "northern star shining", "peaceful country road", "quiet mountain lake", "rustling autumn leaves",
    "sweet summer rain", "tropical paradise", "under starry sky", "vibrant spring colors",
    "warm summer night", "yellow daffodils bloom"
]

def seed_database(session: Session, num_phrases: int = 1000):
    # Create phrases
    selected_phrases = random.sample(phrases, min(num_phrases, len(phrases)))
    phrase_objects = [Phrase(phrase=phrase) for phrase in selected_phrases]

    # Add to database
    session.add_all(phrase_objects)
    session.commit()

if __name__ == "__main__":
    # Create database session
    session = SessionLocal()

    try:
        # Seed the database
        seed_database(session)
        print("Database seeded successfully!")
    finally:
        session.close()
