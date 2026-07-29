import os
import datetime
import asyncio

import edge_tts


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


    def generate(
        self,
        text: str,
        character_name: str,
        gender: str
    ):

        voice = self._get_voice(gender)


        timestamp = datetime.datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )


        filename = (
            f"{timestamp}_"
            f"{gender}_"
            f"{character_name}.mp3"
        )


        output_path = os.path.join(
            self.output_dir,
            filename
        )


        asyncio.run(
            self._generate(
                text,
                voice,
                output_path
            )
        )


        return filename