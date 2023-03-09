const timeColumn = document.getElementById('time-column');
tr = document.createElement('tr');
td = document.createElement('td');
td.className = 'date-time';
td.id = 'extra'
tr.appendChild(td);
timeColumn.appendChild(tr);

for (let i = 6; i <= 22; i += 0.5) {
    tr = document.createElement('tr');
    td = document.createElement('td');
    td.className = 'date-time';

    if (i % 1 === 0) {
        string = i.toString().concat(':00 ');
    } else {
        string = Math.floor(i).toString().concat(':30 ');
    }

    if (i < 12) {
        string = string.concat("AM");
    } else if (i > 12) {
        string = string.concat("PM");
    } else {
        string = string.concat("NN");
    }

    td.innerText = string;
    tr.appendChild(td);
    timeColumn.appendChild(tr);
}

room_name = document.getElementById("room").value
date = document.getElementById("date").value
const url = `/rooms?room_name=${room_name}&date=${date}`
fetch(url)
    .then(response => response.json())
    .then(json => {
        generateCalendar(json);
    })

function generateCalendar(json) {
    let s_time = [];
    let e_time = [];
    for (let item in json) {
        s_time.push(json[item].start_time);
        e_time.push(json[item].end_time);
    }
    console.log(s_time);
    console.log(e_time);

    date = document.getElementById("date").value.split("-");
    dateObj = new Date(date[0], date[1], date[2])
    const calendar = document.getElementById('calendar');

    for (let i = 6; i <= 22; i += 0.5) {
        tr = document.createElement('tr')
        if (i !== 22) {
            for (let j = 0; j < 7; j++) {
                let curr_datetime = "";
                td = document.createElement('td');
                if (i % 1 === 0) {
                    td.className = 'time-full';
                } else {
                    td.className = 'time-half';
                }
                tr.appendChild(td);
            }
        }
        calendar.appendChild(tr);
    }
}