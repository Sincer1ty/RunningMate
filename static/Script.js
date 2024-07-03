// 헤더 공통부분 

function profile(){
    alert('정보수정으로 가기');
}

function myStudy() {
    window.location.href = "/MyStudy";
  }

function main(){
    window.location.href = "/";
}

function login(){
    window.location.href = "/login";
}

// 내가만든 스터디그룹

function CardTitle(){
    alert('스터디그룹 상세내용 모달창');
}

function Correction() {
    window.location.href = '/edit';
}

function Delete(){
    confirm('삭제하시겠습니까?');
}

// 로그인

function Login(){
    alert('로그인 아이디 비밀번호');
}

function Join(){
    alert('회원가입페이지');
}

function FindPass(){
    alert('비밀번호 찾기');
}

function changePw() { 
    window.location.href = '/change_pw';
}
// 회원가입

function JoinConf() {
    
    alert('회원가입 완료');

}


function matching() {
    window.location.href = "/matching";

}

function create() {
    window.location.href = "/create";
}
  
function IdCheck() {
    let currentID = $('#email').val();

    $.ajax({
        type: "POST",
        url: "/idCheck",
        data: { currentID : currentID },
        success: function(response){
            console.log(response)
            alert(response);
            // 리스폰스만 얼럿이 뜨는 이유가 뭘까?
        }
    })


    
    // alert(currentID);
  
   
}

function NickCheck() {
    let currentNickname = $('#nickname').val();
    $.ajax({
        type: "POST",
        url: "/nickCheck",
        data: { currentNickname : currentNickname },
        success: function(response){
            console.log(response)
            alert(response);
            // 리스폰스만 얼럿이 뜨는 이유가 뭘까?
        }
    })
}

function Interest(){
    alert('흥미체크중복확인');
}



$(document).ready(function () {
  
    

    //대면인지 비대면인지에 따라 지역 또는 플랫폼을 고르는 form으로 변경
    document.getElementById("on-off").addEventListener("change", function() {
        const selectedIndex = this.selectedIndex;
        if (selectedIndex === 1) {
            $('#online').addClass('hidden');
            $('#offline').removeClass('hidden');
        }
        else { 
            $('#offline').addClass('hidden');
            $('#online').removeClass('hidden');
        }
    });
    $('.radio').click(function() {
        // 이전에 선택된 div가 있으면 클래스 제거 및 배경색 복원
        const selectedDiv = $('.selected');
        if (selectedDiv.length && selectedDiv[0] !== this) {
            selectedDiv.removeClass('selected').removeClass('bg-blue-500').addClass('bg-gray-200');
        }

        // 현재 클릭된 div에 selected 클래스 추가 및 배경색 변경
        $(this).addClass('selected').removeClass('bg-gray-200').addClass('bg-blue-500');
        if (this.id === 'offlineBtn') {
            $('#offlineform').removeClass('hidden');
            $('#onlineform').addClass('hidden');
        } else if (this.id === 'onlineBtn') {
            $('#onlineform').removeClass('hidden');
            $('#offlineform').addClass('hidden');
        }
    });
    $('.toggle').click(function() {
        $(this).toggleClass('selected');
        if ($(this).hasClass('selected')) {
            $(this).css('background-color', '#4caf50');
            $(this).css('color', 'white');
        } else {
            $(this).css('background-color', '');
            $(this).css('color', '');
        }
    });

    $('#addButton').click(function () {
        const inputBox = $(this).next('.new-input');
        if (inputBox.length) {
            inputBox.remove();
        } else {
            const newInputBox = $('<input type="text" class="new-input bg-gray-200 text-gray-700 px-3 py-2 rounded-lg focus:outline-none" placeholder="New Keyword" />');
            newInputBox.on('keypress', function(event) {
                if (event.which == 13) { // Enter key pressed
                    const keyword = $(this).val();
                    if (keyword.trim() !== '') {
                        const newElement = $('<div id="subject" class="toggle-button bg-gray-200 text-gray-700 px-3 py-2 rounded-lg hover:bg-gray-300 focus:outline-none"></div>').text(keyword);
                        newElement.click(function() {
                            $(this).toggleClass('selected');
                            if ($(this).hasClass('selected')) {
                                $(this).css('background-color', '#4caf50');
                                $(this).css('color', 'white');
                            } else {
                                $(this).css('background-color', '');
                                $(this).css('color', '');
                            }
                        });
                        $('#addButton').before(newElement);
                    }
                    $(this).remove(); // Remove the input box after adding the keyword
                }
            });
            $(this).after(newInputBox);
            newInputBox.focus(); // Focus on the input box
        }
    });
});
