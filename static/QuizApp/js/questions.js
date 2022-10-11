const noOfQuestionEl = document.getElementById('number-of-questions');
const addQuestionBtn = document.getElementById('add-question');
const questionContainer = document.getElementById('test-questions');


// parseInt and stuff
const noOfQuestion = parseInt(noOfQuestionEl.innerText);


function showQTemp(){
    addQuestionBtn.classList.add('add-q-btn')
}

function shareTwitter(){
    console.log('share to Twitter')
}
function shareWhatsapp(){
    console.log('Share to whatsapp')
}
function copyLink(){
    var copyLink = document.getElementById("link");
    console.log('copylink')
}


function QTemp(questionNumber){
    // Question
    const question = document.createElement('div');
    question.classList.add('question');
    const questionNumberEl = document.createElement('span');
    questionNumberEl.innerText = questionNumber

    // Question > number, question
    const questiontxt = document.createElement('input');
    questiontxt.setAttribute('placeholder', 'Question');
    questiontxt.setAttribute('name', 'question');
    questiontxt.setAttribute('type', 'text');

    // Options
    const option_a = document.createElement('input');
    option_a.setAttribute('type', 'radio');
    option_a.setAttribute('id', 'option_a');
    option_a.setAttribute('name', 'option_a');
    option_a.setAttribute('value', '');
    const option_a_label = document.createElement('input');
    option_a_label.setAttribute('for', 'option_a');
    
    const option_b = document.createElement('input');
    option_b.setAttribute('type', 'radio');
    option_b.setAttribute('id', 'option_b');
    option_b.setAttribute('name', 'option_b');
    option_b.setAttribute('value', '');
    const option_b_label = document.createElement('input');
    option_b_label.setAttribute('for', 'option_b');
    
    const option_c = document.createElement('input');
    option_c.setAttribute('type', 'radio');
    option_c.setAttribute('id', 'option_c');
    option_c.setAttribute('name', 'option_c');
    option_c.setAttribute('value', '');
    const option_c_label = document.createElement('input');
    option_c_label.setAttribute('for', 'option_c');
    
    const option_d = document.createElement('input');
    option_d.setAttribute('type', 'radio');
    option_d.setAttribute('id', 'option_d');
    option_d.setAttribute('name', 'option_d');
    option_d.setAttribute('value', '');
    const option_d_label = document.createElement('input');
    option_d_label.setAttribute('for', 'option_d');
    const br = document.createElement('br')

    question.appendChild(questionNumberEl, questiontxt, option_a, option_a_label, br, option_b, option_b_label, br, option_c, option_c_label, br, option_d, option_d_label)
    questionContainer.appendChild(question)
}
