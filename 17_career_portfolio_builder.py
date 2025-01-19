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

def generate_portfolio_script(name, career_summary, skills, projects, goals):
    """
    Uses ChatGPT to create a structured career portfolio script.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = (f"Write a professional career portfolio for {name}. Include the following sections: "
              f"Career Summary: {career_summary}, Key Skills: {', '.join(skills)}, "
              f"Projects: {', '.join(projects)}, and Future Goals: {goals}. Make it engaging and professional.")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def generate_visual(description):
    """
    Uses Krea AI to create visuals for portfolio sections.
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

def create_video_segment(segment_title, narration, visual_url):
    """
    Uses Runway to create a video segment for a portfolio section.
    """
    url = "https://api.runwayml.com/v1/videos"
    headers = {"Authorization": f"Bearer {RUNWAY_API_KEY}"}
    payload = {
        "title": segment_title,
        "text": narration,
        "image_url": visual_url,
        "style": "professional-portfolio"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["video_url"]

def generate_narration(text):
    """
    Uses ElevenLabs to narrate the portfolio sections.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"Authorization": f"Bearer {ELEVENLABS_API_KEY}"}
    payload = {"text": text, "voice": "Professional Narrator", "model": "v1"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json().get("audio_url", "Audio unavailable.")

def generate_music(mood):
    """
    Uses Suno to create background music for the portfolio video.
    """
    url = f"https://api.suno.ai/v1/music?mood={mood}"
    headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()["music_url"]

def add_motion_effects(video_url):
    """
    Uses Immersity AI to enhance portfolio videos with motion effects.
    """
    url = "https://api.immersity.ai/v1/effects"
    headers = {"Authorization": f"Bearer {IMMERSITY_API_KEY}"}
    payload = {"video_url": video_url, "effect": "portfolio-motion"}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["enhanced_video_url"]

def create_avatar_intro(name, narration):
    """
    Uses HeyGen to create a virtual host avatar for the portfolio.
    """
    url = "https://api.heygen.com/v1/avatars"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    payload = {
        "title": f"{name}'s Career Portfolio",
        "narration": narration,
        "avatar": "professional-host"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["avatar_video_url"]

def main():
    """
    Main function to create a personalized career portfolio.
    """
    print("Welcome to the AI-Powered Career Portfolio Builder!")

    # User Inputs
    name = input("Enter your name: ").strip()
    career_summary = input("Enter a brief career summary: ").strip()
    skills = input("Enter your key skills (comma-separated): ").strip().split(',')
    projects = input("Enter key projects you want to highlight (comma-separated): ").strip().split(',')
    goals = input("Enter your future professional goals: ").strip()

    # Generate Portfolio Script
    print("\nGenerating portfolio script...")
    portfolio_script = generate_portfolio_script(name, career_summary, skills, projects, goals)
    print(f"\nPortfolio Script:\n{portfolio_script}")

    # Split script into segments
    segments = portfolio_script.split("\n\n")
    segment_videos = []

    for i, segment in enumerate(segments, start=1):
        print(f"\nProcessing Segment {i}...")

        # Generate visuals
        print("Generating visuals for the segment...")
        visual_description = f"{segment} - professional portfolio style."
        visual_url = generate_visual(visual_description)
        upscaled_visual_url = upscale_image(visual_url)
        print(f"Upscaled Visual URL: {upscaled_visual_url}")

        # Generate narration
        print("Creating narration for the segment...")
        narration_audio = generate_narration(segment)
        print(f"Narration Audio URL: {narration_audio}")

        # Create video segment
        print("Creating video for the segment...")
        video_url = create_video_segment(f"Segment {i}: {name}'s Portfolio", narration_audio, upscaled_visual_url)
        enhanced_video_url = add_motion_effects(video_url)
        print(f"Enhanced Video URL: {enhanced_video_url}")
        segment_videos.append(enhanced_video_url)

    # Create Avatar Introduction
    print("\nCreating virtual host avatar...")
    intro_text = f"Welcome to {name}'s professional career portfolio. Let me guide you through their journey."
    avatar_video_url = create_avatar_intro(name, intro_text)
    print(f"Host Avatar Video URL: {avatar_video_url}")

    print("\nCareer Portfolio Creation Complete!")
    print("Generated Segments:")
    for video in segment_videos:
        print(f"- {video}")
    print(f"Host Introduction Video: {avatar_video_url}")

if __name__ == "__main__":
    main()
""" Example Output
Name: Alex Carter
Career Summary: "A software engineer with 5+ years of experience in full-stack development."
Key Skills: "Python, React, Cloud Computing"
Projects: "E-commerce Platform, AI Chatbot, Data Analytics Dashboard"
Goals: "To lead a development team in an innovative tech company."

Generated Portfolio:

Professional video segments with animations and visuals.
Virtual host introducing Alex’s career journey.
Background music and transitions for a polished feel. """