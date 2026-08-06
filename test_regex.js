let data = {className: '8/4_cs5'};
let classClean = '';
if (data.className && data.className !== 'Chưa rõ') {
    let match = data.className.match(/^(\d+)[\/\-_](\d+)/);
    if (match) {
        const numMapGrade = {'1':'một','2':'hai','3':'ba','4':'bốn','5':'năm','6':'sáu','7':'bảy','8':'tám','9':'chín','10':'mười','11':'mười một','12':'mười hai'};
        const numMapClass = {'1':'một','2':'hai','3':'ba','4':'tư','5':'năm','6':'sáu','7':'bảy','8':'tám','9':'chín','10':'mười','11':'mười một','12':'mười hai'};
        classClean = ` ${numMapGrade[match[1]] || match[1]} ${numMapClass[match[2]] || match[2]}`;
    } else {
        console.log("No match");
    }
}
console.log(classClean);
