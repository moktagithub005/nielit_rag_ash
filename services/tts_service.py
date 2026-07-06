from pathlib import Path

from gtts import gTTS


class TextToSpeechService:
    def __init__(self, language="en"):
        self.language = language

    def synthesize(self, text, output_path=None):
        if not text or not text.strip():
            raise ValueError("Text to synthesize cannot be empty")

        if output_path is None:
            output_path = Path("output/speech.mp3")
        else:
            output_path = Path(output_path)

        output_path.parent.mkdir(parents=True, exist_ok=True)

        tts = gTTS(text=text, lang=self.language)
        tts.save(str(output_path))

        return output_path
