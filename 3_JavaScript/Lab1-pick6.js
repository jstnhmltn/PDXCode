function pick6(){
    for (i=0; i<6; i++){
        return Math.floor(Math.random() * 100);
    }
}

function matches(ticket, winner){
    let match = 0;
    for (i=0; i<6; i++){
        if (ticket[i] === winner[i]){
            match++;
        }
    }
    return match;
}

function main(){
    let expense = 0;
    let payout = [0, 4, 7, 100, 50000, 1000000, 25000000];
    winner = pick6();
    for (i=0; i<10; i++){
        expense += 2;
        match = matches(winner, pick6());  
        balance = payout[match];
    }
    console.log("win  ticket", winner);
    console.log("user ticket", ticket);
    console.log("payout", payout[match]);
}
main();