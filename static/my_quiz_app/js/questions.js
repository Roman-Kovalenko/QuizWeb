
function make_answer_list(all_Question, all_Choice, count){
var html_answer_list = ""
let alphabet_counter = 0;

html_answer_list += "<h2>" + all_Question[count].fields.text + "</h2>";
for (let j = 0; j < all_Choice.length; j++){
    if (all_Choice[j].fields.for_which_question == all_Question[count].pk){
        html_answer_list += "<p> <input class='checkbox' type='checkbox' " + 'value=' + all_Choice[j].pk + ' />'

        + " " + String.fromCharCode(97 + alphabet_counter).toUpperCase() + ") "

        + all_Choice[j].fields.text + "</p>"
        alphabet_counter += 1
    }
}
return html_answer_list
}

function save_user_check(current_checkboxes, user_answers_dict, quesion_pk){
let kostyl = [];
for(let i=0; i<current_checkboxes.length; i++){
    if (current_checkboxes[i].checked){
        kostyl.push(current_checkboxes[i].value);
    }
}
user_answers_dict[quesion_pk]['user_choices'] = kostyl;
}

function recovery_user_check(current_checkboxes, user_answers_dict, quesion_pk){
for(let i=0; i<current_checkboxes.length; i++){
    if (user_answers_dict[quesion_pk]['user_choices'].includes(current_checkboxes[i].value)){
                current_checkboxes[i].checked = true                                                                            
    }
    else {
        current_checkboxes[i].checked = false 
    }
} 
}

function change_count(elem){
let current_checkboxes = document.getElementsByClassName('checkbox');

// Запишем выделеные элементы
save_user_check(current_checkboxes, user_answers_dict, all_Question[count].pk)

//Изменение номера вопроса и ограничение для работы в диаппозоне имеющихся вопросов
if (elem.id == 'previous_btn'){
    if (count > 0 ) {
        count -= 1;
        document.getElementById("questions").innerHTML = 
        make_answer_list(all_Question, all_Choice, count);
    }   
}
else if (elem.id == 'next_btn'){
    if (count < all_Question.length-1) {
        count += 1;
        document.getElementById("questions").innerHTML = 
        make_answer_list(all_Question, all_Choice, count);
    }
}

if (count == 0) {
    previous_button.disabled = true
}
else if (count == all_Question.length-1)
{
    next_button.disabled = true
}
else {
    previous_button.disabled = false
    next_button.disabled = false
}
// Загрузим положения чекбоксов из массива
recovery_user_check(current_checkboxes, user_answers_dict, all_Question[count].pk)
}
