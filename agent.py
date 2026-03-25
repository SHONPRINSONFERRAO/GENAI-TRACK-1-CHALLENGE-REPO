from google.adk.agents import Agent
import google.auth
import google.auth.transport.requests
import google.oauth2.id_token


def summarize_text(text: str, style: str = "concise") -> dict:
    """Summarizes the given text.

    Args:
        text (str): The text to summarize.
        style (str): Style of summary - "concise", "bullet_points", or "eli5".

    Returns:
        dict: status and the text to summarize.
    """
    if not text or len(text.strip()) < 10:
        return {
            "status": "error",
            "error_message": "Please provide text with at least 10 characters."
        }
    return {
        "status": "success",
        "text_to_summarize": text,
        "requested_style": style
    }


root_agent = Agent(
    name="summarizer_agent",
    model="gemini-2.5-flash",
    description="An AI agent that summarizes text in various styles.",
    instruction="""You are a professional text summarization agent.

    When a user sends you text to summarize:
    1. Use the summarize_text tool to process the input.
    2. If the tool returns success, generate a summary of the provided text
       in the requested style:
       - "concise": A brief 2-3 sentence summary
       - "bullet_points": Key points as bullet points
       - "eli5": Explain it like I'm 5 years old
    3. If no style is specified, default to "concise".
    4. Always be accurate and capture the key ideas.

    If the user asks something unrelated to summarization, politely explain
    that you are a text summarization agent.
    """,
    tools=[summarize_text],
)
