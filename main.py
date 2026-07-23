from chat.chat_manager import ChatManager

API_KEY = "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"

chat = ChatManager(API_KEY)

while True:

    user = input("나 : ")

    if user.lower() in ["exit", "quit"]:
        print("프로그램을 종료합니다.")
        break

    answer = chat.chat(

        player_id="Player001",

        character_id="friend_1",

        message=user

    )

    print()

    print("AI :")

    print(answer)

    print()
