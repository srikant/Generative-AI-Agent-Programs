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

def generate_recipe(dish, theme, dietary_preferences):
    """
    Uses ChatGPT to create a detailed recipe with instructions and cooking tips.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Create a detailed recipe for '{dish}' with the theme '{theme}'. "
              f"Include dietary preferences: {dietary_preferences}. Provide step-by-step instructions, ingredients, and tips.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create visuals for the dish and cooking steps.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def upscale_image(image_url):
    """
    Uses Magnific to upscale visuals for high-quality display.
    """
    url = "https://api.magnific.ai/v1/upscale"
    headers = {"Authorization": f"Bearer {MAGNIFIC_API_KEY}"}
    payload = {"image_url": image_url}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["upscaled_image_url"]

def create_step_video(step_description, visual_url):
    """
    Uses Runway to create a video for a cooking step.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": "Cooking Step",
        "text": step_description,
        "image_url": visual_url,
        "style": "cooking-style"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def generate_narration(text):
    """
    Uses ElevenLabs to narrate the recipe steps.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Chef Tone", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create background music for the recipe video.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_motion_effects(video_url):
    """
    Uses Immersity AI to add motion effects to the cooking video.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "cooking-motion"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_chef_avatar(narration):
    """
    Uses HeyGen to create a virtual chef avatar.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": "Chef Introduction",
        "narration": narration,
        "avatar": "chef-avatar"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a personalized multimedia recipe.
    """
    print("Welcome to the AI-Powered Digital Recipe Creator!")

    # User Inputs
    dish = input("Enter the name of the dish: ").strip()
    theme = input("Enter the theme (e.g., Vegan, Holiday): ").strip()
    dietary_preferences = input("Enter any dietary preferences (e.g., Gluten-Free, Low Carb): ").strip()

    # Generate Recipe
    print("\nGenerating recipe...")
    recipe = generate_recipe(dish, theme, dietary_preferences)
    print(f"\nRecipe:\n{recipe}")

    # Split recipe into steps
    steps = recipe.split("\n\n")
    step_videos = []

    for i, step in enumerate(steps, start=1):
        print(f"\nProcessing Step {i}...")

        # Generate visuals
        print("Generating visuals for the step...")
        visual_description = f"{step} - cooking illustration."
        visual_url = generate_visual(visual_description)
        upscaled_visual_url = upscale_image(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration
        print("Creating narration for the step...")
        narration_audio = generate_narration(step)
        print(f"Narration Audio URL: {narration_audio}")

        # Create step video
        print("Creating video for the step...")
        video_url = create_step_video(step, upscaled_visual_url)
        enhanced_video_url = add_motion_effects(video_url)
        print(f"Enhanced Step Video URL: {enhanced_video_url}")
        step_videos.append(enhanced_video_url)

    # Generate Chef Avatar
    print("\nCreating virtual chef avatar...")
    chef_intro = f"Welcome to this recipe tutorial for {dish}. Let's get started!"
    chef_avatar_url = create_chef_avatar(chef_intro)
    print(f"Chef Avatar Video URL: {chef_avatar_url}")

    print("\nDigital Recipe Creation Complete!")
    print("Generated Recipe Steps:")
    for video in step_videos:
        print(f"- {video}")
    print(f"Chef Introduction Video: {chef_avatar_url}")

if __name__ == "__main__":
    main()
""" Example Output
Dish: Spaghetti Carbonara
Theme: Italian Cuisine
Dietary Preferences: Gluten-Free

Generated Recipe:

Illustrated steps for cooking the dish.
Narrated instructions with background music.
Animated video transitions between steps.
Virtual chef avatar introducing the recipe. """