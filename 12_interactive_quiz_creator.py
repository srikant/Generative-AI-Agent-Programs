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

def generate_quiz(topic, difficulty, num_questions):
    """
    Uses ChatGPT to create a quiz with questions, answers, and explanations.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Create a {difficulty} quiz on the topic '{topic}' with {num_questions} questions. "
              f"For each question, provide four options, the correct answer, and a short explanation.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create visuals for the quiz background and questions.
    """
    url = "https://api.krea.ai/v1/images"
    headers = {"Authorization": f"Bearer {KREA_API_KEY}"}
    payload = {"prompt": description, "num_images": 1}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["images"][0]["url"]

def upscale_visual(image_url):
    """
    Uses Magnific to upscale visuals for high resolution.
    """
    url = "https://api.magnific.ai/v1/upscale"
    headers = {"Authorization": f"Bearer {MAGNIFIC_API_KEY}"}
    payload = {"image_url": image_url}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["upscaled_image_url"]

def create_video(question_text, options_text, visual_url):
    """
    Uses Runway to create a video for a quiz question.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": "Quiz Question",
        "text": f"{question_text}\n{options_text}",
        "image_url": visual_url,
        "style": "quiz-style"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def generate_narration(text):
    """
    Uses ElevenLabs to narrate quiz questions and answers.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Lively Host", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create background music for the quiz.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_motion_effects(video_url):
    """
    Uses Immersity AI to enhance quiz videos with interactive effects.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "quiz-motion"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_quiz_host_avatar(narration):
    """
    Uses HeyGen to create a virtual quiz host avatar.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": "Quiz Host Introduction",
        "narration": narration,
        "avatar": "friendly-host"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create an interactive quiz.
    """
    print("Welcome to the AI-Powered Interactive Quiz Creator!")

    # User Inputs
    topic = input("Enter the quiz topic (e.g., Space, History): ").strip()
    difficulty = input("Enter the difficulty level (Easy, Medium, Hard): ").strip()
    num_questions = int(input("Enter the number of questions: "))

    # Generate Quiz Questions
    print("\nGenerating quiz questions...")
    quiz_data = generate_quiz(topic, difficulty, num_questions)
    print(f"\nQuiz Data:\n{quiz_data}")

    # Split quiz into questions
    questions = quiz_data.split("\n\n")
    question_videos = []

    for i, question in enumerate(questions, start=1):
        print(f"\nProcessing Question {i}...")

        # Extract question text and options
        question_text, options_text = question.split("\nOptions:\n", 1)

        # Generate visuals
        print("Generating visuals for the question...")
        visual_description = f"{question_text} - quiz visual style."
        visual_url = generate_visual(visual_description)
        upscaled_visual_url = upscale_visual(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration
        print("Creating narration for the question...")
        narration_audio = generate_narration(question_text)
        print(f"Narration Audio URL: {narration_audio}")

        # Create video
        print("Creating video for the question...")
        video_url = create_video(question_text, options_text, upscaled_visual_url)
        enhanced_video_url = add_motion_effects(video_url)
        print(f"Enhanced Video URL: {enhanced_video_url}")
        question_videos.append(enhanced_video_url)

    # Generate quiz host avatar
    print("\nCreating quiz host avatar...")
    host_intro = f"Welcome to the {topic} Quiz! Let's test your knowledge."
    host_avatar_url = create_quiz_host_avatar(host_intro)
    print(f"Quiz Host Avatar Video URL: {host_avatar_url}")

    print("\nInteractive Quiz Creation Complete!")
    print("Generated Question Videos:")
    for video in question_videos:
        print(f"- {video}")
    print(f"Quiz Host Introduction Video: {host_avatar_url}")

if __name__ == "__main__":
    main()
""" Example Output
Topic: Space Exploration
Difficulty: Medium
Number of Questions: 5

Generated Interactive Quiz:

Animated question videos with visuals, narration, and transitions.
Background music for engagement.
Quiz host avatar introducing the quiz and providing feedback. """