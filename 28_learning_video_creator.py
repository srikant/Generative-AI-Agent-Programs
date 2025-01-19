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

def generate_lesson_script(topic, audience, difficulty, teaching_style):
    """
    Uses ChatGPT to create an educational script.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Create an educational script on the topic '{topic}'. The target audience is '{audience}', "
              f"and the difficulty level is '{difficulty}'. The teaching style should be '{teaching_style}'. "
              f"Include an introduction, main points, examples, and a conclusion.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create visuals for the lesson.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def upscale_image(image_url):
    """
    Uses Magnific to upscale visuals for high-quality educational content.
    """
    url = "https://api.magnific.ai/v1/upscale"
    headers = {"Authorization": f"Bearer {MAGNIFIC_API_KEY}"}
    payload = {"image_url": image_url}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["upscaled_image_url"]

def generate_audio_narration(script):
    """
    Uses ElevenLabs to narrate the lesson script.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": script, "voice": "Professional Narrator", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create background music for the lesson video.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def create_lesson_video(scene_title, narration, visual_url):
    """
    Uses Runway to create a video segment for the lesson.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": scene_title,
        "text": narration,
        "image_url": visual_url,
        "style": "educational-video"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def create_instructor_avatar(narration):
    """
    Uses HeyGen to create a virtual instructor avatar.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": "Instructor Introduction",
        "narration": narration,
        "avatar": "professional-instructor"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a personalized learning video.
    """
    print("Welcome to the AI-Powered Personalized Learning Video Creator!")

    # User Inputs
    topic = input("Enter the topic of the lesson: ").strip()
    audience = input("Enter the target audience (e.g., High School Students, Professionals): ").strip()
    difficulty = input("Enter the difficulty level (Beginner, Intermediate, Advanced): ").strip()
    teaching_style = input("Enter the teaching style (e.g., Conversational, Formal): ").strip()

    # Generate Lesson Script
    print("\nGenerating lesson script...")
    lesson_script = generate_lesson_script(topic, audience, difficulty, teaching_style)
    print(f"\nLesson Script:\n{lesson_script}")

    # Generate Visuals for the Lesson
    print("\nGenerating visuals for the lesson...")
    visual_description = f"Illustration for the topic '{topic}', educational and professional."
    visual_url = generate_visual(visual_description)
    upscaled_visual_url = upscale_image(visual_url)
    print(f"Upscaled Visual URL: {upscaled_visual_url}")

    # Generate Narration
    print("\nCreating narration for the lesson...")
    narration_audio = generate_audio_narration(lesson_script)
    print(f"Narration Audio URL: {narration_audio}")

    # Generate Background Music
    print("\nGenerating background music...")
    music_url = generate_music("motivational")
    print(f"Background Music URL: {music_url}")

    # Create Lesson Video
    print("\nCreating the lesson video...")
    video_url = create_lesson_video(f"{topic} - Learning Video", narration_audio, upscaled_visual_url)
    print(f"Lesson Video URL: {video_url}")

    # Create Instructor Avatar
    print("\nCreating instructor avatar...")
    instructor_intro = f"Welcome to the lesson on {topic}. Let's dive in and explore this topic together!"
    avatar_url = create_instructor_avatar(instructor_intro)
    print(f"Instructor Avatar Video URL: {avatar_url}")

    print("\nLearning Video Creation Complete!")
    print("Generated Assets:")
    print(f"- Lesson Script: Available in console output")
    print(f"- Visuals: {upscaled_visual_url}")
    print(f"- Narration: {narration_audio}")
    print(f"- Background Music: {music_url}")
    print(f"- Lesson Video: {video_url}")
    print(f"- Instructor Avatar: {avatar_url}")

if __name__ == "__main__":
    main()
""" Features
Detailed Educational Content: ChatGPT generates a clear and structured lesson script.
Professional Visuals: Krea AI and Magnific create engaging visuals for the topic.
Dynamic Narration: ElevenLabs adds professional voiceovers.
Cinematic Video: Runway and Immersity AI produce polished video lessons with animations and transitions.
Virtual Instructor: HeyGen creates an engaging avatar to present the lesson. """