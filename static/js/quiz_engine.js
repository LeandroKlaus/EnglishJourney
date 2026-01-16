let currentQuestionIndex = 0;
let userAnswers = {};

const questionBox = document.getElementById('question-box');
const questionText = document.getElementById('question-text');
const optionsContainer = document.getElementById('options-container');
const progressBar = document.getElementById('progress-bar');
const calculatingState = document.getElementById('calculating-state');
const resultBox = document.getElementById('result-box');

function loadQuestion() {
    const currentQuestionData = quizData[currentQuestionIndex];
    
    if (currentQuestionIndex > 0) {
        questionBox.style.opacity = 0.5;
    }

    setTimeout(() => {
        questionText.textContent = currentQuestionData.question;
        optionsContainer.innerHTML = '';

        currentQuestionData.options.forEach((option, index) => {
            const button = document.createElement('button');
            button.classList.add('option-btn');
            button.textContent = option;
            button.addEventListener('click', () => selectOption(currentQuestionData.id, index, button));
            optionsContainer.appendChild(button);
        });

        const progressPercent = (currentQuestionIndex / quizData.length) * 100;
        progressBar.style.width = `${progressPercent}%`;

        questionBox.style.opacity = 1;

    }, 200);
}

function selectOption(questionId, selectedIndex, buttonElement) {
    const allOptions = optionsContainer.querySelectorAll('.option-btn');
    allOptions.forEach(btn => btn.classList.remove('selected'));
    buttonElement.classList.add('selected');

    userAnswers[questionId] = selectedIndex;

    setTimeout(() => {
        currentQuestionIndex++;
        if (currentQuestionIndex < quizData.length) {
            loadQuestion();
        } else {
            finishQuiz();
        }
    }, 400);
}

function finishQuiz() {
    progressBar.style.width = '100%';
    questionBox.classList.add('hidden');
    calculatingState.classList.remove('hidden');

    fetch('/api/calculate-result', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            answers: userAnswers,
            quiz_id: currentQuizId 
        }),
    })
    .then(response => response.json())
    .then(data => {
        setTimeout(() => {
            showResults(data);
        }, 1000);
    })
    .catch((error) => {
        console.error('Error:', error);
        alert("Ocorreu um erro ao processar o resultado.");
    });
}

function showResults(data) {
    calculatingState.classList.add('hidden');
    resultBox.classList.remove('hidden');

    document.getElementById('final-level-text').textContent = data.level;
    document.getElementById('score-text').textContent = data.score + '/' + data.total;
    document.getElementById('percent-text').textContent = data.percentage;
}

document.addEventListener('DOMContentLoaded', loadQuestion);