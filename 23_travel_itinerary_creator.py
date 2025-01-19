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

def generate_itinerary(destination, days, style, activities):
    """
    Uses ChatGPT to create a travel itinerary based on user preferences.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Create a {days}-day travel itinerary for {destination}. The travel style is '{style}', and "
              f"the user prefers activities like {', '.join(activities)}. Include day-by-day plans, landmarks, "
              f"and travel tips.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create visuals for the travel itinerary.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def upscale_image(image_url):
    """
    Uses Magnific to upscale visuals for high-quality travel guides.
    """
    url = "https://api.magnific.ai/v1/upscale"
    headers = {"Authorization": f"Bearer {MAGNIFIC_API_KEY}"}
    payload = {"image_url": image_url}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["upscaled_image_url"]

def generate_audio_narration(text):
    """
    Uses ElevenLabs to narrate the travel itinerary.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Friendly Narrator", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create background music for the travel itinerary.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def create_video_segment(day_title, narration, visual_url):
    """
    Uses Runway to create a video segment for a day in the itinerary.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": day_title,
        "text": narration,
        "image_url": visual_url,
        "style": "travel-itinerary"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def create_virtual_guide(narration):
    """
    Uses HeyGen to create a virtual travel guide avatar.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": "Travel Guide Introduction",
        "narration": narration,
        "avatar": "friendly-travel-guide"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a personalized travel itinerary.
    """
    print("Welcome to the AI-Powered Travel Itinerary Creator!")

    # User Inputs
    destination = input("Enter your travel destination: ").strip()
    days = int(input("Enter the number of days for your trip: ").strip())
    style = input("Enter your travel style (e.g., Luxury, Adventure, Cultural): ").strip()
    activities = input("Enter your preferred activities (comma-separated): ").strip().split(',')

    # Generate Itinerary
    print("\nGenerating travel itinerary...")
    itinerary = generate_itinerary(destination, days, style, activities)
    print(f"\nItinerary:\n{itinerary}")

    # Split itinerary into daily segments
    daily_plans = itinerary.split("\n\n")
    day_videos = []

    for i, day_plan in enumerate(daily_plans, start=1):
        print(f"\nProcessing Day {i}...")

        # Generate visuals for the day
        print("Generating visuals for the day...")
        visual_description = f"{day_plan} - travel destination and activities."
        visual_url = generate_visual(visual_description)
        upscaled_visual_url = upscale_image(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration for the day
        print("Creating narration for the day...")
        narration_audio = generate_audio_narration(day_plan)
        print(f"Narration Audio URL: {narration_audio}")

        # Create video segment for the day
        print("Creating video for the day...")
        video_url = create_video_segment(f"Day {i}: {destination}", narration_audio, upscaled_visual_url)
        print(f"Day Video URL: {video_url}")
        day_videos.append(video_url)

    # Create Virtual Travel Guide
    print("\nCreating virtual travel guide avatar...")
    guide_intro = f"Welcome to your personalized travel itinerary for {destination}! Let's explore the best of it together."
    guide_avatar_url = create_virtual_guide(guide_intro)
    print(f"Travel Guide Avatar Video URL: {guide_avatar_url}")

    print("\nTravel Itinerary Creation Complete!")
    print("Generated Itinerary:")
    for video in day_videos:
        print(f"- {video}")
    print(f"Travel Guide Introduction Video: {guide_avatar_url}")

if __name__ == "__main__":
    main()
""" Features
Personalized Travel Itinerary: ChatGPT generates a day-by-day plan tailored to user preferences.
Visual Representation: Krea AI and Magnific create and enhance images for destinations and activities.
Engaging Narration: ElevenLabs narrates daily plans with a friendly tone.
Dynamic Video Itinerary: Runway and Immersity AI produce professional travel videos with smooth transitions.
Virtual Travel Guide: HeyGen creates an avatar to present and guide users through their itinerary.
 """