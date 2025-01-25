from openai import OpenAI

def generate_summary(transcript, api_key):
    """Generate summary using OpenAI API"""
    try:
        # Initialize client with just the API key
        client = OpenAI(
            api_key=api_key
        )
        
        print("Debug: OpenAI client initialized successfully")  # Debug log
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes YouTube video transcripts."},
                {"role": "user", "content": f"""Please provide the summary of this video transcript: {transcript}. Format the response exactly as follows:

**Title:** [Title of the video]

**Summary:**
• [First point]
• [Second point]
• [Third point]
(continue with all main points and key takeaways)

**Conclusion:** [Conclusion of the video]"""}
            ],
            max_tokens=4096
        )
        
        raw_summary = response.choices[0].message.content
        # Ensure proper line breaks between sections
        formatted_summary = raw_summary.replace('**Summary:**', '\n**Summary:**\n')
        formatted_summary = formatted_summary.replace('**Conclusion:**', '\n**Conclusion:**\n')
        return formatted_summary
    
    except Exception as e:
        print(f"Debug: Error details - {str(e)}")  # Debug log
        print(f"Debug: Error type - {type(e)}")    # Debug log
        raise Exception(f"Failed to generate summary: {str(e)}")
