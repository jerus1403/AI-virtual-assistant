# Feature not complete - coming soon.
# def read_file_content(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             return file.read()
#     except Exception as e:
#         return f"Could not read file: {e}"


# def handle_file_question(file_path, question):
#     file_content = read_file_content(file_path)
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         temperature=0.7,
#         messages=[
#             {"role": "system", "content": "You are an assistant that helps answer questions based on the content of a provided text file."},
#             {"role": "user", "content": f"The content of the file is: {file_content}"},
#             {"role": "user", "content": f"The question is: {question}"}
#         ],
#     )
#     return response.choices[0].message.content
