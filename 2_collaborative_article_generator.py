import openai
import requests
import time

# API keys for tools (replace with your actual keys)
OPENAI_API_KEY = "your_openai_api_key"
MIDJOURNEY_API_KEY = "your_midjourney_api_key"
KREA_API_KEY = "your_krea_api_key"
RUNWAY_API_KEY = "your_runway_api_key"
ELEVENLABS_API_KEY = "your_elevenlabs_api_key"
ARTLIST_API_KEY = "your_artlist_api_key"
HEYGEN_API_KEY = "your_heygen_api_key"
HAILUO_API_KEY = "your_hailuo_api_key"

def generate_story(prompt):
    """
    Uses ChatGPT to generate a story script based on the given prompt.
    """
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Write a short fantasy story: {prompt}"}]
    )
    return response["choices"][0]["message"]["content"]

def generate_image(description):
    """
    Uses Krea AI to generate an image based on the provided description.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def create_video(image_url, narration, title):
    """
    Uses Runway to create a video using the provided image and narration.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": title,
        "image_url": image_url,
        "narration": narration,
        "style": "cinematic",
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def generate_narration(text):
    """
    Uses ElevenLabs to generate audio narration for the story.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Rachel", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    audio_url = response.json().get("audio_url", "Audio unavailable.")
    return audio_url

def add_music(narration_audio, music_type="calm"):
    """
    Uses Artlist to add background music to the narration.
    """
    url = f"https://api.artlist.io/v1/music?genre={music_type}"
    headers = {"Authorization": f"Bearer {ARTLIST_API_KEY}"}
    response = requests.get(url, headers=headers)
    music_url = response.json()["music_tracks"][0]["url"]
    return f"{narration_audio} + {music_url} (combined via editing tool)"

def create_avatar_narrator(narration, title):
    """
    Uses HeyGen to create a talking avatar for the story narration.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "narration": narration,
        "title": title,
        "avatar": "custom-avatar-01"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to run the multimedia story generator.
    """
    print("Welcome to the Multimedia Story Generator!")

    # Get user input
    prompt = input("Enter a story prompt (e.g., 'a dragon and a young hero in a magical forest'): ").strip()
    if not prompt:
        print("Please provide a valid prompt.")
        return

    # Generate the story script
    print("\nGenerating the story...")
    story = generate_story(prompt)
    print("\nStory:\n" + story)

    # Split the story into scenes for image generation
    scenes = story.split("\n\n")
    image_urls = []
    for i, scene in enumerate(scenes):
        print(f"\nGenerating image for Scene {i + 1}...")
        image_description = f"Visualize: {scene}"
        image_url = generate_image(image_description)
        image_urls.append(image_url)
        print(f"Scene {i + 1} image generated: {image_url}")

    # Generate narration
    print("\nGenerating narration audio...")
    narration_audio = generate_narration(story)
    print(f"Narration audio generated: {narration_audio}")

    # Add background music
    print("\nAdding background music...")
    audio_with_music = add_music(narration_audio)
    print(f"Audio with background music ready: {audio_with_music}")

    # Create video
    print("\nCreating video from images and narration...")
    videos = []
    for i, image_url in enumerate(image_urls):
        video_url = create_video(image_url, narration_audio, f"Scene {i + 1}")
        videos.append(video_url)
        print(f"Scene {i + 1} video generated: {video_url}")

    # Create a talking avatar for the story
    print("\nCreating a talking avatar...")
    avatar_video = create_avatar_narrator(narration_audio, "Talking Avatar Narrator")
    print(f"Talking avatar created: {avatar_video}")

    print("\nMultimedia Story Generation Complete!")
    print(f"\nStory Script:\n{story}")
    print("\nGenerated Videos:")
    for video in videos:
        print(f"- {video}")
    print(f"\nTalking Avatar Video: {avatar_video}")

if __name__ == "__main__":
    main()
