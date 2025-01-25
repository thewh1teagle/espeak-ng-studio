import gradio as gr
from espeak_ng import EspeakNG
from pathlib import Path

espeak = EspeakNG()

# Change to True if your language is RTL
IS_RTL = False 
# You should git clone espeak-ng to the same directory as this file
DICTSOURCE_PATH = Path(__file__).parent / "espeak-ng" / "dictsource" 
# Change to your language code
DEFAULT_LANGUAGE = "en"

# Store the thread to stop if needed
def phonemize_and_speak(text, speak, language, compile):
    if compile:
        espeak.compile_voice(dictsource_path=DICTSOURCE_PATH, voice=language)
    espeak.voice = language
    phonemes = espeak.phonemize(text, voice=language)
    espeak.stop()
    if speak:
        espeak.speak(text, voice=language)
    
    return phonemes

def create_ui():
    with gr.Blocks(theme=gr.themes.Soft(font=[gr.themes.GoogleFont('Roboto')])) as ui:
        text_input = gr.TextArea(label="Input Text", placeholder="Enter text to phonemize...", rtl=IS_RTL)
        language_input = gr.Textbox(label="Language", value=DEFAULT_LANGUAGE, placeholder="Enter language code")
        speak_checkbox = gr.Checkbox(label="Speak Text", value=True)
        compile_checkbox = gr.Checkbox(label="Compile phonemes", value=False)
        submit_button = gr.Button("Phonemize")
        phonemes_output = gr.Textbox(label="Phonemes")
        
        submit_button.click(
            fn=phonemize_and_speak, 
            inputs=[text_input, speak_checkbox, language_input, compile_checkbox], 
            outputs=[phonemes_output]
        )
    
    return ui

ui = create_ui()
ui.launch(debug=True)
