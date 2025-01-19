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

def generate_travel_story(destinations, activities, highlights):
    """
    Uses ChatGPT to create a travel story based on user input.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Write a cinematic travel story about a journey to {destinations}. "
              f"Include the following activities: {activities}. Highlight these moments: {highlights}. "
              f"Make it vivid, engaging, and emotional.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create visuals for the travel story.
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
    Uses ElevenLabs to narrate the travel story.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": script, "voice": "Engaging Narrator", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(theme):
    """
    Uses Suno to create background music for the travel video.
    """
    url = f"https://api.suno.ai/v1/music?theme={theme}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def create_travel_video(scene_title, narration, visual_url):
    """
    Uses Runway to create video segments for the travel story.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": scene_title,
        "text": narration,
        "image_url": visual_url,
        "style": "cinematic-travel"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def create_virtual_narrator(narration):
    """
    Uses HeyGen to create a virtual narrator avatar for the travel story.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": "Travel Story Narrator",
        "narration": narration,
        "avatar": "cinematic-narrator"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a personalized travel story video.
    """
    print("Welcome to the AI-Powered Travel Story Creator!")

    # User Inputs
    destinations = input("Enter the travel destinations (comma-separated): ").strip()
    activities = input("Enter the activities you did (comma-separated): ").strip()
    highlights = input("Enter the highlights of your trip (comma-separated): ").strip()

    # Generate Travel Story
    print("\nGenerating travel story...")
    travel_story = generate_travel_story(destinations, activities, highlights)
    print(f"\nTravel Story:\n{travel_story}")

    # Generate Visuals for the Story
    print("\nGenerating visuals for the travel story...")
    visual_description = f"Stunning landscapes and landmarks in {destinations}."
    visual_url = generate_visual(visual_description)
    upscaled_visual_url = upscale_image(visual_url)
    print(f"Upscaled Visual URL: {upscaled_visual_url}")

    # Generate Narration
    print("\nCreating narration for the travel story...")
    narration_audio = generate_audio_narration(travel_story)
    print(f"Narration Audio URL: {narration_audio}")

    # Generate Background Music
    print("\nGenerating background music...")
    music_url = generate_music("adventurous")
    print(f"Background Music URL: {music_url}")

    # Create Travel Video
    print("\nCreating travel story video...")
    video_url = create_travel_video(f"{destinations} Travel Story", narration_audio, upscaled_visual_url)
    print(f"Travel Story Video URL: {video_url}")

    # Create Virtual Narrator
    print("\nCreating virtual narrator for the travel story...")
    narrator_intro = f"Join us on an unforgettable journey to {destinations}!"
    narrator_url = create_virtual_narrator(narrator_intro)
    print(f"Virtual Narrator Video URL: {narrator_url}")

    print("\nTravel Story Video Creation Complete!")
    print("Generated Assets:")
    print(f"- Key Visuals: {upscaled_visual_url}")
    print(f"- Narration: {narration_audio}")
    print(f"- Background Music: {music_url}")
    print(f"- Travel Story Video: {video_url}")
    print(f"- Virtual Narrator: {narrator_url}")

if __name__ == "__main__":
    main()
""" Features
Cinematic Travel Story: ChatGPT weaves user inputs into a compelling narrative.
Visual Enhancements: Krea AI and Magnific create high-quality visuals of destinations.
Dynamic Narration: ElevenLabs provides professional voiceovers.
Cinematic Video Creation: Runway and Immersity AI add polished animations and effects.
Interactive Narrator: HeyGen creates a virtual narrator avatar to guide the audience. """