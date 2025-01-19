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
PINOKIO_API_KEY = "your_pinokio_api_key"
IMMERSITY_API_KEY = "your_immersity_api_key"

def generate_story(theme, main_character, plot):
    """
    Uses ChatGPT to generate a story script.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Write a short story with the theme '{theme}', featuring '{main_character}' as the main character. "
              f"The plot is: {plot}. Include dialogues and scene descriptions.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to generate visuals for the story scenes and characters.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def upscale_visual(image_url):
    """
    Uses Magnific to upscale visuals.
    """
    url = "https://api.magnific.ai/v1/upscale"
    headers = {"Authorization": f"Bearer {MAGNIFIC_API_KEY}"}
    payload = {"image_url": image_url}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["upscaled_image_url"]

def generate_narration(script):
    """
    Uses ElevenLabs to generate narration audio for the story.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": script, "voice": "Clara", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def create_animated_scene(image_url, narration, scene_description):
    """
    Uses Runway to create animated video scenes.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": scene_description,
        "text": narration,
        "image_url": image_url,
        "style": "cinematic"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def add_background_music(mood):
    """
    Uses Suno to generate background music based on the story's mood.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_dynamic_effects(video_url):
    """
    Uses Immersity AI to add motion effects.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "cinematic"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def main():
    """
    Main function to run the Animated Story Creator.
    """
    print("Welcome to the AI-Powered Animated Story Creator!")

    # User Input
    theme = input("Enter the story theme (e.g., Adventure, Mystery): ").strip()
    main_character = input("Enter the main character (e.g., a young wizard, a brave explorer): ").strip()
    plot = input("Enter a brief plot outline: ").strip()

    # Generate Story
    print("\nGenerating story script...")
    story_script = generate_story(theme, main_character, plot)
    print(f"Story Script:\n{story_script}")

    # Split story into scenes
    scenes = story_script.split("\n\n")
    animated_videos = []

    for i, scene in enumerate(scenes, start=1):
        print(f"\nProcessing Scene {i}...")

        # Generate visual for the scene
        print("Generating scene visual...")
        visual_description = f"{scene} in the style of {theme}."
        image_url = generate_visual(visual_description)
        upscaled_image_url = upscale_visual(image_url)
        print(f"Upscaled Image URL: {upscaled_image_url}")

        # Generate narration
        print("Generating narration audio...")
        narration_audio = generate_narration(scene)
        print(f"Narration Audio URL: {narration_audio}")

        # Create animated scene
        print("Creating animated scene...")
        video_url = create_animated_scene(upscaled_image_url, narration_audio, f"Scene {i}")
        enhanced_video_url = add_dynamic_effects(video_url)
        print(f"Enhanced Video URL: {enhanced_video_url}")
        animated_videos.append(enhanced_video_url)

    # Add music
    print("\nAdding background music...")
    music_url = add_background_music("adventurous")
    print(f"Background Music URL: {music_url}")

    print("\nAnimated Story Completed!")
    print("Generated Videos:")
    for video in animated_videos:
        print(f"- {video}")

if __name__ == "__main__":
    main()
""" Output Example:
Theme: Adventure
Main Character: A curious archaeologist
Plot: "Explores a lost temple to uncover an ancient secret."

Final Output:

Animated Video Scenes: Each scene features visuals, narration, and motion effects.
Music and Sound: Background music enhances immersion.
Story Highlights: Narrated scenes with cinematic effects and transitions. """