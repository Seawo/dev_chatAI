# AI Roleplay Server

A Python-based AI server for creating immersive AI NPC experiences using NVIDIA Build API.

Designed for Unreal Engine integration, this server provides AI-driven character interactions with personality-based responses, conversation memory, world context, and dynamic voice generation using TTS.

The server manages multiple NPC characters, dialogue history, character personas, and AI-generated voice data to create interactive virtual characters.

---

## Features

🤖 **NVIDIA Build API Integration**
- AI response generation using NVIDIA LLM models

🎭 **Character Persona System**
- JSON-based NPC configuration
- Individual personality, speech style, and background settings

💬 **Conversation Memory System**
- Stores and manages NPC conversation history
- Maintains contextual interactions

🌍 **World Context System**
- Scenario-based environment information
- Supports various roleplay situations

🔊 **TTS Voice Generation**
- AI response converted into voice using edge-tts
- MP3 to WAV conversion pipeline
- Unreal runtime audio playback support

🔌 **Unreal Engine Integration**
- REST API communication between Unreal Engine and Python server
- Delivers AI responses and generated voice data

🧠 **Multi-NPC Roleplay Support**
- Supports multiple AI characters with unique personalities

⚡ **FastAPI REST Server**
- Lightweight and scalable AI server architecture


---

# AI 롤플레잉 서버

NVIDIA Build API를 활용하여 몰입감 있는 AI NPC 경험을 제공하는 Python 기반 AI 서버입니다.

언리얼 엔진(Unreal Engine)과의 연동을 목표로 설계되었으며, 캐릭터의 성격과 설정에 기반한 AI 대화, 대화 기억 관리, 상황(World) 정보, TTS 음성 생성 기능을 제공합니다.

다수의 NPC 캐릭터, 대화 기록, 캐릭터 페르소나, AI 생성 음성 데이터를 관리하여 실제와 같은 상호작용형 가상 캐릭터 환경을 구축합니다.

---

## 주요 기능

🤖 **NVIDIA Build API 연동**
- NVIDIA LLM 모델 기반 AI 응답 생성

🎭 **캐릭터 페르소나 시스템**
- JSON 기반 NPC 데이터 관리
- 캐릭터별 성격, 말투, 배경 설정 지원

💬 **대화 메모리 시스템**
- NPC와의 대화 기록 저장 및 관리
- 이전 대화를 기반으로 한 지속적인 상호작용 지원

🌍 **월드 컨텍스트 시스템**
- 상황 및 환경 데이터 기반 역할극 지원
- 다양한 시나리오 적용 가능

🔊 **TTS 음성 생성 시스템**
- AI 응답을 음성 데이터로 변환
- edge-tts 기반 음성 생성
- MP3 → WAV 변환 파이프라인 구축
- Unreal Runtime 음성 재생 지원

🔌 **Unreal Engine 연동**
- Unreal Engine ↔ Python Server REST API 통신
- AI 응답 및 생성된 음성 데이터 전달

🧠 **다중 NPC 역할극 지원**
- 서로 다른 성격과 설정을 가진 여러 NPC 관리

⚡ **FastAPI REST 서버**
- 가볍고 확장 가능한 AI 서버 구조
