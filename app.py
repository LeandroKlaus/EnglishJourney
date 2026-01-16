from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

QUIZZES = {
    "beginner_1": {
        "title": "Iniciante: Fundamentos",
        "description": "Verbo To Be, Pronomes e Present Simple.",
        "level": "Iniciante",
        "difficulty_class": "level-easy",
        "questions": [
            {"id": 1, "question": "I _____ from Brazil.", "options": ["is", "am", "are"], "answer_index": 1},
            {"id": 2, "question": "She _____ pizza on weekends.", "options": ["eat", "eating", "eats"], "answer_index": 2},
            {"id": 3, "question": "_____ they your brothers?", "options": ["Is", "Am", "Are"], "answer_index": 2},
            {"id": 4, "question": "Where _____ you live?", "options": ["do", "does", "are"], "answer_index": 0},
            {"id": 5, "question": "My father _____ work today.", "options": ["don't", "doesn't", "isn't"], "answer_index": 1},
            {"id": 6, "question": "Choose the plural: 'One child, two _____'.", "options": ["childs", "children", "childrens"], "answer_index": 1},
            {"id": 7, "question": "What time _____ it?", "options": ["is", "am", "are"], "answer_index": 0}
        ]
    },
    "beginner_2": {
        "title": "Iniciante: Rotina e Passado",
        "description": "Simple Past básico e rotinas diárias.",
        "level": "Iniciante",
        "difficulty_class": "level-easy",
        "questions": [
            {"id": 1, "question": "Yesterday, I _____ soccer.", "options": ["play", "played", "playing"], "answer_index": 1},
            {"id": 2, "question": "They _____ at home last night.", "options": ["wasn't", "weren't", "didn't"], "answer_index": 1},
            {"id": 3, "question": "_____ you go to the party?", "options": ["Did", "Do", "Were"], "answer_index": 0},
            {"id": 4, "question": "I usually _____ up at 7 AM.", "options": ["get", "got", "getting"], "answer_index": 0},
            {"id": 5, "question": "She _____ a new car last month.", "options": ["buy", "buyed", "bought"], "answer_index": 2},
            {"id": 6, "question": "We _____ watching TV now.", "options": ["is", "am", "are"], "answer_index": 2},
            {"id": 7, "question": "He _____ not like spicy food.", "options": ["do", "does", "is"], "answer_index": 1}
        ]
    },
    "inter_1": {
        "title": "Intermediário: Experiências",
        "description": "Present Perfect vs Past Simple.",
        "level": "Intermediário",
        "difficulty_class": "level-medium",
        "questions": [
            {"id": 1, "question": "I _____ to Paris twice this year.", "options": ["have been", "went", "was"], "answer_index": 0},
            {"id": 2, "question": "She _____ here since 2010.", "options": ["works", "is working", "has worked"], "answer_index": 2},
            {"id": 3, "question": "I _____ him yesterday.", "options": ["have seen", "saw", "seen"], "answer_index": 1},
            {"id": 4, "question": "Have you _____ eaten sushi?", "options": ["ever", "never", "yet"], "answer_index": 0},
            {"id": 5, "question": "We haven't finished the project _____.", "options": ["just", "already", "yet"], "answer_index": 2},
            {"id": 6, "question": "While I was cooking, the phone _____.", "options": ["ring", "rang", "was ringing"], "answer_index": 1},
            {"id": 7, "question": "I am interested _____ learning new skills.", "options": ["on", "at", "in"], "answer_index": 2}
        ]
    },
    "inter_2": {
        "title": "Intermediário: Previsões e Planos",
        "description": "Futuro, Condicionais Zero e 1st.",
        "level": "Intermediário",
        "difficulty_class": "level-medium",
        "questions": [
            {"id": 1, "question": "Look at those clouds! It _____ rain.", "options": ["will", "is going to", "shalls"], "answer_index": 1},
            {"id": 2, "question": "If it rains, I _____ at home.", "options": ["stay", "will stay", "stayed"], "answer_index": 1},
            {"id": 3, "question": "I _____ help you if you ask.", "options": ["would", "will", "am"], "answer_index": 1},
            {"id": 4, "question": "This time tomorrow, I _____ flying to London.", "options": ["will be", "am", "will"], "answer_index": 0},
            {"id": 5, "question": "Unless you _____, you won't pass.", "options": ["study", "don't study", "will study"], "answer_index": 0},
            {"id": 6, "question": "I promise I _____ tell anyone.", "options": ["don't", "won't", "not"], "answer_index": 1},
            {"id": 7, "question": "He is good _____ playing chess.", "options": ["in", "at", "on"], "answer_index": 1}
        ]
    },
    "adv_1": {
        "title": "Avançado: Complex Grammar",
        "description": "Passive Voice, Reported Speech, 3rd Conditional.",
        "level": "Avançado",
        "difficulty_class": "level-hard",
        "questions": [
            {"id": 1, "question": "The house _____ built in 1990.", "options": ["is", "was", "has been"], "answer_index": 1},
            {"id": 2, "question": "She told me she _____ tired.", "options": ["is", "was", "has been"], "answer_index": 1},
            {"id": 3, "question": "If I _____ known, I would have come.", "options": ["have", "had", "would have"], "answer_index": 1},
            {"id": 4, "question": "I wish I _____ more time.", "options": ["have", "had", "have had"], "answer_index": 1},
            {"id": 5, "question": "By next year, I _____ graduated.", "options": ["will have", "will be", "have"], "answer_index": 0},
            {"id": 6, "question": "Seldom _____ seen such beauty.", "options": ["I have", "have I", "I did"], "answer_index": 1},
            {"id": 7, "question": "Despite _____ raining, we went out.", "options": ["of", "it", "(nothing)"], "answer_index": 1}
        ]
    },
    "adv_2": {
        "title": "Avançado: Phrasal Verbs & Connectors",
        "description": "Vocabulário técnico e verbos frasais.",
        "level": "Avançado",
        "difficulty_class": "level-hard",
        "questions": [
            {"id": 1, "question": "We need to _____ up with a solution.", "options": ["come", "go", "get"], "answer_index": 0},
            {"id": 2, "question": "Please _____ out this form.", "options": ["full", "fill", "feel"], "answer_index": 1},
            {"id": 3, "question": "I can't put _____ with this noise.", "options": ["up", "on", "in"], "answer_index": 0},
            {"id": 4, "question": "_____ it was expensive, I bought it.", "options": ["However", "Although", "Despite"], "answer_index": 1},
            {"id": 5, "question": "He turned _____ the job offer.", "options": ["off", "down", "out"], "answer_index": 1},
            {"id": 6, "question": "We have run _____ of milk.", "options": ["out", "off", "away"], "answer_index": 0},
            {"id": 7, "question": "Let's call _____ the meeting.", "options": ["out", "off", "away"], "answer_index": 1}
        ]
    },
    "fluent_1": {
        "title": "Fluente: Nuance & Idioms",
        "description": "Expressões idiomáticas e sutilezas da língua.",
        "level": "Fluente",
        "difficulty_class": "level-expert",
        "questions": [
            {"id": 1, "question": "Don't beat around the _____.", "options": ["tree", "bush", "shrub"], "answer_index": 1},
            {"id": 2, "question": "It's raining cats and _____.", "options": ["dogs", "frogs", "logs"], "answer_index": 0},
            {"id": 3, "question": "He spilled the _____ about the surprise.", "options": ["soup", "beans", "tea"], "answer_index": 1},
            {"id": 4, "question": "I'm feeling under the _____.", "options": ["weather", "storm", "cloud"], "answer_index": 0},
            {"id": 5, "question": "Break a _____!", "options": ["arm", "leg", "bone"], "answer_index": 1},
            {"id": 6, "question": "That sounds right up my _____.", "options": ["street", "alley", "road"], "answer_index": 1},
            {"id": 7, "question": "Choose the synonym for 'Ubiquitous':", "options": ["Scarce", "Omnipresent", "Hidden"], "answer_index": 1}
        ]
    },
    "fluent_2": {
        "title": "Fluente: Academic & Proficiency",
        "description": "Estruturas formais e vocabulário erudito.",
        "level": "Fluente",
        "difficulty_class": "level-expert",
        "questions": [
            {"id": 1, "question": "The data _____ inconsistent.", "options": ["is", "are", "be"], "answer_index": 1},
            {"id": 2, "question": "This phenomenon is known _____ 'gravity'.", "options": ["as", "for", "by"], "answer_index": 0},
            {"id": 3, "question": "We must adhere _____ the rules.", "options": ["with", "to", "at"], "answer_index": 1},
            {"id": 4, "question": "It is imperative that he _____ present.", "options": ["be", "is", "was"], "answer_index": 0},
            {"id": 5, "question": "Had I known, I _____ acted differently.", "options": ["would", "would have", "had"], "answer_index": 1},
            {"id": 6, "question": "He was acquited _____ all charges.", "options": ["of", "from", "for"], "answer_index": 0},
            {"id": 7, "question": "The epitome of _____.", "options": ["perfection", "perfect", "perfectly"], "answer_index": 0}
        ]
    }
}

TIPS = [
    {"title": "Imersão Digital", "content": "Mude o idioma do seu celular e computador para Inglês hoje mesmo.", "category": "Life Hack"},
    {"title": "A Técnica Feynman", "content": "Tente explicar um conceito gramatical simples para uma criança (ou pato de borracha) em inglês.", "category": "Estudos"},
    {"title": "Shadowing", "content": "Copie a fala de atores nativos com o mesmo ritmo e entonação.", "category": "Speaking"},
    {"title": "Consumo Passivo", "content": "Ouça podcasts em inglês enquanto lava a louça. Seu cérebro absorve os padrões.", "category": "Listening"}
]

def determine_level(percentage):
    if percentage < 20: return "Need Practice"
    if percentage < 40: return "Apprentice"
    if percentage < 60: return "Intermediate"
    if percentage < 80: return "Advanced"
    if percentage < 95: return "Expert"
    return "Master Native"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tests')
def list_tests():
    return render_template('tests.html', quizzes=QUIZZES)

@app.route('/tips')
def list_tips():
    return render_template('tips.html', tips=TIPS)

@app.route('/quiz/<quiz_id>')
def start_quiz(quiz_id):
    quiz = QUIZZES.get(quiz_id)
    if not quiz:
        return render_template('index.html') 
    
    safe_questions = []
    for q in quiz['questions']:
        safe_q = q.copy()
        del safe_q['answer_index']
        safe_questions.append(safe_q)
    
    return render_template('quiz.html', questions=safe_questions, quiz_title=quiz['title'], quiz_id=quiz_id)

@app.route('/api/calculate-result', methods=['POST'])
def calculate_result():
    data = request.json
    user_answers = data.get('answers', {})
    quiz_id = data.get('quiz_id')
    
    quiz = QUIZZES.get(quiz_id)
    if not quiz: return jsonify({"error": "Quiz not found"}), 404

    score = 0
    questions_list = quiz['questions']
    total_questions = len(questions_list)

    for q in questions_list:
        q_id = str(q['id'])
        if q_id in user_answers and user_answers[q_id] == q['answer_index']:
            score += 1
            
    percentage = (score / total_questions) * 100
    final_level = determine_level(percentage)
    
    return jsonify({
        "score": score,
        "total": total_questions,
        "level": final_level,
        "percentage": round(percentage)
    })

if __name__ == '__main__':
    app.run(debug=True)