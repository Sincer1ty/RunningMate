// 헤더 공통부분 

function profile() {
    alert('정보수정으로 가기');
}

function Title() {
    alert('메인으로 가기');
}

function LogOut() {
    confirm('로그아웃하시겠습니까?');
}

// 내가만든 스터디그룹

function CardTitle() {
    alert('스터디그룹 상세내용 모달창');
}

function Correction() {
    alert('수정페이지로 이동');
}

function Delete() {
    confirm('삭제하시겠습니까?');
}

function Create() {

    list = $('#subject > .selected');

    level = $('#level > .selected').text();
    mood=$('#mood > .selected').text();

    let array = [];
    for (let i = 0; i < list.length; i++) {

        keyword = list[i].value;
        array.push(keyword);
        console.log(array);
    }

    on_off = $('#on_off option:selected').text()
    loc = $('#location option:selected').text()

    $.ajax({
        type: "POST",
        url: "/make",
        data: {
            keyword1: array[0], keyword2: array[1], keyword3: array[2],
            mode: 'ajax', on_off_give: on_off, location_give: loc,
            level: level, mood: mood
        },
        success: function (response) { // 성공하면
            if (response['result'] == 'success') {
                alert(response['msg']);
            }
        }
    })
}

// 로그인

function Login() {
    alert('로그인 아이디 비밀번호');
}

function Join() {
    alert('회원가입페이지');
}

function FindPass() {
    alert('비밀번호 찾기');
}

// 회원가입

function JoinConf() {
    alert('회원가입 완료');
}

function IdCheck() {
    alert('아이디중복확인');
}

function NickCheck() {
    alert('닉네임중복확인');
}

function Interest() {
    alert('흥미체크중복확인');
}

$(document).ready(function () {
    //on-off
    OnOffSelect = document.querySelector('#on_off')
    LocationSelect = document.querySelector('#location')

    OnOffSelect.addEventListener('change', (event) => {
        console.log('on-off');
        if (event.target.value == "off") {
            $('#location > #on').css('display', 'none');
            $('#location > #off').css('display', 'block');
            LocationSelect.value = $('#location > #off')[0].text;
        }
        else {
            $('#location > #on').css('display', 'block');
            $('#location > #off').css('display', 'none');
            LocationSelect.value = $('#location > #on')[0].text;
        }
    })

    $('.toggle').click(function () {


        list = $(this).parent().children();
        console.log($(this).prop('tagName'));
        flag = false;
        if ($(this).prop('tagName') == 'INPUT') {
            console.log('tagName: INPUT');
            //input 이면 중복 허용
            $(this).toggleClass('selected');
        }
        else {
            //selected class 를 가진 div 가 하나 이상이면 막기
            if (list.hasClass('selected')) {
                console.log('if');
                flag = true;
            }

            if (!flag) {
                $(this).toggleClass('selected');

                console.log('check');
            }
            else {
                flag = false;
                $(this).removeClass('selected');

                console.log('off');
            }
        }
    });

    $('#addButton').click(function () {
        const inputBox = $(this).next('.new-input');
        if (inputBox.length) {
            inputBox.remove();
        } else {
            const newInputBox = $('<input type="text" class="new-input bg-gray-200 text-gray-700 px-3 py-2 rounded-lg focus:outline-none" placeholder="New Keyword" />');
            newInputBox.on('keypress', function (event) {
                if (event.which == 13) { // Enter key pressed
                    const keyword = $(this).val();
                    if (keyword.trim() !== '') {
                        const newElement = $(`<input type="text" name="keyword1" value="${keyword}" readonly
                class="w-full bg-gray-200 p-2 text-gray-700 hover:bg-gray-300 focus:outline-none rounded-md h-10 drag-n cursor-pointer toggle" />`);
                        newElement.click(function () {
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