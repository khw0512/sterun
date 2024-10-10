var infoMonth = document.querySelector('.infoMonth');
var infoDay = document.querySelector('.infoDay');
var selFormArr = Array.from(Array(1), () => Array(2).fill(null));
var daySel = $('.selected').length + 1;

var tableTr = document.getElementsByClassName("date-cell");

// row 선택 시 event
for(var i = 0; i < tableTr.length; i++) {
    $(tableTr).click(function(e) {
        tableTrClick(e);
    });
}

// row 선택 시 색깔 변경 나머지 원래대로
function tableTrClick(e) {
    if($(e.target.parentElement).hasClass("selected") && e.target.textContent !=0) {
        $(e.target.parentElement).removeClass('selected');
        $(e.target.parentElement.parentElement).removeClass('selected');
    } else {
        for(var i = 0; i < tableTr.length; i++) {
            tableTr[i].classList.remove('selected');
            try{
                tableTr[i].parentElement.classList.remove('selected');

            }
            catch(e){
                console.log('None Class')
            }
        }
    }
    if(e.target.textContent !=0){
        $(e.target.parentElement).addClass('selected');
    };
    
    if(e.target.parentElement.children[0].textContent!='' && e.target.parentElement.children[0].textContent.length<3){
        infoMonth.innerHTML=month+'월';
        infoDay.innerHTML=e.target.parentElement.children[0].textContent + '일';
    }
    else{
        infoMonth.innerHTML='-';
        infoDay.innerHTML='-';
    }

}