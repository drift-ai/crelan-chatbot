import chainlit as cl

from embedchain import App


@cl.on_chat_start
async def on_chat_start():
    app = App.from_config(
        config={
            "app": {"config": {"name": "chainlit-app"}},
            "llm": {
                "config": {
                    "stream": True,
                    "model": "gpt-3.5-turbo-16k",
                    "temperature": 0.5,
                    "max_tokens": 4000,
                }
            },
        }
    )
    # import your data here
    app.add(
        "https://www.crelan.be/nl/particulieren/artikel/faq-mycrelan",
        data_type="web_page",
    )
    app.collect_metrics = True
    cl.user_session.set("app", app)
    await cl.Message(
        author="myCrelan Assistent",
        content="Hallo, stel mij maar een vraag over myCrelan!\n\nBonjour, posez-moi une question sur myCrelan!\n\nIn German: Hallo, stellen Sie mir einfach eine Frage über myCrelan!",
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    app = cl.user_session.get("app")

    # add loader with an empty message
    msg = cl.Message(content="")
    await msg.send()

    response = await cl.make_async(app.chat)(message.content)
    msg.content = (
        response
        + "\n\nMeer info over myCrelan: https://www.crelan.be/nl/particulieren/artikel/faq-mycrelan"
    )
    await msg.update()
