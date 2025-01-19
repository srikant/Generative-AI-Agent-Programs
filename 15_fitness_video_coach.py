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

def generate_workout_plan(goal, workout_type, experience_level):
    """
    Uses ChatGPT to create a personalized workout plan with step-by-step instructions.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Create a detailed workout plan for '{goal}' with a focus on '{workout_type}' exercises. "
              f"The user is at an '{experience_level}' fitness level. Include step-by-step instructions and tips.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create visuals for exercises and poses.
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

def create_workout_video(step_description, visual_url):
    """
    Uses Runway to create a video for a workout step.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": "Workout Step",
        "text": step_description,
        "image_url": visual_url,
        "style": "fitness-style"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def generate_narration(text):
    """
    Uses ElevenLabs to narrate workout instructions.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Motivational Coach", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create upbeat background music for the workout.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_motion_effects(video_url):
    """
    Uses Immersity AI to enhance workout videos with motion effects.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "workout-motion"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_fitness_coach_avatar(narration):
    """
    Uses HeyGen to create a virtual fitness coach avatar.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": "Fitness Coach Introduction",
        "narration": narration,
        "avatar": "fitness-coach"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a personalized fitness coaching video.
    """
    print("Welcome to the AI-Powered Fitness Video Coach!")

    # User Inputs
    goal = input("Enter your fitness goal (e.g., Weight Loss, Muscle Gain): ").strip()
    workout_type = input("Enter your workout type (e.g., Yoga, HIIT, Strength Training): ").strip()
    experience_level = input("Enter your fitness level (Beginner, Intermediate, Advanced): ").strip()

    # Generate Workout Plan
    print("\nGenerating workout plan...")
    workout_plan = generate_workout_plan(goal, workout_type, experience_level)
    print(f"\nWorkout Plan:\n{workout_plan}")

    # Split workout plan into steps
    steps = workout_plan.split("\n\n")
    step_videos = []

    for i, step in enumerate(steps, start=1):
        print(f"\nProcessing Step {i}...")

        # Generate visuals
        print("Generating visuals for the step...")
        visual_description = f"{step} - fitness exercise illustration."
        visual_url = generate_visual(visual_description)
        upscaled_visual_url = upscale_image(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration
        print("Creating narration for the step...")
        narration_audio = generate_narration(step)
        print(f"Narration Audio URL: {narration_audio}")

        # Create workout video
        print("Creating workout video for the step...")
        video_url = create_workout_video(step, upscaled_visual_url)
        enhanced_video_url = add_motion_effects(video_url)
        print(f"Enhanced Step Video URL: {enhanced_video_url}")
        step_videos.append(enhanced_video_url)

    # Generate Fitness Coach Avatar
    print("\nCreating virtual fitness coach avatar...")
    coach_intro = f"Welcome to your {goal} fitness journey! Let's crush this {workout_type} workout together!"
    coach_avatar_url = create_fitness_coach_avatar(coach_intro)
    print(f"Fitness Coach Avatar Video URL: {coach_avatar_url}")

    print("\nFitness Video Coaching Complete!")
    print("Generated Workout Steps:")
    for video in step_videos:
        print(f"- {video}")
    print(f"Fitness Coach Introduction Video: {coach_avatar_url}")

if __name__ == "__main__":
    main()
""" Example Output
Goal: Weight Loss
Workout Type: HIIT
Experience Level: Beginner

Generated Fitness Video:

Step-by-step animated workout demonstrations.
Personalized avatar introducing and guiding the workout.
Upbeat background music and cinematic motion effects. """