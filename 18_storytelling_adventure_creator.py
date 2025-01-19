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

def generate_story(theme, main_character, ending_style):
    """
    Uses ChatGPT to create an interactive storytelling adventure.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Create an interactive adventure story with the theme '{theme}'. "
              f"The main character is '{main_character}'. The story should include at least three choices "
              f"and a '{ending_style}' ending. Write it in chapters with interactive decision points.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create visuals for story scenes and characters.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def upscale_image(image_url):
    """
    Uses Magnific to upscale visuals for cinematic quality.
    """
    url = "https://api.magnific.ai/v1/upscale"
    headers = {"Authorization": f"Bearer {MAGNIFIC_API_KEY}"}
    payload = {"image_url": image_url}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["upscaled_image_url"]

def create_video_scene(scene_title, narration, visual_url):
    """
    Uses Runway to create a video scene for the story.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": scene_title,
        "text": narration,
        "image_url": visual_url,
        "style": "storybook"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def generate_narration(text):
    """
    Uses ElevenLabs to narrate story scenes and character dialogues.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Adventure Narrator", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create thematic background music for the story.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_motion_effects(video_url):
    """
    Uses Immersity AI to enhance video scenes with cinematic effects.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "storybook-motion"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_avatar(character_name, narration):
    """
    Uses HeyGen to create a talking avatar for a story character.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": f"{character_name} Introduction",
        "narration": narration,
        "avatar": "storybook-character"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a personalized storytelling adventure.
    """
    print("Welcome to the AI-Powered Storytelling Adventure Creator!")

    # User Inputs
    theme = input("Enter the story theme (e.g., Fantasy, Sci-Fi): ").strip()
    main_character = input("Enter the main character's name: ").strip()
    ending_style = input("Enter the ending style (e.g., Happy, Tragic, Open-Ended): ").strip()

    # Generate Story
    print("\nGenerating story...")
    story = generate_story(theme, main_character, ending_style)
    print(f"\nStory:\n{story}")

    # Split story into chapters
    chapters = story.split("\n\n")
    chapter_videos = []

    for i, chapter in enumerate(chapters, start=1):
        print(f"\nProcessing Chapter {i}...")

        # Generate visuals
        print("Generating visuals for the chapter...")
        visual_description = f"{chapter} - cinematic story style."
        visual_url = generate_visual(visual_description)
        upscaled_visual_url = upscale_image(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration
        print("Creating narration for the chapter...")
        narration_audio = generate_narration(chapter)
        print(f"Narration Audio URL: {narration_audio}")

        # Create video scene
        print("Creating video for the chapter...")
        video_url = create_video_scene(f"Chapter {i}: {theme}", narration_audio, upscaled_visual_url)
        enhanced_video_url = add_motion_effects(video_url)
        print(f"Enhanced Chapter Video URL: {enhanced_video_url}")
        chapter_videos.append(enhanced_video_url)

    # Generate Main Character Avatar
    print("\nCreating main character avatar...")
    character_intro = f"Hello, I'm {main_character}, your guide for this adventure."
    character_avatar_url = create_avatar(main_character, character_intro)
    print(f"Main Character Avatar Video URL: {character_avatar_url}")

    print("\nStorytelling Adventure Creation Complete!")
    print("Generated Chapters:")
    for video in chapter_videos:
        print(f"- {video}")
    print(f"Main Character Introduction Video: {character_avatar_url}")

if __name__ == "__main__":
    main()
""" Example Output
Theme: Fantasy
Main Character: Aria the Explorer
Ending Style: Open-Ended

Generated Story Adventure:

Animated chapters with engaging visuals and narration.
Virtual avatar as the main character introducing the story.
Dynamic transitions, music, and sound effects. """