
let sum = arr => {let c=0; for (let i of arr) c+=i; return c;};

function b64to10(b64, base=64){
    let vals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
    return sum([...b64].map((b,n)=>vals.indexOf(b)*Math.pow(base, b64.length-1-n)));
};


function nearest_even(n) {
    'Returns the higest power of 2 less than n'
    let i=0;
    while ((n - Math.pow(2,i+1))>=0) i++;
    return i;
}

function nearest_pow(num, int=2){
    'Returns the higest power of int less than num'
    let i=0;
    while ((num - Math.pow(int,i+1))>=0) i++;
    return i;
}

/** Same as above but lesser code
function nearest_even(n) {
    for (let i=0; (n - Math.pow(2,i+1))>=0; i++);
    return i;
}

function nearest_pow(int, num){
   for (let i=0; (num - Math.pow(int,i+1))>=0; i++);
   return i;
}
*/

function b10to2 (dec){
    let pows = {};
    while (dec){
        let pow = nearest_even(dec);
        pows[pow]=1;
        dec-=Math.pow(2,pow);
    }
    let intarr = Array(Math.max(...Object.keys(pows))).fill(0); // make an array of 0s (length = highest power of 2 divisible by dec)
    for (let _p of Object.keys(pows))
        intarr[_p] = 1;
    return intarr.reverse().join('');}


function nearest_pow_num(n, base){
    'Returns [X = highest power of base less than n, highest multiple of 3*X less than n]'
    let nums = irange(base).reverse();
    let i=0;
    let q = nearest_pow;
    while (true) {
        if ((Math.pow(base,q(n,base))*nums[i])<=n)
            return [q(n,base), nums[i]];
        i++;
    }
}


function nearest_char_pow_num(n, chars) {
    chars = chars instanceof Array? chars: [...chars];
    let nums = chars.map((i,n)=>n).reverse();
    chars = chars.reverse();
    let i = 0;
    let base=chars.length;
    let q = nearest_pow;
    while (true){
        if ((Math.pow(base,q(n,base))*nums[i])<=n)
            return [chars[i], q(n,base), nums[i]];
        i++;
    }
}

function b10to3 (dec) {
    let pows = {};
    while (dec){
        let [pow, mul] = nearest_pow_num(dec, 3);
        pows[pow] = mul;
        dec -= mul*Math.pow(3,pow);
    }
    let intarr = Array(Math.max(...Object.keys(pows))).fill(0); // make an array of 0s (length = highest power of 2 divisible by dec)
    for (let [p,m] of Object.entries(pows))
        intarr[p] = m;
    return intarr.reverse().join('');}


function b10toN (dec, N=2) {
    console.assert(N<=10 && N >=2, "N must be 10 >= N >= 2");
    let pows = {};
    while (dec){
        let [pow, mul] = nearest_pow_num(dec, N);
        pows[pow] = mul;
        dec -= mul*Math.pow(N,pow);
    }
    let intarr = Array(Math.max(...Object.keys(pows))).fill(0); // make an array of 0s (length = highest power of 2 divisible by dec)
    for (let [p,m] of Object.entries(pows))
        intarr[p] = m;
    return intarr.reverse().join('');}


function b10toAny(dec, chars) {
    let N = chars.length;
    console.assert(N >=2, "N must be N >= 2");
    let pows={};
    while (dec) {
        let [pow, mul] = nearest_pow_num(dec, N);
        pows[pow] = mul;
        dec -= mul*Math.pow(N,pow);
    }
    let intarr = Array(Math.max(...Object.keys(pows))).fill(0); // make an array of 0s (length = highest power of 2 divisible by dec)
    for (let [p,m] of Object.entries(pows))
        intarr[p] = chars[m];
    return intarr.reverse().join('');
}

let b10to64 = dec => b10toAny(dec, 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/');