from character.character_manager import CharacterManager
from conversation.conversation_manager import ConversationManager
from prompt.prompt_builder import PromptBuilder
from memory.memory_manager import MemoryManager
from llm.nvidia_client import NvidiaClient
from world.world_manager import WorldManager
from tts.tts_manager import TTSManager

class ChatManager:

    def __init__(self, api_key):

        self.character_manager = CharacterManager()
        self.world_manager = WorldManager()
        self.conversation_manager = ConversationManager()
        self.memory_manager = MemoryManager()
        self.prompt_builder = PromptBuilder()
        self.llm = NvidiaClient(api_key)
        self.tts = TTSManager()

    def chat(self, player_id, character_id, world_id, message):

    # ---------------------------------------------------------
    # 1. 캐릭터 확인
    # ---------------------------------------------------------
        character = self.character_manager.get_character(character_id)

        if character is None:
            raise ValueError(
                f"Character '{character_id}' 를 찾을 수 없습니다."
            )

        # ---------------------------------------------------------
        # 2. World 확인
        # ---------------------------------------------------------
        world = self.world_manager.get_world(world_id)

        if world is None:
            raise ValueError(
                f"World '{world_id}' 를 찾을 수 없습니다."
            )

        # ---------------------------------------------------------
        # 3. 사용자 메시지 확인
        # ---------------------------------------------------------
        if message is None or not message.strip():
            raise ValueError(
                "사용자 메시지가 비어있습니다."
            )

        # ---------------------------------------------------------
        # 4. 사용자 메시지 저장
        # ---------------------------------------------------------
        self.conversation_manager.add_user_message(
            player_id,
            character_id,
            message
        )

        # ---------------------------------------------------------
        # 5. 현재 Conversation 가져오기
        # ---------------------------------------------------------
        conversation = self.conversation_manager.get_messages(
            player_id,
            character_id
        )

        # ---------------------------------------------------------
        # 6. Memory 가져오기
        # ---------------------------------------------------------
        memories = self.memory_manager.load_memory(
            player_id,
            character_id
        )

        # ---------------------------------------------------------
        # 7. Prompt 생성
        # ---------------------------------------------------------
        messages = self.prompt_builder.build(
            character,
            world,
            memories,
            conversation
        )

        # ---------------------------------------------------------
        # 8. LLM 호출
        # ---------------------------------------------------------
        answer = self.llm.chat(
            messages
        )

        # ---------------------------------------------------------
        # 9. LLM 응답 검증
        # ---------------------------------------------------------
        if answer is None:
            raise RuntimeError(
                "LLM 응답이 None입니다."
            )

        if not isinstance(answer, str):
            raise RuntimeError(
                f"LLM 응답 타입이 올바르지 않습니다: "
                f"{type(answer).__name__}"
            )

        answer = answer.strip()

        if not answer:
            raise RuntimeError(
                "LLM 응답이 비어있습니다."
            )

        print()
        print("[ChatManager] ===== LLM Answer =====")
        print(answer)
        print("[ChatManager] ======================")

        # ---------------------------------------------------------
        # 10. AI 답변 저장
        # ---------------------------------------------------------
        self.conversation_manager.add_assistant_message(
            player_id,
            character_id,
            answer
        )

        # ---------------------------------------------------------
        # 11. TTS 생성
        # ---------------------------------------------------------
        voice_file = self.tts.generate(
            answer,
            character.name,
            character.gender
        )

        # ---------------------------------------------------------
        # 12. 반환
        # ---------------------------------------------------------
        return {
            "answer": answer,
            "voice": voice_file
        }