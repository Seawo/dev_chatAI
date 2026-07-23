from character.character_manager import CharacterManager
from conversation.conversation_manager import ConversationManager
from prompt.prompt_builder import PromptBuilder
from memory.memory_manager import MemoryManager
from llm.nvidia_client import NvidiaClient

class ChatManager:

    def __init__(self, api_key):

        self.character_manager = CharacterManager()
        self.conversation_manager = ConversationManager()
        self.memory_manager = MemoryManager()
        self.prompt_builder = PromptBuilder()
        self.llm = NvidiaClient(api_key)

    def chat(self, player_id, character_id, message):

        # 캐릭터 가져오기
        character = self.character_manager.get_character(character_id)

        if character is None:

            raise ValueError(f"Character '{character_id}' 를 찾을 수 없습니다.")

        # 유저 메세지 저장
        self.conversation_manager.add_user_message(

            player_id,

            character_id,

            message

        )

        # 현재 대화 가져오기
        conversation = self.conversation_manager.get_messages(

            player_id,

            character_id

        )
        
        # Memory 가져오기
        memories = self.memory_manager.load_memory(

            player_id,

            character_id

        )

        # Prompt 생성
        messages = self.prompt_builder.build(

            character,
            memories,
            conversation

        )

        # AI 호출
        answer = self.llm.chat(

            messages

        )

        # AI 답변 저장
        self.conversation_manager.add_assistant_message(

            player_id,

            character_id,

            answer

        )

        # 7. 반환
        return answer