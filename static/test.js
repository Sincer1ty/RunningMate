$(document).ready(function () {
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
                flag=false;
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