from tts.tts_manager import TTSManager


tts = TTSManager()


voice = tts.generate(
    "(화를내며)야 너 정말 이럴거야?",
    "서아", "Female"
)


print(voice)