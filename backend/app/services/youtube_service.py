from youtube_transcript_api import YouTubeTranscriptApi
import logging

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    try:
        if 'youtu.be' in url:
            return url.split('/')[-1]
        elif 'youtube.com' in url:
            if 'v=' in url:
                return url.split('v=')[1].split('&')[0]
            elif 'embed/' in url:
                return url.split('embed/')[-1].split('?')[0]
        return url
    except Exception as e:
        logging.error(f"Error extracting video ID from URL {url}: {str(e)}")
        raise Exception(f"Invalid YouTube URL format: {url}")

def get_video_transcript(url):
    """Get transcript of YouTube video"""
    try:
        video_id = get_video_id(url)
        logging.info(f"Attempting to get transcript for video ID: {video_id}")

        # First, list all available transcripts
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        logging.info(f"Available transcripts: {transcript_list}")

        # Try to get English transcript first
        try:
            transcript = transcript_list.find_transcript(['en'])
        except:
            # If English isn't available, get the first available transcript and translate it
            transcript = transcript_list.find_transcript(['en-US', 'en-GB'])
            transcript = transcript.translate('en')

        # Get the actual transcript
        transcript_parts = transcript.fetch()
        
        # Combine all transcript pieces into one text
        transcript_text = ' '.join([item['text'] for item in transcript_parts])
        
        logging.info(f"Successfully retrieved transcript of length: {len(transcript_text)}")
        return transcript_text

    except Exception as e:
        logging.error(f"Error getting transcript for video {url}: {str(e)}")
        error_msg = str(e)
        
        if "TranscriptsDisabled" in error_msg:
            raise Exception("Transcripts are disabled for this video. Please try a video with closed captions enabled.")
        elif "NoTranscriptFound" in error_msg:
            raise Exception("No English transcript found for this video. Please try a video with English captions.")
        else:
            raise Exception(f"Failed to get video transcript: {error_msg}")
