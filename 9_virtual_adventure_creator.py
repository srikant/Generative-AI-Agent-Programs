import openai
import requests

# API keys (replace with your actual keys)
OPENAI_API_KEY = "your_openai_api_key"
KREA_API_KEY = "your_krea_api_key"
MAGNIFIC_API_KEY = "your_magnific_api_key"
RUNWAY_API_KEY = "your_runway_api_key"
ELEVENLABS_API_KEY = "your_elevenlabs_api_key"
ARTLIST_API_KEY = "your_artlist_api_key"
HEYGEN_API_KEY = "your_heygen_api_key"
SUNO_API_KEY = "your_suno_api_key"
IMMERSITY_API_KEY = "your_immersity_ai_key"
PINOKIO_API_KEY = "your_pinokio_api_key"

def generate_adventure_story(adventure_type, main_objective, setting):
    """
    Uses ChatGPT to create a detailed adventure storyline.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Write a detailed virtual adventure storyline for a '{adventure_type}' adventure. "
              f"The main objective is '{main_objective}'. The setting is '{setting}'. "
              f"Include NPC roles, missions, and key scenes.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to generate visuals for the adventure scenes.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def upscale_visual(image_url):
    """
    Uses Magnific to upscale visuals for cinematic quality.
    """
    url = "https://api.magnific.ai/v1/upscale"
    headers = {"Authorization": f"Bearer {MAGNIFIC_API_KEY}"}
    payload = {"image_url": image_url}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["upscaled_image_url"]

def create_video(scene_title, narration, visual_url):
    """
    Uses Runway to create a cinematic video for an adventure scene.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": scene_title,
        "text": narration,
        "image_url": visual_url,
        "style": "cinematic"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def generate_narration(text):
    """
    Uses ElevenLabs to narrate the adventure.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Alex", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create music for the adventure.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_dynamic_effects(video_url):
    """
    Uses Immersity AI to add cinematic motion effects.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "cinematic-motion"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_npc_avatar(character_name, narration):
    """
    Uses HeyGen to create an NPC avatar with dialogue.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": f"{character_name} Introduction",
        "narration": narration,
        "avatar": "adventurer-npc"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a virtual adventure.
    """
    print("Welcome to the AI-Powered Virtual Adventure Creator!")

    # User Inputs
    adventure_type = input("Enter the type of adventure (e.g., Treasure Hunt, Space Exploration): ").strip()
    main_objective = input("Enter the main objective of the adventure: ").strip()
    setting = input("Enter the setting of the adventure (e.g., Jungle, Mars, Ancient City): ").strip()

    # Generate Adventure Story
    print("\nGenerating adventure storyline...")
    adventure_story = generate_adventure_story(adventure_type, main_objective, setting)
    print(f"\nAdventure Storyline:\n{adventure_story}")

    # Split storyline into scenes
    scenes = adventure_story.split("\n\n")
    video_urls = []

    for i, scene in enumerate(scenes, start=1):
        print(f"\nProcessing Scene {i}...")

        # Generate visuals
        print("Generating visuals for the scene...")
        visual_description = f"{scene} - fantasy adventure style."
        visual_url = generate_visual(visual_description)
        upscaled_visual_url = upscale_visual(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration
        print("Creating narration for the scene...")
        narration_audio = generate_narration(scene)
        print(f"Narration Audio URL: {narration_audio}")

        # Create video
        print("Creating cinematic video for the scene...")
        video_url = create_video(f"Scene {i}: Adventure", narration_audio, upscaled_visual_url)
        enhanced_video_url = add_dynamic_effects(video_url)
        print(f"Enhanced Video URL: {enhanced_video_url}")
        video_urls.append(enhanced_video_url)

    # Generate NPC avatar
    print("\nCreating NPC introduction...")
    npc_name = "Guide of the Journey"
    npc_intro_text = "Welcome to your adventure. I will guide you through the challenges ahead."
    npc_avatar_url = create_npc_avatar(npc_name, npc_intro_text)
    print(f"NPC Avatar Video URL: {npc_avatar_url}")

    print("\nVirtual Adventure Created!")
    print("Generated Videos:")
    for video in video_urls:
        print(f"- {video}")
    print(f"NPC Introduction Video: {npc_avatar_url}")

if __name__ == "__main__":
    main()
""" Example Output
Adventure Type: Treasure Hunt
Main Objective: Find the Lost Crown of Atlantis
Setting: An Ancient Underwater City

Generated Virtual Adventure:

Intro Scene: NPC guide introduces the adventure.
Cinematic Scenes: Key moments narrated with dynamic visuals and soundtracks.
Immersive Soundscape: Background music matches the suspenseful, adventurous tone. """