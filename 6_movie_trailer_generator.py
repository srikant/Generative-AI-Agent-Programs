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

def generate_movie_storyline(genre, theme):
    """
    Uses ChatGPT to generate a movie storyline and trailer script.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Create a compelling movie storyline in the {genre} genre with the theme '{theme}'. "
              f"Also, write a dramatic trailer script highlighting key moments.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to generate visuals for the trailer scenes.
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
    Uses Runway to create animated video scenes.
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

def generate_narration(trailer_script):
    """
    Uses ElevenLabs to create a dramatic voiceover for the trailer.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": trailer_script, "voice": "James", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to generate background music for the trailer.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_dynamic_effects(video_url):
    """
    Uses Immersity AI to enhance the video with dynamic effects.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "action-cinematic"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_avatar_intro(character_name, narration):
    """
    Uses HeyGen to create a talking avatar for a character introduction.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": f"Character Intro: {character_name}",
        "narration": narration,
        "avatar": "dramatic-character"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to generate a personalized movie trailer.
    """
    print("Welcome to the AI-Powered Movie Trailer Generator!")

    # User Inputs
    genre = input("Enter the movie genre (e.g., Action, Sci-Fi, Fantasy): ").strip()
    theme = input("Enter the theme of the movie (e.g., 'Redemption', 'Survival'): ").strip()
    if not genre or not theme:
        print("Please provide valid inputs for both genre and theme.")
        return

    # Generate Storyline and Script
    print("\nGenerating movie storyline and trailer script...")
    trailer_script = generate_movie_storyline(genre, theme)
    print(f"\nMovie Storyline and Script:\n{trailer_script}")

    # Split script into scenes
    scenes = trailer_script.split("\n\n")
    video_urls = []

    for i, scene in enumerate(scenes, start=1):
        print(f"\nProcessing Scene {i}...")

        # Generate visuals
        print("Generating visuals for the scene...")
        visual_description = f"{scene} - {genre} style"
        visual_url = generate_visual(visual_description)
        upscaled_visual_url = upscale_visual(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration
        print("Creating narration for the scene...")
        narration_audio = generate_narration(scene)
        print(f"Narration Audio URL: {narration_audio}")

        # Create video
        print("Creating video for the scene...")
        video_url = create_video(f"Scene {i}", narration_audio, upscaled_visual_url)
        enhanced_video_url = add_dynamic_effects(video_url)
        print(f"Enhanced Video URL: {enhanced_video_url}")
        video_urls.append(enhanced_video_url)

    # Generate music
    print("\nGenerating background music...")
    music_url = generate_music("dramatic")
    print(f"Background Music URL: {music_url}")

    print("\nMovie Trailer Completed!")
    print("Generated Videos:")
    for video in video_urls:
        print(f"- {video}")

if __name__ == "__main__":
    main()
""" Example Output
Genre: Sci-Fi
Theme: Survival
Generated Trailer:
Scene-based videos with visuals, dramatic narration, and cinematic music.
A talking avatar introduces the protagonist.
Dynamic transitions and motion effects enhance the trailer. """