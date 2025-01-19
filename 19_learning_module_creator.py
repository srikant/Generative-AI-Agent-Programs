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

def generate_lesson_plan(topic, audience, difficulty, objectives):
    """
    Uses ChatGPT to create a structured learning module with lessons and quizzes.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Create a learning module on the topic '{topic}' for '{audience}'. "
              f"Difficulty level: '{difficulty}'. Learning objectives: {objectives}. "
              f"Include lessons, explanations, and interactive quizzes with answers and feedback.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create visuals for the learning module.
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

def create_lesson_video(lesson_title, narration, visual_url):
    """
    Uses Runway to create a video for a lesson in the module.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": lesson_title,
        "text": narration,
        "image_url": visual_url,
        "style": "educational"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def generate_narration(text):
    """
    Uses ElevenLabs to narrate lessons and provide feedback.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Professional Narrator", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create background music for the learning module.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_motion_effects(video_url):
    """
    Uses Immersity AI to enhance lesson videos with motion effects.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "educational-motion"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_tutor_avatar(narration):
    """
    Uses HeyGen to create a virtual tutor avatar.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": "Virtual Tutor Introduction",
        "narration": narration,
        "avatar": "friendly-tutor"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a personalized learning module.
    """
    print("Welcome to the AI-Powered Learning Module Creator!")

    # User Inputs
    topic = input("Enter the topic of the learning module: ").strip()
    audience = input("Enter the target audience (e.g., High School Students, Professionals): ").strip()
    difficulty = input("Enter the difficulty level (Beginner, Intermediate, Advanced): ").strip()
    objectives = input("Enter the learning objectives: ").strip()

    # Generate Lesson Plan
    print("\nGenerating lesson plan...")
    lesson_plan = generate_lesson_plan(topic, audience, difficulty, objectives)
    print(f"\nLesson Plan:\n{lesson_plan}")

    # Split lesson plan into lessons
    lessons = lesson_plan.split("\n\n")
    lesson_videos = []

    for i, lesson in enumerate(lessons, start=1):
        print(f"\nProcessing Lesson {i}...")

        # Generate visuals
        print("Generating visuals for the lesson...")
        visual_description = f"{lesson} - educational infographic style."
        visual_url = generate_visual(visual_description)
        upscaled_visual_url = upscale_image(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration
        print("Creating narration for the lesson...")
        narration_audio = generate_narration(lesson)
        print(f"Narration Audio URL: {narration_audio}")

        # Create lesson video
        print("Creating video for the lesson...")
        video_url = create_lesson_video(f"Lesson {i}: {topic}", narration_audio, upscaled_visual_url)
        enhanced_video_url = add_motion_effects(video_url)
        print(f"Enhanced Lesson Video URL: {enhanced_video_url}")
        lesson_videos.append(enhanced_video_url)

    # Create Virtual Tutor Introduction
    print("\nCreating virtual tutor avatar...")
    tutor_intro = f"Welcome to this learning module on {topic}. Let's explore together!"
    tutor_avatar_url = create_tutor_avatar(tutor_intro)
    print(f"Tutor Avatar Video URL: {tutor_avatar_url}")

    print("\nLearning Module Creation Complete!")
    print("Generated Lessons:")
    for video in lesson_videos:
        print(f"- {video}")
    print(f"Tutor Introduction Video: {tutor_avatar_url}")

if __name__ == "__main__":
    main()
""" Example Output
Topic: Introduction to Machine Learning
Audience: Beginners
Difficulty: Intermediate
Objectives: "Understand supervised learning, unsupervised learning, and key algorithms."

Generated Learning Module:

Interactive videos for each lesson with narration and visuals.
Quizzes with feedback narrated by a virtual tutor.
Background music to maintain engagement. """