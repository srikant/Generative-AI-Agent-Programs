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

def generate_movie_pitch(genre, concept, characters, tone):
    """
    Uses ChatGPT to create a professional movie pitch, including storyline and characters.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Create a movie pitch for a '{genre}' film. The concept is: '{concept}'. "
              f"Include main characters: {', '.join(characters)}. Describe the plot in detail with a '{tone}' tone.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create cinematic visuals for the pitch.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def upscale_image(image_url):
    """
    Uses Magnific to upscale visuals for high-quality movie concept art.
    """
    url = "https://api.magnific.ai/v1/upscale"
    headers = {"Authorization": f"Bearer {MAGNIFIC_API_KEY}"}
    payload = {"image_url": image_url}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["upscaled_image_url"]

def create_pitch_video(segment_title, narration, visual_url):
    """
    Uses Runway to create a video segment for the movie pitch.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": segment_title,
        "text": narration,
        "image_url": visual_url,
        "style": "cinematic"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def generate_narration(text):
    """
    Uses ElevenLabs to narrate the movie pitch.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Cinematic Narrator", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create cinematic background music for the pitch.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_motion_effects(video_url):
    """
    Uses Immersity AI to enhance pitch videos with cinematic effects.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "cinematic-motion"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_presenter_avatar(narration):
    """
    Uses HeyGen to create a virtual director avatar to present the pitch.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": "Movie Pitch Presentation",
        "narration": narration,
        "avatar": "director"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a personalized movie pitch.
    """
    print("Welcome to the AI-Powered Movie Pitch Creator!")

    # User Inputs
    genre = input("Enter the movie genre (e.g., Sci-Fi, Drama, Action): ").strip()
    concept = input("Enter the core concept of the movie: ").strip()
    characters = input("Enter the main characters (comma-separated): ").strip().split(',')
    tone = input("Enter the tone of the movie (e.g., Suspenseful, Inspirational): ").strip()

    # Generate Movie Pitch
    print("\nGenerating movie pitch...")
    pitch = generate_movie_pitch(genre, concept, characters, tone)
    print(f"\nMovie Pitch:\n{pitch}")

    # Split pitch into segments
    segments = pitch.split("\n\n")
    segment_videos = []

    for i, segment in enumerate(segments, start=1):
        print(f"\nProcessing Segment {i}...")

        # Generate visuals
        print("Generating visuals for the segment...")
        visual_description = f"{segment} - cinematic movie scene."
        visual_url = generate_visual(visual_description)
        upscaled_visual_url = upscale_image(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration
        print("Creating narration for the segment...")
        narration_audio = generate_narration(segment)
        print(f"Narration Audio URL: {narration_audio}")

        # Create pitch video
        print("Creating video for the segment...")
        video_url = create_pitch_video(f"Segment {i}: {genre} Movie", narration_audio, upscaled_visual_url)
        enhanced_video_url = add_motion_effects(video_url)
        print(f"Enhanced Video URL: {enhanced_video_url}")
        segment_videos.append(enhanced_video_url)

    # Create Presenter Avatar
    print("\nCreating presenter avatar...")
    presenter_intro = f"Welcome to the pitch for an exciting new {genre} movie. Let’s explore the story concept."
    presenter_avatar_url = create_presenter_avatar(presenter_intro)
    print(f"Presenter Avatar Video URL: {presenter_avatar_url}")

    print("\nMovie Pitch Creation Complete!")
    print("Generated Segments:")
    for video in segment_videos:
        print(f"- {video}")
    print(f"Presenter Introduction Video: {presenter_avatar_url}")

if __name__ == "__main__":
    main()
""" Example Output
Genre: Sci-Fi Thriller
Concept: "Humanity's last hope is an AI """