from flask import Blueprint, request, jsonify
from app.services.youtube_service import get_video_transcript
from app.services.openai_service import generate_summary
import logging

main = Blueprint('main', __name__)

# Root route
@main.route('/')
def home():
    return jsonify({
        "message": "YouTube Video Summarizer API",
        "status": "running"
    })

# Test route
@main.route('/api/test', methods=['GET'])
def test_api():
    return jsonify({'status': 'API is working!'}), 200


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

        logging.info("Starting transcript fetch for video: %s", video_url)
        
        transcript = get_video_transcript(video_url)
        logging.info("Transcript fetched successfully, length: %d", len(transcript))
        
        logging.info("Starting summary generation with OpenAI")
        summary = generate_summary(transcript, api_key)
        logging.info("Summary generated successfully")  

        return jsonify({'summary': summary})
    
    except Exception as e:
        # Ensure API key is not included in error messages
        error_message = str(e)
        logging.error("Full error details: %s", error_message)

        if "Could not retrieve a transcript" in error_message:
            logging.error("Transcript fetch failed for video: %s", video_url)
            
            return jsonify({
                'error': 'This video does not have subtitles/captions available. Please try a different video that has closed captions enabled.'
            }), 400
        
        if api_key in error_message:
            error_message = error_message.replace(api_key, '[API KEY]')

        logging.error(f"Error in summarize_video: {error_message}")    
        return jsonify({'error': error_message}), 500 