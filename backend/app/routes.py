from flask import Blueprint, request, jsonify
from app.services.youtube_service import get_video_transcript
from app.services.openai_service import generate_summary

main = Blueprint('main', __name__)

@main.route('/api/summarize', methods=['POST'])
def summarize_video():
    data = request.json
    video_url = data.get('video_url')
    api_key = data.get('api_key')  # SECURITY: This key should never be logged or stored

    if not video_url or not api_key:
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        # Get video transcript
        transcript = get_video_transcript(video_url)
        
        # Generate summary using OpenAI
        summary = generate_summary(transcript, api_key)
        
        return jsonify({'summary': summary})
    except Exception as e:
        # Ensure API key is not included in error messages
        error_message = str(e)
        if api_key in error_message:
            error_message = error_message.replace(api_key, '[API KEY]')
        return jsonify({'error': error_message}), 500 