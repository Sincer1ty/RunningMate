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

function toggleCategory(element) {
    // 클릭된 항목의 선택 상태를 토글합니다
    element.classList.toggle('selected');
}

// 추가버튼

document.addEventListener('DOMContentLoaded', function() {
    const toggleItems = document.querySelectorAll('.Pbutton');
    const inputBox = document.getElementById('inputBox');
    const sideElementsContainer = document.getElementById('sideElements');

    toggleItems.forEach(item => {
        item.addEventListener('click', function() {
            toggleItems.forEach(i => i.classList.remove('selected'));
            this.classList.add('selected');
            inputBox.style.display = 'block'; // Show input box
        });
    });

    inputBox.addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            const inputValue = inputBox.value.trim();
            if (inputValue) {
                // Create a new side element
                const sideElement = document.createElement('div');
                sideElement.classList.add('tag-toggle'); // Add class
                sideElement.onclick = function() {
                    toggleCategory(this); // Add onclick function
                };
                const img = document.createElement('img');
                img.classList.add('check');
                img.src = 'check0.svg'; // Set image source
                const title = document.createElement('div');
                title.classList.add('title');
                title.textContent = inputValue; // Set title text
                sideElement.appendChild(img);
                sideElement.appendChild(title);
                sideElementsContainer.appendChild(sideElement);

                inputBox.value = ''; // Clear input
                inputBox.style.display = 'none'; // Hide input box
            }
        }
    });
});