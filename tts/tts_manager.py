import os
import re
import datetime
import asyncio
import subprocess

import edge_tts
import imageio_ffmpeg


class TTSManager:

    def __init__(self):

        self.output_dir = "data/voices"

        os.makedirs(
            self.output_dir,
            exist_ok=True
        )


    def _get_voice(self, gender: str):

        if gender == "Male":
            return "ko-KR-InJoonNeural"

        elif gender == "Female":
            return "ko-KR-SunHiNeural"

        else:
            return "ko-KR-HyunsuMultilingualNeural"


    def _clean_text(self, text: str):

        # (), （）, [], {} 안의 내용 제거
        text = re.sub(r"\(.*?\)", "", text)
        text = re.sub(r"（.*?）", "", text)
        text = re.sub(r"\[.*?\]", "", text)
        text = re.sub(r"\{.*?\}", "", text)

        # 공백 정리
        text = re.sub(r"\n\s*\n", "\n", text)

        return text.strip()


    async def _generate(
        self,
        text: str,
        voice: str,
        output_path: str
    ):

        communicate = edge_tts.Communicate(
            text=text,
            voice=voice
        )

        await communicate.save(output_path)


    def _convert_to_wav(
        self,
        mp3_path: str,
        wav_path: str
    ):

        ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

        subprocess.run(
            [
                ffmpeg_path,
                "-y",
                "-i",
                mp3_path,
                wav_path
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )


    def generate(
        self,
        text: str,
        character_name: str,
        gender: str
    ):

        voice = self._get_voice(gender)
        text = self._clean_text(text)

        timestamp = datetime.datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        mp3_name = (
            f"{timestamp}_"
            f"{gender}_"
            f"{character_name}.mp3"
        )

        wav_name = (
            f"{timestamp}_"
            f"{gender}_"
            f"{character_name}.wav"
        )

        mp3_path = os.path.join(
            self.output_dir,
            mp3_name
        )

        wav_path = os.path.join(
            self.output_dir,
            wav_name
        )

        asyncio.run(
            self._generate(
                text,
                voice,
                mp3_path
            )
        )

        self._convert_to_wav(
            mp3_path,
            wav_path
        )

        # mp3 삭제
        if os.path.exists(mp3_path):
            os.remove(mp3_path)

        return wav_name