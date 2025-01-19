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
IMMERSITY_API_KEY = "your_immersity_api_key"
PINOKIO_API_KEY = "your_pinokio_api_key"

def generate_game_storyline(theme, main_character, world_setting):
    """
    Uses ChatGPT to generate a fantasy game storyline.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Write a compelling fantasy game storyline with the theme '{theme}', featuring '{main_character}' as the hero. "
              f"Set the story in a world called '{world_setting}' and include an epic conflict.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create visuals for the game scenes and characters.
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
    Uses Runway to create a cinematic video for a game intro scene.
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

def generate_narration(script):
    """
    Uses ElevenLabs to create dramatic narration for the game intro.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": script, "voice": "James", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to generate epic background music for the game intro.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_dynamic_effects(video_url):
    """
    Uses Immersity AI to enhance the video with cinematic motion effects.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "dramatic-motion"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_avatar_intro(character_name, narration):
    """
    Uses HeyGen to create a talking avatar for character introduction.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": f"Character Intro: {character_name}",
        "narration": narration,
        "avatar": "hero-avatar"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a fantasy game intro video.
    """
    print("Welcome to the AI-Powered Fantasy Game Intro Creator!")

    # User Input
    theme = input("Enter the game theme (e.g., 'Heroic Quest', 'Dark Magic'): ").strip()
    main_character = input("Enter the main character's name: ").strip()
    world_setting = input("Enter the name of the game world: ").strip()

    # Generate Storyline and Script
    print("\nGenerating game storyline and intro script...")
    game_storyline = generate_game_storyline(theme, main_character, world_setting)
    print(f"\nGame Storyline:\n{game_storyline}")

    # Split storyline into scenes
    scenes = game_storyline.split("\n\n")
    video_urls = []

    for i, scene in enumerate(scenes, start=1):
        print(f"\nProcessing Scene {i}...")

        # Generate visuals
        print("Generating visuals for the scene...")
        visual_description = f"{scene} - fantasy style."
        visual_url = generate_visual(visual_description)
        upscaled_visual_url = upscale_visual(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration
        print("Creating narration for the scene...")
        narration_audio = generate_narration(scene)
        print(f"Narration Audio URL: {narration_audio}")

        # Create video
        print("Creating cinematic video for the scene...")
        video_url = create_video(f"Scene {i}", narration_audio, upscaled_visual_url)
        enhanced_video_url = add_dynamic_effects(video_url)
        print(f"Enhanced Video URL: {enhanced_video_url}")
        video_urls.append(enhanced_video_url)

    # Generate music
    print("\nGenerating epic background music...")
    music_url = generate_music("epic")
    print(f"Background Music URL: {music_url}")

    print("\nFantasy Game Intro Completed!")
    print("Generated Videos:")
    for video in video_urls:
        print(f"- {video}")

if __name__ == "__main__":
    main()
""" Example Output
Theme: Dark Magic
Main Character: Lyra, the Shadowborn
World Setting: Eldoria
Generated Fantasy Game Intro:

Cinematic videos for each story scene with visuals, narration, and music.
Personalized character avatar introducing Lyra.
Dynamic motion effects for an epic, immersive experience. """