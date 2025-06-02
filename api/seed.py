from sqlalchemy.orm import Session
from models import Phrase
from database import SessionLocal
import random

# Common English phrases (limited to max 2 words and approx. 500 total, >= 70% single words <= 15 characters)
phrases = [
    # Single words (expanded list, <= 15 characters)
    "apple", "banana", "cherry", "garden", "nature", "ocean", "peace", "wisdom", "yellow", "zebra",
    "ability", "absence", "academy", "account", "achieve", "acquire", "address", "advance",
    "advisor", "against", "airline", "airport", "alcohol", "already", "analyst", "ancient",
    "another", "anxiety", "anybody", "anymore", "approve", "arrange", "arrival", "article",
    "artwork", "athlete", "attempt", "attract", "auction", "authority", "average", "balance",
    "bargain", "barrier", "battery", "believe", "beneath", "benefit", "biology", "blanket",
    "boundary", "briefly", "brother", "burglar", "cabinet", "capture", "carrier", "caution",
    "ceiling", "central", "century", "certain", "chamber", "channel", "chapter", "charity",
    "chemist", "clarify", "climate", "collect", "combine", "comfort", "command", "comment",
    "company", "compare", "compete", "complex", "connect", "consider", "consist", "contact",
    "contain", "contest", "context", "control", "convert", "correct", "council", "country",
    "courage", "crystal", "culture", "curious", "current", "custody", "declare", "default",
    "defense", "deflect", "deliver", "density", "deposit", "despite", "destroy", "develop",
    "diamond", "digital", "diploma", "dispute", "distant", "disturb", "divided", "dolphin",
    "economy", "edition", "educate", "elegant", "element", "embrace", "emotion", "enhance",
    "enquire", "essence", "ethical", "evident", "examine", "example", "excited", "execute",
    "expense", "explore", "express", "extend", "extreme", "factory", "faculty", "fantasy",
    "fashion", "feature", "federal", "fiction", "fifteen", "fighter", "finance", "finding",
    "fishing", "fitness", "fixture", "florist", "forever", "fortune", "founder", "freedom",
    "friendly", "fulfill", "gateway", "general", "genesis", "genuine", "giraffe", "glimpse",
    "graphic", "gravity", "grocery", "guarantee", "guardian", "habitat", "handful", "handler",
    "happily", "harvest", "heading", "healthy", "hearsay", "heating", "heavily", "helpful",
    "helpful", "herself", "highway", "himself", "history", "holiday", "homeless", "horizon",
    "however", "hundred", "hunting", "imagine", "immediately", "improve", "include", "initial",
    "inspire", "install", "instead", "intense", "interact", "invoice", "involve", "journal",
    "journey", "justice", "justify", "keyword", "kindness", "kingdom", "kitchen", "lateral",
    "laughter", "leading", "leaflet", "leather", "leaving", "legally", "legend", "leisure",
    "liberal", "library", "license", "limited", "listing", "literal", "loyalty", "machine",
    "manager", "mankind", "marital", "massive", "master", "material", "maximum", "meaning",
    "measure", "medical", "medium", "mention", "message", "mineral", "minimum", "mission",
    "mistake", "mixture", "mobile", "modest", "modify", "moment", "monitor", "morning",
    "motel", "mother", "motion", "moving", "myself", "nation", "native", "natural",
    "nearly", "neglect", "neither", "nervous", "network", "neutral", "namely", "ninety",
    "normal", "notice", "novelist", "nuclear", "nursery", "obvious", "offense", "officer",
    "opening", "operate", "opinion", "optical", "organic", "outcome", "outline", "outside",
    "package", "painter", "parking", "partner", "passage", "passion", "patient", "pattern",
    "payment", "penalty", "perfect", "perform", "perhaps", "permits", "persuade", "picture",
    "pioneer", "plastic", "poetical", "portion", "posture", "poverty", "precise", "predict",
    "premier", "prepare", "present", "prevent", "primary", "printer", "privacy", "private",
    "problem", "proceed", "process", "produce", "program", "project", "promote", "protest",
    "provide", "province", "publish", "purpose", "quality", "quarter", "radical", "railway",
    "readily", "reality", "receive", "recover", "reflect", "regular", "related", "release",
    "remain", "removal", "require", "reserve", "resolve", "respect", "respond", "restore",
    "retired", "revenue", "reverse", "roughly", "routine", "running", "satisfy", "schedule",
    "science", "scratch", "seating", "section", "segment", "selfish", "serious", "service",
    "setting", "seventh", "several", "shallow", "sharing", "shelter", "shortly", "showing",
    "silence", "singing", "skilled", "slavery", "sleeper", "smoking", "society", "somehow",
    "someone", "speaker", "special", "species", "sponsor", "station", "storage", "strange",
    "stretch", "student", "subject", "succeed", "suggest", "summary", "support", "surely",
    "surface", "surgery", "survive", "suspect", "sustain", "teacher", "tension", "testing",
    "theater", "therapy", "thereby", "thought", "through", "tobacco", "tonight", "totally",
    "towards", "traffic", "trainer", "trouble", "typical", "unhappy", "uniform", "unknown",
    "unusual", "utility", "variety", "vehicle", "venture", "version", "veteran", "victory",
    "village", "violent", "visible", "visitor", "visual", "vitamin", "volume", "warning",
    "weakness", "wealthy", "weekend", "welcome", "welfare", "whoever", "whomever", "widely",
    "willing", "winning", "written", "yourself",

    # Two-word phrases (filtered for total chars <= 25)
    "blue sky", "cold water", "dark night", "fresh air", "golden sun",
    "happy days", "inner peace", "jumping joy", "kind heart", "loving care", "mighty river",
    "open door", "quiet night", "sweet dreams", "under stars",
    "zesty lemon",
    "have fun", "be kind", "thank again", "well play", "my turn",
    "your turn", "good try", "nice shot", "big win", "small win",
    "red ball", "blue car", "green tree", "tall building", "short story",
    "long day", "hot sun", "cold wind", "new house", "old house",
    "fast car", "slow car", "happy face", "sad face", "big dog",
    "small cat", "wild animal", "pet animal", "loud music", "quiet music",
    "bright light", "dark shadow", "high mountain", "low valley", "deep water",
    "shallow water", "clean room", "dirty room", "hard work", "easy work",
    "new book", "old book", "hot tea", "cold tea", "warm milk",
    "cold milk", "big apple", "small banana", "red cherry", "green grape"
]

def seed_database(session: Session, num_phrases: int = 1000):
    # Create phrases from the curated list
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
