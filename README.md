# 🎙️ CR Voice Assistant

> **Course Title:** Artificial Intelligence and Expert Systems Lab  
> **Course Code:** CSE-4104  
> **Project Title:** CR Voice Assistant  

---

## 📑 Table of Contents
- [Abstract](#abstract)
- [Introduction](#introduction)
- [Objectives](#objectives)
- [Motivation](#motivation)
- [Related Work](#related-work)
- [Methodology](#methodology)
- [Workflow](#workflow)
- [GUI Interface](#gui-interface)
- [Why Our Project is AI](#why-our-project-is-ai)
- [Conclusion](#conclusion)
- [References](#references)

---

## 📘 Abstract
This project introduces an advanced-level **AI voice assistant** for high-quality speech interaction between users and machines. By combining **Speech-to-Text (STT)** and **Text-to-Speech (TTS)** technologies, the assistant can take commands via voice and reply through speech—enabling natural, hands-free conversation.  

The assistant is capable of:
- Opening websites and applications  
- Hotword detection  
- WhatsApp calls/video calls  
- Playing YouTube videos  
- Web searches  

Built with **Python** and APIs, this project demonstrates logic flow and rule-based decision-making without relying on machine learning. It emphasizes **accessibility, productivity, and flexibility**, laying the groundwork for future advancements in AI-powered assistants.

---

## 📝 Introduction
In recent years, voice assistants such as **Alexa, Siri, and Google Assistant** have revolutionized human-computer interaction. Inspired by these technologies, our project presents a **custom AI-based voice assistant** that performs **reliable STT and TTS** for natural human-computer interactions.  

Key highlights:
- Understands spoken commands and responds verbally  
- Integrates with tools and services (emails, scheduling, searches)  
- Built entirely with **Python** and open-source APIs  
- Cost-effective, customizable, and scalable  

This project bridges **theoretical AI concepts** with **real-world applications**, providing a hands-on learning experience in NLP, automation, and accessibility.

---

## 🎯 Objectives
The main objectives of this project are:

- **Voice-Based Interaction System**: Enable natural speech interaction.  
- **Integrate STT & TTS**: Convert user speech into text and vice versa.  
- **Tool Integration**: Automate WhatsApp calls, YouTube, websites, etc.  
- **Web Search**: Execute online searches and provide spoken results.  
- **Accessibility**: Ensure inclusivity for users with disabilities.  

---

## 💡 Motivation
Reasons behind building this assistant:

1. **Growing Demand for Voice Interfaces** – Voice is becoming a dominant interface in modern devices.  
2. **Enhancing Accessibility** – Empowering people with disabilities through hands-free technology.  
3. **Bridging AI and Daily Life** – Applying NLP and automation to real-world productivity.  
4. **Customization** – Unlike commercial assistants, this project enables task-specific tailoring.  
5. **Skill Development** – Practical experience in **Speech Recognition, NLP, TTS**, and automation.  

---

## 📚 Related Work
### [1] Artificial Intelligence Voice Assistant & Home Automation
- **Contributions**: Home automation, weather/news APIs, accessibility features  
- **Tools**: Python, Pyttsx3, Selenium, Speech Recognition  
- **Limitations**: Accuracy issues in noise, weak security, limited context handling  

### [2] AI Voice Assistant: Conversational Companion
- **Features**: STT, TTS, calendar & email integration, knowledge base, web search  
- **Tools**: Python 3.9+, Google APIs, Tavily API, Gemini, Deepgram  
- **Contribution**: Demonstrates scalability with API integrations  

---

## ⚙️ Methodology
### 5.1 Project Setup
- Install Python **3.13** and create a virtual environment  
- Dependencies: `speech_recognition`, `pyttsx3`, `pywhatkit`, `requests`, `webbrowser`  

### 5.2 Speech-to-Text (STT)
- Capture audio input using `speech_recognition`  
- Convert speech → text via Google STT API  
- Implement wake-word detection (e.g., *"Jarvis"*)  

### 5.3 Text-to-Speech (TTS)
- Use `pyttsx3` for natural speech output  
- Customizable voice (speed, gender, accent)  

### 5.4 Core Functionalities
- Open websites/apps  
- WhatsApp calls  
- Play YouTube videos  
- Web search with APIs  

### 5.5 Logic & Workflow
Example:
```
python
if "play music" in command:
    play_on_youtube(query)  
elif "send email" in command:
    send_email()  
Multithreading: Implement background processes for uninterrupted listening and task execution.
```

### 5.6 🧪 Testing & Debugging
- Test modules individually  
- Validate APIs and error handling  
- Collect user feedback  

### 5.7 🚀 Customization & Scalability
- Add ML models (e.g., ChatGPT API) for dynamic responses  
- GUI development with **Eel**  

---

## 🔄 Workflow
**Fig. 6.1: Workflow Diagram**  

<img src="www/assets/img/Screenshot 2025-08-19 185639.png" alt="GUI Screenshot" width="600"/> 
---

## 🖥️ GUI Interface
**Fig. 7.1: GUI Interface of CR Voice Assistant**  


<img src="www/assets/img/Screenshot 2025-05-26 024245.png" alt="GUI Screenshot" width="600"/>

---

## 🤖 Why Our Project is AI
- **NLP**: Processes natural language commands  
- **Speech Recognition**: Converts spoken words into text  
- **Decision-Making**: Executes actions via rule-based logic  
- **Context Awareness**: Handles tasks across apps/services  
- **Automation**: Executes queries with minimal human input  
- **Simulated Intelligence**: Mimics human-like responses using decision trees & rules  

---

## ✅ Conclusion
This project demonstrates the **design and implementation** of an AI-powered voice assistant with STT, TTS, and API integrations.  

### Key Achievements:
- Hands-free, natural human-computer interaction  
- Task automation: WhatsApp, YouTube, web search, scheduling  
- Accessibility and productivity improvements  

### Future Work:
- Real-time weather/news APIs  
- Advanced accessibility for disabled users  
- Incorporation of ML for contextual understanding  

---

## 📖 References
1. Singh, N. S., et al. (2024). *Artificial intelligence voice assistant and home automation*. IJ Science & Research Archive, 12(1), 2006–2017. https://doi.org/10.30574/ijsra.2024.12.1.0954  
2. Kaymen99. *AI Voice Assistant: Talk to an AI Agent...* GitHub, 2024. [Link](https://github.com/kaymen99/AI-Voice-assistant)  
3. ProjectsWithDigambar. *Jarvis Project*. GitHub, 2024. [Link](https://github.com/projectswithdigambar/jarvis)  

