import gradio as gr

def greet(name):
    return f"Hello {name}!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text").launch(share=True)
iface.launch(server_name='0.0.0.0', server_port=7860)

