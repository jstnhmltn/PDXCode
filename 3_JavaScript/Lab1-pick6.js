let ticket = [];
let winner = [];
let match = 0;

function win_pick6() {
    for (i=0; i<6; i++) {
        winner.push(Math.floor(Math.random() * 100));
        }   
    console.log("win  ticket", winner);
}
win_pick6();

function tix_pick6() {
    for (i=0; i<6; i++) {
        ticket.push(Math.floor(Math.random() * 100));
        }   
    console.log("user ticket", ticket);
}
tix_pick6();

function matches() {
    //let payout = [0, 4, 7, 100, 50000, 1000000, 25000000];
    for (i=0; i<6; ++i) {
        if (ticket[i] === winner[i]) {
            match++;
        }
    }
    console.log("number of matches", match);
}
matches();

/*
function play100k() {
    winner = pick6();
    bal = 0;
    for (let i=0; i<100000; ++i) {
        ticket = pick6();
        bal -= 2;
        payout = matches(winner, ticket);
        bal +- payout;
    }
    return console.log(bal);
}

function main() {
    for (i=0; i<100; ++i) {
        play100k();
    }
}
main();
*/