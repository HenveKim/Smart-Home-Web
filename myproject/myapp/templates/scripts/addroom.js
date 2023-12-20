document.getElementById('addRoomForm').addEventListener('submit', function(event) {
    event.preventDefault(); // 阻止默认提交行为

    const newRoomName = document.getElementById('newRoomName').value;
    if (newRoomName.trim() !== '') {
        // 创建一个新的房间号，可以基于已有房间数量自动生成
        const newRoomNumber = document.querySelectorAll('.furniture-form').length + 1;

        // 创建一个新的房间按钮
        const newRoomButton = document.createElement('button');
        newRoomButton.textContent = newRoomName;
        newRoomButton.setAttribute('onclick', `toggleForm('room${newRoomNumber}')`);
        document.body.insertBefore(newRoomButton, document.getElementById('addRoomForm'));

        // 创建一个新的房间表单
        const newForm = document.createElement('form');
        newForm.id = `room${newRoomNumber}`;
        newForm.className = 'furniture-form';
        newForm.action = "/submit_furniture";
        newForm.method = "post";
        // ...其他房间表单元素，与之前类似...

        // 将新表单添加到页面中
        document.body.appendChild(newForm);

        // 重置新房间输入表单
        document.getElementById('newRoomName').value = '';
    } else {
        alert("请输入新房间的名称！");
    }
});

// 现有的房间切换函数和其他部分保持不变
