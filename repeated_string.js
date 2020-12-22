function repeatedString(s, n) {
    const arrString = s;

    // check 'a'
    if(arrString.length == 1 && arrString == 'a'){
        return n;
    } else if (!arrString.includes("a")) {
        return 0;
    }
    
    // check total of 'a'
    let num_a = 0;
    for(let i = 0; i < arrString.length; i++){
        if(arrString[i] == 'a'){
            num_a++;
        }
    }

    let mod_str = n % arrString.length;
    // check mod string
    if (mod_str == 0) {
        return Math.floor(n / arrString.length) * num_a;

    } else {
        // check total last of 'a'
        let last_a = 0;
        for(let i = 0; i < mod_str; i++){
            if(arrString[i] == 'a'){
                last_a++;
            }
        }
        
        return Math.floor(n / arrString.length) * num_a + last_a;
    }
}

console.log(repeatedString('epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq', 549382313570));
