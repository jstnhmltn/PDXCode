add_button.onclick = function() {
    let todo_input = document.querySelector('#todo_input');
    let list = document.querySelector('#todo_list');
    let completed_list = document.querySelector('#completed_list');
    let text = todo_input.value;
    if (text === '') {
        return;
    }

    todo_input.value = '';
    let li = document.createElement('li');
    li.classList.add('todo_item');
    let text_div = document.createElement('div');
    text_div.innerHTML = text;

    let button_complete = document.createElement('button');
    button_complete.innerHTML = 'COMPLETE';
    button_complete.onclick = function() {
        list.removeChild(this.parentElement);
        let li = document.createElement('li');
        li.innerText = text;
        completed_list.appendChild(li);
    };

    li.appendChild(text_div);
    li.appendChild(button_complete);
    list.appendChild(li);
};