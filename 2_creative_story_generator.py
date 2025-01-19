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

def generate_module_outline(topic):
    """
    Uses ChatGPT to generate a structured outline for an educational module.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = f"Create a structured lesson outline for the topic: {topic}. Include sections, key points, and interactive activities."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to generate visuals for the topic sections.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def upscale_visual(image_url):
    """
    Uses Magnific to upscale the visuals.
    """
    url = "https://api.magnific.ai/v1/upscale"
    headers = {"Authorization": f"Bearer {MAGNIFIC_API_KEY}"}
    payload = {"image_url": image_url}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["upscaled_image_url"]

def create_video(section_title, narration, visual_url):
    """
    Uses Runway to create a video for a module section.
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

def generate_narration(text):
    """
    Uses ElevenLabs to generate voice narration for each module section.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Clara", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to generate background music for the lesson.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_dynamic_motion(video_url):
    """
    Uses Immersity AI to add interactive motion effects to the video.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "educational-highlight"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_avatar_intro(narration):
    """
    Uses HeyGen to create a talking avatar introduction for the module.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "narration": narration,
        "avatar": "friendly-educator"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create an interactive learning module.
    """
    print("Welcome to the AI-Powered Interactive Learning Module Creator!")

    # User Input
    topic = input("Enter the topic for the learning module: ").strip()
    if not topic:
        print("Please provide a valid topic.")
        return

    # Generate Module Outline
    print("\nGenerating module outline...")
    module_outline = generate_module_outline(topic)
    print(f"Module Outline:\n{module_outline}")

    # Split outline into sections
    sections = module_outline.split("\n\n")
    section_videos = []

    for i, section in enumerate(sections, start=1):
        print(f"\nProcessing Section {i}...")

        # Generate visuals
        print("Generating visuals...")
        visual_url = generate_visual(f"{section} related to {topic}")
        upscaled_visual_url = upscale_visual(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration
        print("Generating narration...")
        narration_audio = generate_narration(section)
        print(f"Narration Audio URL: {narration_audio}")

        # Create video
        print("Creating section video...")
        video_url = create_video(f"Section {i}: {topic}", narration_audio, upscaled_visual_url)
        enhanced_video_url = add_dynamic_motion(video_url)
        print(f"Enhanced Video URL: {enhanced_video_url}")
        section_videos.append(enhanced_video_url)

    # Generate avatar introduction
    print("\nCreating avatar introduction...")
    intro_narration = f"Welcome to this learning module on {topic}. Let's explore together!"
    avatar_intro_url = create_avatar_intro(intro_narration)
    print(f"Avatar Intro URL: {avatar_intro_url}")

    print("\nInteractive Learning Module Completed!")
    print("Generated Videos:")
    for video in section_videos:
        print(f"- {video}")
    print(f"Avatar Introduction Video: {avatar_intro_url}")

if __name__ == "__main__":
    main()
""" Example Output:
Topic: Solar System
Generated Modules:

Section 1: Introduction to Planets (video, narration, and visuals)
Section 2: How the Solar System Formed (interactive video)
Avatar Intro: "Hello! Let's explore the wonders of our solar system!"
This creates a fully multimedia, engaging educational experience. Let me know if you’d like further refinements! 🌟📚 """