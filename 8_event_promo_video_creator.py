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

def generate_promo_script(event_type, theme, date, highlights):
    """
    Uses ChatGPT to generate a promotional video script.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Write a promotional video script for a {event_type} with the theme '{theme}'. "
              f"Include the date '{date}' and key highlights: {', '.join(highlights)}. "
              f"Make it engaging with a call to action.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create visuals for the promo video.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def upscale_visual(image_url):
    """
    Uses Magnific to upscale visuals to high quality.
    """
    url = "https://api.magnific.ai/v1/upscale"
    headers = {"Authorization": f"Bearer {MAGNIFIC_API_KEY}"}
    payload = {"image_url": image_url}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["upscaled_image_url"]

def create_video(section_title, narration, visual_url):
    """
    Uses Runway to create an animated video section.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": section_title,
        "text": narration,
        "image_url": visual_url,
        "style": "cinematic"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def generate_narration(script):
    """
    Uses ElevenLabs to create a narration for the promo video.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": script, "voice": "Emma", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create background music for the promo.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_dynamic_effects(video_url):
    """
    Uses Immersity AI to enhance the promo video with motion effects.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "promotional-motion"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_avatar_intro(event_name, narration):
    """
    Uses HeyGen to create a talking avatar for event introduction.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": f"Welcome to {event_name}",
        "narration": narration,
        "avatar": "event-host"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a promotional video for an event.
    """
    print("Welcome to the AI-Powered Event Promo Video Creator!")

    # User Inputs
    event_type = input("Enter the event type (e.g., Wedding, Conference): ").strip()
    theme = input("Enter the event theme: ").strip()
    date = input("Enter the event date: ").strip()
    highlights = input("Enter key highlights of the event (comma-separated): ").strip().split(',')

    # Generate Promo Script
    print("\nGenerating promotional script...")
    promo_script = generate_promo_script(event_type, theme, date, highlights)
    print(f"\nPromo Script:\n{promo_script}")

    # Generate visuals and video sections
    video_urls = []
    sections = promo_script.split("\n\n")

    for i, section in enumerate(sections, start=1):
        print(f"\nProcessing Section {i}...")

        # Generate visuals
        print("Generating visuals for the section...")
        visual_description = f"{section} - promotional style."
        visual_url = generate_visual(visual_description)
        upscaled_visual_url = upscale_visual(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration
        print("Creating narration for the section...")
        narration_audio = generate_narration(section)
        print(f"Narration Audio URL: {narration_audio}")

        # Create video
        print("Creating video for the section...")
        video_url = create_video(f"Section {i}", narration_audio, upscaled_visual_url)
        enhanced_video_url = add_dynamic_effects(video_url)
        print(f"Enhanced Video URL: {enhanced_video_url}")
        video_urls.append(enhanced_video_url)

    # Generate music
    print("\nAdding background music...")
    music_url = generate_music("upbeat")
    print(f"Background Music URL: {music_url}")

    # Create avatar intro
    print("\nCreating avatar introduction...")
    intro_narration = f"Welcome to {event_type}! Join us on {date} for an unforgettable experience."
    avatar_intro_url = create_avatar_intro(event_type, intro_narration)
    print(f"Avatar Intro URL: {avatar_intro_url}")

    print("\nPromotional Video Completed!")
    print("Generated Videos:")
    for video in video_urls:
        print(f"- {video}")
    print(f"Avatar Introduction Video: {avatar_intro_url}")

if __name__ == "__main__":
    main()
""" Example Output
Event Type: Product Launch
Theme: Futuristic Innovation
Date: January 25, 2025
Highlights: "Cutting-edge tech, interactive demos, VIP networking"
Generated Event Promo Video:

Avatar Intro: Welcomes attendees with key event details.
Video Segments: Highlight event features with visuals, narration, and music.
Dynamic Transitions: Cinematic effects for a professional promo. """