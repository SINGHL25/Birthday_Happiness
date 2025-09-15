
#!/usr/bin/env python3
"""
Love Notes Generator for Priya
A sweet collection of personalized love notes and romantic messages
"""

import random
from datetime import datetime
import json

class LoveNotesGenerator:
    def __init__(self):
        self.name = "Priya"
        self.sweet_adjectives = [
            "beautiful", "amazing", "wonderful", "incredible", "stunning",
            "brilliant", "radiant", "extraordinary", "magnificent", "precious",
            "adorable", "charming", "captivating", "enchanting", "lovely"
        ]
        
        self.romantic_phrases = [
            f"Every day with you feels like a dream come true, {self.name}",
            f"Your smile lights up my entire world, {self.name}",
            f"I fall in love with you more each passing day, {self.name}",
            f"You make everything better just by being you, {self.name}",
            f"My heart skips a beat every time I see you, {self.name}",
            f"You are my sunshine on the cloudiest days, {self.name}",
            f"With you, every moment is a precious memory, {self.name}",
            f"You are the poetry my heart has been trying to write, {self.name}",
            f"In your eyes, I see my forever, {self.name}",
            f"You are my favorite hello and hardest goodbye, {self.name}"
        ]
        
        self.daily_affirmations = [
            f"Good morning, {self.name}! You're going to have an amazing day! 🌅",
            f"Remember how incredible you are, {self.name}! ✨",
            f"The world is brighter because you're in it, {self.name}! 🌟",
            f"You've got this, {self.name}! I believe in you always! 💪",
            f"Sending you all my love today, {self.name}! 💕",
            f"You make ordinary moments feel magical, {self.name}! ✨",
            f"Your kindness makes the world a better place, {self.name}! 🌸",
            f"I'm so grateful to have you in my life, {self.name}! 🙏",
            f"You inspire me to be better every day, {self.name}! 🌱",
            f"Sweet dreams, beautiful {self.name}! You're my last thought tonight! 🌙"
        ]
        
        self.special_occasions = {
            "monday": f"Happy Monday, {self.name}! Let's make this week amazing together! 💫",
            "tuesday": f"Tuesday feels perfect because I get to think about you, {self.name}! 💭",
            "wednesday": f"Halfway through the week, but you make every day feel like Friday, {self.name}! 🎉",
            "thursday": f"Thursday thoughts are all about how lucky I am to know you, {self.name}! 🍀",
            "friday": f"Friday is here, but every day is a celebration with you, {self.name}! 🎊",
            "saturday": f"Saturday vibes: relaxing and thinking about my favorite person - you, {self.name}! 😌",
            "sunday": f"Sunday serenity with thoughts of you, {self.name}! Perfect way to end the week! 🕊️"
        }

    def generate_random_love_note(self):
        """Generate a random personalized love note"""
        templates = [
            f"Hey {self.sweet_adjectives[random.randint(0, len(self.sweet_adjectives)-1)]} {self.name}, just wanted to remind you that you're absolutely incredible! 💖",
            f"Thinking of you today, {self.name}, and smiling because you make life so much brighter! ☀️",
            f"Dear {self.name}, you are {self.sweet_adjectives[random.randint(0, len(self.sweet_adjectives)-1)]} in every possible way! 🌹",
            f"Random reminder for {self.name}: You are loved, appreciated, and absolutely amazing! 💕",
            f"To my {self.sweet_adjectives[random.randint(0, len(self.sweet_adjectives)-1)]} {self.name}: Hope your day is as wonderful as you are! 🌺"
        ]
        return random.choice(templates)

    def get_daily_note(self):
        """Get today's special note"""
        today = datetime.now().strftime("%A").lower()
        if today in self.special_occasions:
            return self.special_occasions[today]
        else:
            return random.choice(self.daily_affirmations)

    def create_weekly_notes(self):
        """Generate a week's worth of love notes"""
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        weekly_notes = {}
        
        for day in days:
            note = self.generate_random_love_note()
            romantic_phrase = random.choice(self.romantic_phrases)
            weekly_notes[day] = {
                "sweet_note": note,
                "romantic_message": romantic_phrase,
                "affirmation": random.choice(self.daily_affirmations)
            }
        
        return weekly_notes

    def create_surprise_notes(self, count=10):
        """Create surprise notes for hiding around"""
        surprise_notes = []
        locations = [
            "bathroom mirror", "coffee mug", "car dashboard", "laptop bag",
            "pillow", "wallet", "phone case", "favorite book", "kitchen counter",
            "work desk", "purse", "jacket pocket", "water bottle", "planner"
        ]
        
        for i in range(count):
            note = {
                "location": locations[i % len(locations)],
                "message": self.generate_random_love_note(),
                "bonus": random.choice(self.romantic_phrases)
            }
            surprise_notes.append(note)
        
        return surprise_notes

    def memory_lane_notes(self):
        """Create notes about shared memories and future dreams"""
        memory_notes = [
            f"Remember when we first met? I knew {self.name} was special from day one! 💫",
            f"Every adventure with you, {self.name}, becomes my favorite memory! 🗺️",
            f"I love how we laugh together, {self.name}. Your joy is contagious! 😄",
            f"All our inside jokes make me smile, {self.name}. We have the best conversations! 💬",
            f"I can't wait to make more beautiful memories with you, {self.name}! 📸",
            f"Our future looks so bright together, {self.name}! ✨",
            f"Every shared sunset with you, {self.name}, feels like magic! 🌅",
            f"I love our quiet moments together, {self.name}. Peace feels like home with you! 🏠"
        ]
        return memory_notes

    def celebration_notes(self):
        """Special notes for celebrations"""
        celebration_messages = [
            f"Celebrating you today and always, {self.name}! You deserve all the happiness! 🎉",
            f"Every day is worth celebrating because you're in the world, {self.name}! 🎊",
            f"Here's to another year of your amazing presence, {self.name}! 🥂",
            f"Celebrating the incredible person you are, {self.name}! 🎈",
            f"You make every celebration more special, {self.name}! 🎂",
            f"Today we celebrate you, {self.name}, and all the joy you bring! 🌟"
        ]
        return celebration_messages

    def save_notes_to_file(self, filename="priya_love_notes.json"):
        """Save all generated notes to a file"""
        all_notes = {
            "generated_date": datetime.now().isoformat(),
            "for": self.name,
            "daily_notes": self.create_weekly_notes(),
            "surprise_notes": self.create_surprise_notes(),
            "memory_notes": self.memory_lane_notes(),
            "celebration_notes": self.celebration_notes(),
            "random_phrases": self.romantic_phrases
        }
        
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(all_notes, file, indent=2, ensure_ascii=False)
        
        print(f"💕 Love notes saved to {filename}")
        return all_notes

def main():
    """Main function to demonstrate the love notes generator"""
    print("💖 Love Notes Generator for Priya 💖")
    print("=" * 40)
    
    love_notes = LoveNotesGenerator()
    
    # Generate today's note
    print("\n🌟 Today's Special Note:")
    print(love_notes.get_daily_note())
    
    # Generate a random love note
    print("\n💕 Random Love Note:")
    print(love_notes.generate_random_love_note())
    
    # Show a romantic phrase
    print("\n🌹 Romantic Message:")
    print(random.choice(love_notes.romantic_phrases))
    
    # Generate weekly notes
    print("\n📅 This Week's Love Notes:")
    weekly = love_notes.create_weekly_notes()
    for day, notes in weekly.items():
        print(f"\n{day}:")
        print(f"  💫 {notes['sweet_note']}")
    
    # Generate surprise notes
    print("\n🎁 Surprise Notes (for hiding around):")
    surprises = love_notes.create_surprise_notes(5)
    for i, note in enumerate(surprises, 1):
        print(f"\n{i}. Location: {note['location']}")
        print(f"   Message: {note['message']}")
    
    # Save everything to file
    print("\n💾 Saving all notes...")
    love_notes.save_notes_to_file()
    
    print(f"\n✨ All done! Spread the love to {love_notes.name}! ✨")

if __name__ == "__main__":
    main()
