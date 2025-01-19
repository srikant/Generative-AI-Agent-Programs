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

def generate_invitation_script(event_type, theme, date, highlights):
    """
    Uses ChatGPT to create an event invitation script.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Write a personalized event invitation for a '{event_type}' on '{date}' with the theme '{theme}'. "
              f"Include key highlights: {', '.join(highlights)}. Make it engaging and festive.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create visuals for the event theme.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def upscale_image(image_url):
    """
    Uses Magnific to upscale visuals for high-quality invitations.
    """
    url = "https://api.magnific.ai/v1/upscale"
    headers = {"Authorization": f"Bearer {MAGNIFIC_API_KEY}"}
    payload = {"image_url": image_url}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["upscaled_image_url"]

def create_invitation_video(text, visual_url):
    """
    Uses Runway to create an animated invitation video.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": "Event Invitation",
        "text": text,
        "image_url": visual_url,
        "style": "invitation-style"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def generate_narration(text):
    """
    Uses ElevenLabs to narrate the invitation details.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Warm Invitation", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create background music for the invitation.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_motion_effects(video_url):
    """
    Uses Immersity AI to enhance the invitation video with motion effects.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "cinematic-invitation"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_host_avatar(narration):
    """
    Uses HeyGen to create a virtual host avatar for the invitation.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": "Event Host Introduction",
        "narration": narration,
        "avatar": "festive-host"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a personalized event invitation.
    """
    print("Welcome to the AI-Powered Event Invitation Creator!")

    # User Inputs
    event_type = input("Enter the event type (e.g., Wedding, Birthday, Conference): ").strip()
    theme = input("Enter the event theme: ").strip()
    date = input("Enter the event date: ").strip()
    highlights = input("Enter key highlights of the event (comma-separated): ").strip().split(',')

    # Generate Invitation Script
    print("\nGenerating invitation script...")
    invitation_script = generate_invitation_script(event_type, theme, date, highlights)
    print(f"\nInvitation Script:\n{invitation_script}")

    # Generate Visuals
    print("\nGenerating visuals...")
    visual_description = f"{theme} event decorations and designs."
    visual_url = generate_visual(visual_description)
    upscaled_visual_url = upscale_image(visual_url)
    print(f"Upscaled Visual URL: {upscaled_visual_url}")

    # Generate Narration
    print("\nCreating narration...")
    narration_audio = generate_narration(invitation_script)
    print(f"Narration Audio URL: {narration_audio}")

    # Create Invitation Video
    print("\nCreating invitation video...")
    video_url = create_invitation_video(invitation_script, upscaled_visual_url)
    enhanced_video_url = add_motion_effects(video_url)
    print(f"Enhanced Video URL: {enhanced_video_url}")

    # Create Host Avatar
    print("\nCreating virtual host avatar...")
    host_avatar_url = create_host_avatar(invitation_script)
    print(f"Host Avatar Video URL: {host_avatar_url}")

    print("\nEvent Invitation Creation Complete!")
    print(f"Invitation Video: {enhanced_video_url}")
    print(f"Host Avatar Video: {host_avatar_url}")

if __name__ == "__main__":
    main()
""" Example Output
Event Type: Wedding
Theme: Rustic Elegance
Date: June 15, 2025
Highlights: "Live Band, Sunset Ceremony, Gourmet Dinner"

Generated Invitation:

Animated video invitation with visuals and narration.
Virtual host introducing the event and inviting guests.
Background music matching the rustic theme. """