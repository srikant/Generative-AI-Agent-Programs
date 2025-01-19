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

def generate_comic_storyline(genre, main_character, setting):
    """
    Uses ChatGPT to create a comic storyline with panel descriptions.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Write a detailed storyline for a comic in the '{genre}' genre. "
              f"The main character is '{main_character}', and the setting is '{setting}'. "
              f"Include panel descriptions, character dialogues, and an engaging plot.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create visuals for the comic panels.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def upscale_visual(image_url):
    """
    Uses Magnific to upscale visuals for high-resolution panels.
    """
    url = "https://api.magnific.ai/v1/upscale"
    headers = {"Authorization": f"Bearer {MAGNIFIC_API_KEY}"}
    payload = {"image_url": image_url}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["upscaled_image_url"]

def create_motion_panel(panel_title, narration, visual_url):
    """
    Uses Runway to create a motion comic panel.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": panel_title,
        "text": narration,
        "image_url": visual_url,
        "style": "comic"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def generate_narration(text):
    """
    Uses ElevenLabs to narrate comic dialogues or story.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Emma", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create music for the comic.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_dynamic_effects(video_url):
    """
    Uses Immersity AI to add cinematic motion effects to panels.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "comic-motion"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_character_avatar(character_name, narration):
    """
    Uses HeyGen to create a talking avatar for a comic character.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": f"{character_name} Avatar",
        "narration": narration,
        "avatar": "comic-hero"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a personalized comic book.
    """
    print("Welcome to the AI-Powered Comic Creator!")

    # User Inputs
    genre = input("Enter the comic genre (e.g., Superhero, Fantasy, Sci-Fi): ").strip()
    main_character = input("Enter the main character's name: ").strip()
    setting = input("Enter the setting of the comic (e.g., Metropolis, Space Station): ").strip()

    # Generate Comic Storyline
    print("\nGenerating comic storyline...")
    comic_storyline = generate_comic_storyline(genre, main_character, setting)
    print(f"\nComic Storyline:\n{comic_storyline}")

    # Split storyline into panels
    panels = comic_storyline.split("\n\n")
    panel_videos = []

    for i, panel in enumerate(panels, start=1):
        print(f"\nProcessing Panel {i}...")

        # Generate visuals
        print("Generating visuals for the panel...")
        visual_description = f"{panel} - comic style illustration."
        visual_url = generate_visual(visual_description)
        upscaled_visual_url = upscale_visual(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration
        print("Creating narration for the panel...")
        narration_audio = generate_narration(panel)
        print(f"Narration Audio URL: {narration_audio}")

        # Create motion panel
        print("Creating motion panel...")
        video_url = create_motion_panel(f"Panel {i}: {genre}", narration_audio, upscaled_visual_url)
        enhanced_video_url = add_dynamic_effects(video_url)
        print(f"Enhanced Panel Video URL: {enhanced_video_url}")
        panel_videos.append(enhanced_video_url)

    print("\nComic Book Creation Complete!")
    print("Generated Panels:")
    for video in panel_videos:
        print(f"- {video}")

if __name__ == "__main__":
    main()
""" Example Output
Genre: Superhero
Main Character: Nova, the Galactic Defender
Setting: A futuristic metropolis under siege

Generated Comic Book:

Panels: Each story panel includes visuals, narration, and animated motion effects.
Music: Background scores enhance the atmosphere (e.g., heroic, suspenseful).
Character Avatars: Nova introduces her mission with dialogue. """