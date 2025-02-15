from django.shortcuts import render
from .models import Question, Subject

def chatbot_view(request):
    chat_history = request.session.get("chat_history", [])  # Store chat history
    response = ""
    question = None
    correct_answer = None

    if request.method == "POST":
        user_input = request.POST.get("user_input", "").strip().lower()

        # If user is answering a question
        if request.session.get("current_question_id"):
            question_id = request.session["current_question_id"]  # Keep question ID stored
            question = Question.objects.filter(id=question_id).first()

            if question:
                correct_answer = question.correct_option.lower()
                if user_input == correct_answer:
                    response = "✅ Correct! Great job! 🎉"
                    request.session.pop("current_question_id")  # Remove question from session
                else:
                    response = f"❌ Incorrect. Try again! Type A, B, C, or D."
        
        else:
            # Fetch a math or science question
            if "math" in user_input:
                subject = Subject.objects.filter(name__icontains="math").first()
            elif "science" in user_input:
                subject = Subject.objects.filter(name__icontains="science").first()
            elif "geography" in user_input:
                subject = Subject.objects.filter(name__icontains="geography").first() 
                   
            else:
                subject = None

            if subject:
                question = Question.objects.filter(subject=subject).order_by('?').first()
                if question:
                    response = f"Here's a {subject.name} question: {question.question_text} \n"
                    response += f"A) {question.option_a} | B) {question.option_b} | C) {question.option_c} | D) {question.option_d}"
                    request.session["current_question_id"] = question.id  # Store question ID
                else:
                    response = f"I couldn't find any {subject.name} questions in the database."

            else:
                # Default responses
                if "hello" in user_input:
                    response = "👋 Hi there! How can I assist you?"
                elif "bye" in user_input:
                    response = "👋 Goodbye! Have a great day!"
                else:
                    response = "🤖 I'm still learning! Can you ask me something else?"

        # Append to chat history
        chat_history.append({"user": user_input, "bot": response})
        request.session["chat_history"] = chat_history  # Save session data

    return render(request, 'chatbot/chatbot.html', {"response": response, "chat_history": chat_history})
