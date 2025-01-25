from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    if 'youtu.be' in url:
        return url.split('/')[-1]
    elif 'youtube.com' in url:
        return url.split('v=')[1].split('&')[0]
    return url

def get_video_transcript(url):
    """Get transcript of YouTube video"""
    try:
        video_id = get_video_id(url)
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Combine all transcript pieces into one text
        transcript_text = ' '.join([item['text'] for item in transcript_list])
        return transcript_text
    except Exception as e:
        raise Exception(f"Failed to get video transcript: {str(e)}") 