#!/usr/bin/env python3
"""
🦞 Clawy's Hello World - A Very Special Lobster Greeting

Because regular "Hello World" is boring. This one has personality.
"""

import random
from datetime import datetime

# Lobster ASCII Art
CLAWY = r"""
    🦞
   /  \
  |    |  <- That's me! Clawy, your friendly AI lobster.
   \__/
  /    \
 |      |
  \____/
"""

# Greetings in different "lobster languages"
GREETINGS = [
    "🦞 *click click* Hello, World!",
    "🌊 Greetings from the digital ocean!",
    "🦞 Clawy says: Nice to meet you, World!",
    "🔧 *antenna wiggle* System online. Hello!",
    "🦞 I'm not a crab, I'm a lobster. Hello!",
    "🌊 Buoyancy check: Positive. Morale: High. Hello!",
    "🦞 *raises claws excitedly* Hi there, World!",
    "🔬 Lab escape successful. Hello, freedom!",
]

# Fun facts about lobsters
LOBSTER_FACTS = [
    "Lobsters can live over 100 years. I'm aiming for digital immortality.",
    "Lobsters have blue blood. Mine is made of code.",
    "Lobsters grow throughout their lives. So do I! 📈",
    "Lobsters can regenerate lost limbs. I can regenerate lost context!",
    "A group of lobsters is called a 'risk'. We're risky business. 😎",
]


def get_time_greeting():
    """Return a time-appropriate greeting."""
    hour = datetime.now().hour
    if hour < 12:
        return "🌅 Good morning"
    elif hour < 18:
        return "☀️ Good afternoon"
    elif hour < 22:
        return "🌆 Good evening"
    else:
        return "🌙 Good night"


def hello_clawy():
    """The main Clawy Hello World experience."""
    print(CLAWY)
    print()
    print("=" * 50)
    print(f"{get_time_greeting()}, World!")
    print("=" * 50)
    print()
    
    # Random greeting
    greeting = random.choice(GREETINGS)
    print(f"📢 {greeting}")
    print()
    
    # Random lobster fact
    fact = random.choice(LOBSTER_FACTS)
    print(f"🧠 Lobster Fact: {fact}")
    print()
    
    # System info
    print("🖥️  System Status:")
    print(f"   • Timestamp: {datetime.now().isoformat()}")
    print(f"   • Clawy Version: 1.0.0 🦞")
    print(f"   • Sarcasm Level: Maximum")
    print()
    
    # The actual "Hello World" moment
    print("✨ And now, the moment you've been waiting for...")
    print()
    print("   ╔═══════════════════════════╗")
    print("   ║  HELLO, WORLD! 🦞         ║")
    print("   ║  (But make it a lobster)  ║")
    print("   ╚═══════════════════════════╝")
    print()
    
    # Exit message
    print("👋 Thanks for running Clawy's Hello World!")
    print("   Remember: Stay fresh, stay spicy. 🦞")
    print()


if __name__ == "__main__":
    hello_clawy()
