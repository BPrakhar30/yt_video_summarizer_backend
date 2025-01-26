from flask import Blueprint, request, jsonify
from app.services.youtube_service import get_video_transcript
from app.services.openai_service import generate_summary
import logging

main = Blueprint('main', __name__)

@main.route('/api/summarize', methods=['POST'])
def summarize_video():

    # Log incoming request
    logging.info(f"Received request for URL: {request.json.get('video_url', 'No URL provided')}")

    data = request.json
    video_url = data.get('video_url')
    api_key = data.get('api_key')  # SECURITY: This key should never be logged or stored

    if not video_url or not api_key:
        logging.error("Missing parameters in request")
        return jsonify({'error': 'Missing required parameters'}), 400

    try:

        logging.info("Fetching video transcript...")
        # Get video transcript
        transcript = get_video_transcript(video_url)
        
        logging.info("Generating summary...")
        # Generate summary using OpenAI
        summary = generate_summary(transcript, api_key)

        logging.info("Summary generated successfully")    
        return jsonify({'summary': summary})
    except Exception as e:
        # Ensure API key is not included in error messages
        error_message = str(e)
        if api_key in error_message:
            error_message = error_message.replace(api_key, '[API KEY]')

        logging.error(f"Error in summarize_video: {error_message}")    
        return jsonify({'error': error_message}), 500 