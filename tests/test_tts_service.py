from pathlib import Path

from services.tts_service import TextToSpeechService


class DummyGTTS:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def save(self, fp):
        Path(fp).write_bytes(b"fake-audio")


def test_speech_service_writes_audio_file(monkeypatch, tmp_path):
    monkeypatch.setattr("services.tts_service.gTTS", DummyGTTS)

    output_path = tmp_path / "speech.mp3"
    service = TextToSpeechService()

    service.synthesize("hello world", output_path=output_path)

    assert output_path.exists()
    assert output_path.read_bytes() == b"fake-audio"
