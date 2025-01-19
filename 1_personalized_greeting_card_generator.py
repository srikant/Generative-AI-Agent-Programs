import openai
import requests

# API keys (replace with your actual keys)
OPENAI_API_KEY = "your_openai_api_key"
MIDJOURNEY_API_KEY = "your_midjourney_api_key"
KREA_API_KEY = "your_krea_api_key"
MAGNIFIC_API_KEY = "your_magnific_api_key"
RUNWAY_API_KEY = "your_runway_api_key"
ARTLIST_API_KEY = "your_artlist_api_key"
ELEVENLABS_API_KEY = "your_elevenlabs_api_key"
HEYGEN_API_KEY = "your_heygen_api_key"
SUNO_API_KEY = "your_suno_api_key"
IMMERSITY_API_KEY = "your_immersity_api_key"
PINOKIO_API_KEY = "your_pinokio_api_key"

def generate_greeting(theme, recipient_name, occasion):
    """
    Uses ChatGPT to generate a personalized greeting message.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = f"Create a heartfelt {occasion} greeting for {recipient_name} with the theme '{theme}'."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_image(description):
    """
    Uses Krea AI to generate an image for the greeting card.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def upscale_image(image_url):
    """
    Uses Magnific to upscale the generated image.
    """
    url = "https://api.magnific.ai/v1/upscale"
    headers = {"Authorization": f"Bearer {MAGNIFIC_API_KEY}"}
    payload = {"image_url": image_url}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["upscaled_image_url"]

def generate_video(theme, greeting_message, image_url):
    """
    Uses Runway to create a short video based on the greeting and theme.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": f"{theme} Greeting Video",
        "theme": theme,
        "text": greeting_message,
        "image_url": image_url,
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def generate_music(mood):
    """
    Uses Suno to generate background music for the video.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def generate_voice_narration(text):
    """
    Uses ElevenLabs to generate a voice narration for the greeting message.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Clara", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def create_talking_avatar(narration_audio, title):
    """
    Uses HeyGen to create a talking avatar delivering the greeting.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": title,
        "audio_url": narration_audio,
        "avatar": "friendly-avatar"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def add_dynamic_effects(video_url):
    """
    Uses Immersity AI to add dynamic motion effects to the video.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "celebration"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def generate_character_face(description):
    """
    Uses Pinokio to generate a unique character face.
    """
    url = "https://api.pinokio.ai/v1/face"
    headers = {"Authorization": f"Bearer {PINOKIO_API_KEY}"}
    payload = {"description": description}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["face_url"]

def main():
    """
    Main function to generate a personalized multimedia greeting card.
    """
    print("Welcome to the AI-Powered Greeting Card Generator!")

    # User input
    recipient_name = input("Enter the recipient's name: ").strip()
    occasion = input("Enter the occasion (e.g., Birthday, Anniversary): ").strip()
    theme = input("Enter a theme (e.g., Magical Forest, Space Adventure): ").strip()

    # Generate greeting message
    print("\nGenerating the greeting message...")
    greeting_message = generate_greeting(theme, recipient_name, occasion)
    print(f"Greeting Message: {greeting_message}")

    # Generate background image
    print("\nGenerating the background image...")
    image_description = f"{theme} background for a greeting card"
    image_url = generate_image(image_description)
    upscaled_image_url = upscale_image(image_url)
    print(f"Background Image URL: {upscaled_image_url}")

    # Generate video
    print("\nCreating a greeting video...")
    video_url = generate_video(theme, greeting_message, upscaled_image_url)
    print(f"Video URL: {video_url}")

    # Generate music
    print("\nGenerating background music...")
    music_url = generate_music("happy")
    print(f"Music URL: {music_url}")

    # Generate voice narration
    print("\nCreating voice narration...")
    narration_audio = generate_voice_narration(greeting_message)
    print(f"Narration Audio URL: {narration_audio}")

    # Generate talking avatar
    print("\nCreating a talking avatar...")
    avatar_video_url = create_talking_avatar(narration_audio, f"{occasion} Greeting")
    print(f"Talking Avatar Video URL: {avatar_video_url}")

    # Add dynamic effects
    print("\nAdding dynamic effects to the video...")
    enhanced_video_url = add_dynamic_effects(video_url)
    print(f"Enhanced Video URL: {enhanced_video_url}")

    # Generate character face
    print("\nCreating a unique character face for the card...")
    character_face_url = generate_character_face(f"A {theme} character")
    print(f"Character Face URL: {character_face_url}")

    print("\nGreeting Card Generation Complete!")
    print(f"Final Enhanced Video: {enhanced_video_url}")
    print(f"Talking Avatar: {avatar_video_url}")
    print(f"Character Face: {character_face_url}")

if __name__ == "__main__":
    main()
