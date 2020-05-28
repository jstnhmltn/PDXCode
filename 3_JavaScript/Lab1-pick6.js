function pick6() {
    let winner = [];
    for (i=0; i<6; i++) {
        winner.push(Math.floor(Math.random() * 100));
        }   
    console.log(winner);
}
pick6();

/*function matches(ticket, winner) {
    let payout = [0, 4, 7, 100, 50000, 1000000, 25000000];
    let matches = 0;
    for (i=0; i<6; i++) {
        if (ticket[i] === winner[i]) {
            matches++;
        }
    console.log(payout[matches]);
    }
}

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