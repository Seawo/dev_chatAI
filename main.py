from tts.tts_manager import TTSManager


tts = TTSManager()


voice = tts.generate(
    "승우야 오늘 뭐했어? ㅎㅎ",
    "서아", "Female"
)


print(voice)