import os
import gradio as gr
from dotenv import load_dotenv

from brain import encode_image, analyze_image_with_query
from voice_of_patient import transcribe_with_groq
from voice_of_doctor import text_to_speech_with_gtts

load_dotenv()

system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose.
What's in this image? Do you find anything wrong with it medically?
If you make a differential, suggest some remedies for them.
Do not add any numbers or special characters in your response.
Your response should be in one long paragraph.
Also always answer as if you are answering to a real person.
Do not say 'In the image I see' but say 'With what I see, I think you have ....'
Do not respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot.
Keep your answer concise (max 2 sentences).
No preamble, start your answer right away please"""


def process_inputs(audio_filepath,image_filepath):

    if not audio_filepath:
        return "Please record your symptoms first.","Please provide your symptoms.",None

    speech_to_text_output=transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
        audio_filepath=audio_filepath,
        stt_modelm="whisper-large-v3"
    )

    if image_filepath:
        doctor_response=analyze_image_with_query(
            query=system_prompt+speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="qwen/qwen3.8-27b"
        )
    else:
        doctor_response="No image was provided for me to analyze."

    output_audio="final.mp3"

    text_to_speech_with_gtts(
        input_text=doctor_response,
        output_filepath=output_audio
    )

    return speech_to_text_output,doctor_response,output_audio


with gr.Blocks(
    theme=gr.themes.Soft(),
    title="AI Doctor"
) as iface:

    gr.Markdown(
        """
        # 🩺 AI Doctor
        ### Voice + Vision Medical Assistant
        Describe your symptoms using your voice and upload an image for analysis.
        """
    )

    with gr.Row():

        with gr.Column():

            gr.Markdown("### Patient Information")

            audio_input=gr.Audio(
                sources=["microphone","upload"],
                type="filepath",
                label="Describe Your Symptoms"
            )

            image_input=gr.Image(
                sources=["upload","webcam"],
                type="filepath",
                label="Upload Medical Image"
            )

            analyze_button=gr.Button(
                "🔍 Analyze",
                variant="primary"
            )

        with gr.Column():

            gr.Markdown("### Consultation")

            speech_output=gr.Textbox(
                label="Speech to Text",
                lines=3
            )

            doctor_output=gr.Textbox(
                label="Doctor's Response",
                lines=5
            )

            audio_output=gr.Audio(
                type="filepath",
                label="Doctor's Voice"
            )

    gr.Markdown(
        "⚠️ This project is for educational purposes and should not replace professional medical advice."
    )

    clear_button=gr.ClearButton(
        [audio_input,image_input,speech_output,doctor_output,audio_output],
        value="Clear"
    )

    analyze_button.click(
        fn=process_inputs,
        inputs=[audio_input,image_input],
        outputs=[speech_output,doctor_output,audio_output]
    )


iface.launch(debug=True)