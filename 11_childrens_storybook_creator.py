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

def generate_storyline(title, theme, characters, moral):
    """
    Uses ChatGPT to create a children's story with a moral lesson.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Write a children's story titled '{title}' with the theme '{theme}'. "
              f"The main characters are {', '.join(characters)}. "
              f"Conclude with the moral: '{moral}'. Include page descriptions for illustrations.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_illustration(description):
    """
    Uses Krea AI to create illustrations for the storybook pages.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def upscale_image(image_url):
    """
    Uses Magnific to upscale illustrations for high-resolution pages.
    """
    url = "https://api.magnific.ai/v1/upscale"
    headers = {"Authorization": f"Bearer {MAGNIFIC_API_KEY}"}
    payload = {"image_url": image_url}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["upscaled_image_url"]

def create_animated_page(page_title, narration, visual_url):
    """
    Uses Runway to create an animated storybook page.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": page_title,
        "text": narration,
        "image_url": visual_url,
        "style": "storybook"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def generate_narration(text):
    """
    Uses ElevenLabs to narrate the story.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Alice", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create background music for the story.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_motion_effects(video_url):
    """
    Uses Immersity AI to enhance animated pages with motion effects.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "storybook-motion"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_character_avatar(character_name, narration):
    """
    Uses HeyGen to create a talking avatar for a story character.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": f"{character_name} Introduction",
        "narration": narration,
        "avatar": "storybook-character"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a personalized children's storybook.
    """
    print("Welcome to the AI-Powered Children's Storybook Creator!")

    # User Inputs
    title = input("Enter the story title: ").strip()
    theme = input("Enter the story theme: ").strip()
    characters = input("Enter the main characters (comma-separated): ").strip().split(',')
    moral = input("Enter the moral of the story: ").strip()

    # Generate Storyline
    print("\nGenerating story...")
    storyline = generate_storyline(title, theme, characters, moral)
    print(f"\nStoryline:\n{storyline}")

    # Split storyline into pages
    pages = storyline.split("\n\n")
    page_videos = []

    for i, page in enumerate(pages, start=1):
        print(f"\nProcessing Page {i}...")

        # Generate illustrations
        print("Generating illustrations for the page...")
        visual_description = f"{page} - child-friendly illustration."
        visual_url = generate_illustration(visual_description)
        upscaled_visual_url = upscale_image(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration
        print("Creating narration for the page...")
        narration_audio = generate_narration(page)
        print(f"Narration Audio URL: {narration_audio}")

        # Create animated page
        print("Creating animated page...")
        video_url = create_animated_page(f"Page {i}: {title}", narration_audio, upscaled_visual_url)
        enhanced_video_url = add_motion_effects(video_url)
        print(f"Enhanced Page Video URL: {enhanced_video_url}")
        page_videos.append(enhanced_video_url)

    # Generate music
    print("\nAdding background music...")
    music_url = generate_music("uplifting")
    print(f"Background Music URL: {music_url}")

    print("\nChildren's Storybook Creation Complete!")
    print("Generated Pages:")
    for video in page_videos:
        print(f"- {video}")

if __name__ == "__main__":
    main()
""" Example Output
Title: "The Adventures of Luna the Brave"
Theme: Friendship and Courage
Characters: Luna, Max the Owl
Moral: "True courage lies in helping others."

Generated Storybook:

Illustrated pages with animations and narration.
Uplifting background music to engage children.
Talking avatars for """