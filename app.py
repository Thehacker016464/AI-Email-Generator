from groq import Groq
from dotenv import load_dotenv
import send_email
import json
load_dotenv()


hacky = '''
    You are a hacky. you are help full and personlize AI assistant.use the tools list when needed.
'''


client = Groq()
while True:
    # r_mail=input('enter receriver mail: ')
    user = input('enter you query : ')
    
    response = client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {'role':'system','content':hacky},
            {'role':'user','content':user}
        ],
        tools=[send_email.email_tool_schema],
        tool_choice='auto',
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    if not tool_calls:
        print(response.choices[0].message.content)
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.function.name == 'send_email':
                args = json.loads(tool_call.function.arguments)
                print(args)
                #send_email.send_email(receiver=args['receiver_email'],sub=args['subject'],genrated_body=args['body'])
                print(f'Done, sir. I have sent the emai to {args['receiver_email']}')
    




