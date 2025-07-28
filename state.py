from typing import TypedDict, Optional, List

class GraphState(TypedDict, total=False):
    song: str
    artist: str
    title: str
    full_title: str
    lyrics_url: str
    lyrics_text: str
    mood: str  # Primary mood
    mood_options: List[str]  # Multiple mood classifications
    mood_confidence: float  # Confidence of primary mood
    playlist: List[tuple[str, str]]  # [(title, YouTube link)]
    error: Optional[str]
    validated: bool  # Flag for playlist validation