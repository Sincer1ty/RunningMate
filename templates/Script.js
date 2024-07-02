// 헤더 공통부분 

function profile(){
    alert('정보수정으로 가기');
}

function Title(){
    alert('메인으로 가기');
}

function LogOut(){
    confirm('로그아웃하시겠습니까?');
}

// 내가만든 스터디그룹

function CardTitle(){
    alert('스터디그룹 상세내용 모달창');
}

function Correction(){
    alert('수정페이지로 이동');
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

// 회원가입

function JoinConf(){
    alert('회원가입 완료');
}

function IdCheck(){
    alert('아이디중복확인');
}

function NickCheck(){
    alert('닉네임중복확인');
}

function Interest(){
    alert('흥미체크중복확인');
}

$(document).ready(function() {
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

    $('#addButton').click(function() {
        const inputBox = $(this).next('.new-input');
        if (inputBox.length) {
            inputBox.remove();
        } else {
            const newInputBox = $('<input type="text" class="new-input bg-gray-200 text-gray-700 px-3 py-2 rounded-lg focus:outline-none" placeholder="New Keyword" />');
            newInputBox.on('keypress', function(event) {
                if (event.which == 13) { // Enter key pressed
                    const keyword = $(this).val();
                    if (keyword.trim() !== '') {
                        const newElement = $('<div class="toggle-button bg-gray-200 text-gray-700 px-3 py-2 rounded-lg hover:bg-gray-300 focus:outline-none"></div>').text(keyword);
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
