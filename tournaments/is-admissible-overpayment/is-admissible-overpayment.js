function isAdmissibleOverpayment(prices, notes, x) {
    let difference = 0;
    
    for (i = 0; i < prices.length; i++) {
        const price = prices[i];
        const note = notes[i];
        const words = note.split(' ');
        
        if (words[0] === 'Same') { continue; }
            
        const first = words[0];
        const percent = Number(first.slice(0, first.length - 1)) / 100;
        let inStoreCost;
        
        if (words[1] === 'higher') {
            inStoreCost =  price / (1 + percent);
        }
        
        if (words[1] === 'lower') {
            inStoreCost =  price / (1 - percent);
        }
        
        difference += price - inStoreCost;
    }
    
    console.log(difference);
    return Math.round(difference * 1000000) <= x * 1000000;
}

function isAdmissibleOverpaymentV2(prices, notes, x) {
    var diff = 0,
        i,
        price, note, orig;
    for (i in prices) {
        price = prices[i];
        note = notes[i].match(/(.*)% (lower|higher)/);
        if (note) {
            if (note[2] == 'higher') {
                orig = price * 100 / (100 - - note[1]);
            } else {
                orig = price * 100 / (100 - note[1]);
            }
        } else {
            orig = price;
        }
        diff += price - Math.round(orig * 1e6) / 1e6;
    }
    return x >= diff;
}