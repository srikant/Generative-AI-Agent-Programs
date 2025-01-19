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

def generate_story(title, characters, theme, moral):
    """
    Uses ChatGPT to create a children's story.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Write a children's story titled '{title}'. The main characters are {characters}. "
              f"The story should follow the theme '{theme}' and end with the moral: '{moral}'. "
              f"Make it engaging, imaginative, and fun.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create visuals for the story.
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

def generate_audio_narration(script):
    """
    Uses ElevenLabs to narrate the children's story.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": script, "voice": "Expressive Narrator", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(theme):
    """
    Uses Suno to create playful background music for the story.
    """
    url = f"https://api.suno.ai/v1/music?theme={theme}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def create_story_video(scene_title, narration, visual_url):
    """
    Uses Runway to create video segments for the story.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": scene_title,
        "text": narration,
        "image_url": visual_url,
        "style": "children's-story"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def create_character_avatar(narration):
    """
    Uses HeyGen to create a virtual character avatar.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": "Character Introduction",
        "narration": narration,
        "avatar": "playful-character"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a children's story video.
    """
    print("Welcome to the AI-Powered Children's Story Creator!")

    # User Inputs
    title = input("Enter the story title: ").strip()
    characters = input("Enter the main characters (comma-separated): ").strip()
    theme = input("Enter the story theme: ").strip()
    moral = input("Enter the story's moral: ").strip()

    # Generate Story Script
    print("\nGenerating the story script...")
    story_script = generate_story(title, characters, theme, moral)
    print(f"\nStory Script:\n{story_script}")

    # Generate Visuals for the Story
    print("\nGenerating visuals for the story...")
    visual_description = f"Colorful illustrations for the children's story '{title}' with characters {characters}."
    visual_url = generate_visual(visual_description)
    upscaled_visual_url = upscale_image(visual_url)
    print(f"Upscaled Visual URL: {upscaled_visual_url}")

    # Generate Narration
    print("\nCreating narration for the story...")
    narration_audio = generate_audio_narration(story_script)
    print(f"Narration Audio URL: {narration_audio}")

    # Generate Background Music
    print("\nGenerating background music...")
    music_url = generate_music("playful")
    print(f"Background Music URL: {music_url}")

    # Create Story Video
    print("\nCreating story video...")
    video_url = create_story_video(f"{title} Story Video", narration_audio, upscaled_visual_url)
    print(f"Story Video URL: {video_url}")

    # Create Character Avatar
    print("\nCreating character avatar...")
    avatar_intro = f"Hi! I'm one of the characters in the story '{title}'. Let me tell you what happened!"
    avatar_url = create_character_avatar(avatar_intro)
    print(f"Character Avatar Video URL: {avatar_url}")

    print("\nChildren's Story Video Creation Complete!")
    print("Generated Assets:")
    print(f"- Story Script: Available in console output")
    print(f"- Visuals: {upscaled_visual_url}")
    print(f"- Narration: {narration_audio}")
    print(f"- Background Music: {music_url}")
    print(f"- Story Video: {video_url}")
    print(f"- Character Avatar: {avatar_url}")

if __name__ == "__main__":
    main()
""" Features
Interactive Storytelling: ChatGPT crafts a fun, engaging children's story with a clear moral.
Vibrant Visuals: Krea AI and Magnific create high-quality story illustrations.
Expressive Narration: ElevenLabs provides playful voiceovers for characters and narration.
Dynamic Video Creation: Runway and Immersity AI add cinematic transitions and animations.
Character Personalization: HeyGen and Pinokio generate interactive avatars and custom character designs. """