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

def generate_event_script(event_type, key_moments, mood):
    """
    Uses ChatGPT to create a narrative script for event highlights.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Create a narrative script for a '{event_type}' highlights reel. The key moments are: {key_moments}. "
              f"The mood of the event is '{mood}'. Describe each moment with emotion and storytelling.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create artistic visuals for the event.
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
    Uses ElevenLabs to narrate the event highlights script.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": script, "voice": "Narrator", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create background music for the event reel.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def create_highlight_video(scene_title, narration, visual_url):
    """
    Uses Runway to create a video segment for the event highlights.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": scene_title,
        "text": narration,
        "image_url": visual_url,
        "style": "event-highlights"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def create_virtual_host(narration):
    """
    Uses HeyGen to create a virtual host avatar for the highlights reel.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": "Event Host Introduction",
        "narration": narration,
        "avatar": "event-host"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a personalized event highlights reel.
    """
    print("Welcome to the AI-Powered Event Highlights Creator!")

    # User Inputs
    event_type = input("Enter the type of event (e.g., Wedding, Birthday, Conference): ").strip()
    key_moments = input("Enter the key moments of the event (comma-separated): ").strip()
    mood = input("Enter the mood of the event (e.g., Joyful, Emotional, Professional): ").strip()

    # Generate Event Script
    print("\nGenerating event narrative script...")
    event_script = generate_event_script(event_type, key_moments, mood)
    print(f"\nEvent Script:\n{event_script}")

    # Generate Visuals for Key Moments
    print("\nGenerating visuals for key moments...")
    visual_description = f"{event_type} with key moments: {key_moments}. Mood: {mood}."
    visual_url = generate_visual(visual_description)
    upscaled_visual_url = upscale_image(visual_url)
    print(f"Upscaled Visual URL: {upscaled_visual_url}")

    # Generate Narration
    print("\nCreating narration for the event highlights...")
    narration_audio = generate_audio_narration(event_script)
    print(f"Narration Audio URL: {narration_audio}")

    # Generate Background Music
    print("\nGenerating background music...")
    music_url = generate_music(mood)
    print(f"Background Music URL: {music_url}")

    # Create Highlight Video
    print("\nCreating event highlight video...")
    video_url = create_highlight_video(f"{event_type} Highlights", narration_audio, upscaled_visual_url)
    print(f"Event Highlight Video URL: {video_url}")

    # Create Virtual Host
    print("\nCreating virtual host avatar...")
    host_intro = f"Welcome to the highlights of this wonderful {event_type}. Let’s relive the best moments!"
    host_avatar_url = create_virtual_host(host_intro)
    print(f"Virtual Host Video URL: {host_avatar_url}")

    print("\nEvent Highlights Reel Creation Complete!")
    print("Generated Assets:")
    print(f"- Visuals: {upscaled_visual_url}")
    print(f"- Narration: {narration_audio}")
    print(f"- Background Music: {music_url}")
    print(f"- Highlights Video: {video_url}")
    print(f"- Virtual Host: {host_avatar_url}")

if __name__ == "__main__":
    main()
""" Features
Engaging Narrative Script: ChatGPT generates a heartfelt or professional narrative for the event highlights.
High-Quality Visuals: Krea AI and Magnific produce detailed and artistic event visuals.
Dynamic Narration: ElevenLabs adds professional voiceovers to the video.
Cinematic Highlight Video: Runway and Immersity AI create smooth, cinematic transitions and effects.
Virtual Host: HeyGen creates an avatar that acts as the face of the event highlights reel.
 """