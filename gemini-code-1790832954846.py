import pyttsx3

engine = pyttsx3.init()

# 1. Fetch available system voices
voices = engine.getProperty('voices')

for index, voice in enumerate(voices):
    print(f"Index: {index} | Name: {voice.name} | ID: {voice.id}")

# 2. Select a specific voice (e.g., index 0 for male, index 1 for female)
engine.setProperty('voice', voices[1].id)

# 3. Optional adjustments
engine.setProperty('rate', 145)   # Speed (words per minute)
engine.setProperty('volume', 1.0) # Volume (0.0 to 1.0)

# 4. Synthesize speech
engine.say("Space exploration has entered a transformative era driven by technological innovation and private enterprise. For decades, space travel was the exclusive domain of major national agencies with massive budgets. Today, reusable rocket technology has drastically lowered the cost of reaching orbit, enabling commercial satellite deployments, deep-space probes, and ambitious human spaceflight missions to become routine occurrences.")
engine.runAndWait()

